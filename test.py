from decouple import config
import requests
import random
import boto3
headers = {
                'Authorization': config('PEXELS_API_KEY')
            }

            #Change query to try except with decreasing num of nouns
query = "test"

endpoint = f"https://api.pexels.com/v1/search?query={query}&per_page=5"

response = requests.get(url=endpoint, headers=headers)

print((len(response.json()['photos'])))


image_chosen = random.randint(0, (len(response.json()['photos'])-1))
url = f"{(response.json()['photos'][image_chosen]['src']['large'])}"
            
#uplaod to s3 using url then cretae a aws lambda function which "cleans" the image

r = requests.get(url, stream=True)

session = boto3.Session()
s3 = session.resource('s3')

bucket_name = 'strategy-ahead-resized'
key = f"temp-images/{url.split('/')[-1].split('?')[0]}" # key is the name of file on your bucket

bucket = s3.Bucket(bucket_name)
bucket.upload_fileobj(r.raw, key)

#set up lambda to resize the image/clean