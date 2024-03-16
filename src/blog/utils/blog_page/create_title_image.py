from decouple import config
import requests
import random
import boto3
import time
import shutil
from PIL import Image
import math
from PIL import ImageDraw, ImageFont
from product_launch_site.settings import BASE_DIR

   
def create_title_image(title):
    headers = {
                    'Authorization': config('PEXELS_API_KEY')
                }

    query = title.split(' ')[-1]

    endpoint = f"https://api.pexels.com/v1/search?query={query}&per_page=5"

    response = requests.get(url=endpoint, headers=headers)


    image_chosen = random.randint(0, (len(response.json()['photos'])-1))
    url = f"{(response.json()['photos'][image_chosen]['src']['large'])}"
                
    #uplaod to s3 using url then cretae a aws lambda function which "cleans" the image

    r = requests.get(url, stream=True)

    session = boto3.Session()
    s3 = session.resource('s3')

    bucket_name = 'strategy-ahead'
    key = f"temp-images/{url.split('/')[-1].split('?')[0]}" # key is the name of file on your bucket

    bucket = s3.Bucket(bucket_name)
    bucket.upload_fileobj(r.raw, key)

    #set up lambda to resize the image/clean (done)

    #add a wait to #access the cleaned image and process


    url = f'https://strategy-ahead.s3.amazonaws.com/resized-temp-images/{key.split('/')[-1]}'

    time.sleep(5)
    response = requests.get(url, stream=True)

    with open('img.png', 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response


    im = Image.open("img.png")
    # im.show()

    #crop iamge to required dimensions

    width, height = im.size


    # w/h 1.5 ratio 1000wide , 667 tall #resize so minimum is 667height  or 1000 wide then crop

    if width < 1000:
        width_new_old_ratio = 1000/width
        new_height = height * width_new_old_ratio

        im = im.resize((1000, math.floor(new_height)))
    if height < 667:
        height_new_old_ratio = 667/height
        new_width = width * height_new_old_ratio

        im = im.resize((math.floor(new_width), 667))

    centerx, centery = math.floor(width/2), math.floor(height/2)

    img = im.crop(box=(centerx-500,centery-333, centerx+500,centery+333))


    im.save("img2.png")


    #add text from top left corner 

    W = int(img.size[0])
    H = int(img.size[1])
    draw = ImageDraw.Draw(img)


    def wrap_text(text, width, font):
        text_lines = []
        text_line = []
        text = text.replace('\n', ' [br] ')
        words = text.split()
    #As text is same calculate this once and then save the result so ready for next
        for word in words:
            if word == '[br]':
                text_lines.append(' '.join(text_line))
                text_line = []
                continue
            text_line.append(word)
            x1, y1, x2, y2 = font.getbbox(' '.join(text_line))
            w = x2 - x1
            if w > width:
                text_line.pop()
                text_lines.append(' '.join(text_line))
                text_line = [word]

        if len(text_line) > 0:
            text_lines.append(' '.join(text_line))

        return text_lines

    title = f"{title}".upper()
    def text_wrapped(font_size):
            print('BASE_DIR', BASE_DIR)
            if str(BASE_DIR) == "/APP/src":
                font_path = f'{BASE_DIR}/blog/utils/blog_page/Montserrat-Bold.ttf'
            else:
                font_path = f'{BASE_DIR}\\blog\\utils\\blog_page\\Montserrat-Bold.ttf'
            print(font_path)
            font2 = ImageFont.truetype(font_path, font_size)
            msg2 = wrap_text(text=title, width=600, font=font2)

            _, _, width, text_height = draw.textbbox((0, 0), text=title, font=font2)

            line_spacing = text_height * 1.5
            total_text_height = len(msg2)*line_spacing

            return locals()

    starting_font = 90
    text_wrapped_vars = text_wrapped(starting_font) 
    msg2 = text_wrapped_vars['msg2']
    line_spacing = text_wrapped_vars['line_spacing']
    font2 = text_wrapped_vars['font2']
    h_title=0
    total_text_height = text_wrapped_vars['total_text_height']

    longest_line = 0
    for x in msg2:
        line_length = draw.textlength( x, font=font2)
        if line_length > longest_line:
            longest_line = line_length

    while total_text_height > 600 or longest_line > 600:
                    starting_font -= 5
                    text_wrapped_vars = text_wrapped(starting_font) 
                    msg2 = text_wrapped_vars['msg2']
                    line_spacing = text_wrapped_vars['line_spacing']
                    font2 = text_wrapped_vars['font2']
                    h_title=0
                    total_text_height = text_wrapped_vars['total_text_height'] 
                
                    longest_line = 0
                    for x in msg2:
                        line_length = draw.textlength( x, font=font2)
                        if line_length > longest_line:
                            longest_line = line_length

    for text in msg2:
            _, _, width, height = draw.textbbox((0, 0), text=text, font=font2)

            #now create a rectangle using pillo
            padding = height *0.1
            draw.rectangle((100-padding , 
                            h_title+((H-total_text_height)/2) -padding ,
                            100 + width +padding , 
                            h_title+((H-total_text_height)/2) + height +padding),
                            
                            fill="black")

            draw.text((100, (h_title+((H-total_text_height)/2))), text , (255, 255, 255), font=font2) 
            h_title += line_spacing


    img.save('img.jpg', 'JPEG', quality=85) # save image to BytesIO object

    return img



# image = File(img_io, name=f"{uuid4()}.jpg") # create a django friendly File object

# to do:  transfer code as a function to override default save method delete unnecesssary files, here and in s3, , keep save method clean should bea simple function call create_title_image(self)
