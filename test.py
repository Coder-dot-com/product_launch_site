from decouple import config
import requests
import random
import boto3
import time
headers = {
                'Authorization': config('PEXELS_API_KEY')
            }

            #Change query to try except with decreasing num of nouns
query = "apple"

endpoint = f"https://api.pexels.com/v1/search?query={query}&per_page=5"

response = requests.get(url=endpoint, headers=headers)

print((len(response.json()['photos'])))


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


import shutil


url = f'https://strategy-ahead.s3.amazonaws.com/resized-temp-images/{key.split('/')[-1]}'

time.sleep(2)
response = requests.get(url, stream=True)

with open('img.png', 'wb') as out_file:
    shutil.copyfileobj(response.raw, out_file)
del response

from PIL import Image

im = Image.open("img.png")
# im.show()

#crop iamge to required dimensions

width, height = im.size

print(width, height)

import math

# w/h 1.5 ratio 1000wide , 667 tall #resize so minimum is 667height  or 1000 wide then crop

if width < 1000:
    width_new_old_ratio = 1000/width
    new_height = height * width_new_old_ratio

    im = im.resize((1000, math.floor(new_height)))
elif height < 667:
    height_new_old_ratio = 667/height
    new_width = width * height_new_old_ratio

    im = im.resize((math.floor(new_width), 667))

centerx, centery = math.floor(width/2), math.floor(height/2)

im = im.crop(box=(centerx-500,centery-333, centerx+500,centery+333))


im.save("img2.png")

