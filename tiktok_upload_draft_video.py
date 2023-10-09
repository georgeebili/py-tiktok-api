import os
import math
import requests
import json

# Replace with the path to your video file
video_file_path = 'C:/Users/george/Downloads/part1.mp4'

# TikTok API endpoint for initiating video upload
init_upload_endpoint = 'https://open.tiktokapis.com/v2/post/publish/inbox/video/init/'

# Your TikTok access token
access_token = ''

# Calculate the video size in bytes
video_size = os.path.getsize(video_file_path)

# Define the chunk size (e.g., 1MB)
chunk_size = min(video_size, 5 * 1024 * 1024)  # 1MB in bytes

print(chunk_size, video_size)
# Calculate the total number of chunks
chunk_count = int(video_size / chunk_size)

# Initialize the video upload
init_upload_data = {
    'source_info': {
        'source': 'FILE_UPLOAD',
        'video_size': video_size,
        'chunk_size':chunk_size,
        'total_chunk_count': chunk_count
    }
}

headers = {
    'Authorization': 'Bearer ' + access_token,
    'Content-Type': 'application/json; charset=UTF-8',
}

# Disable SSL certificate verification (for testing purposes)
requests.packages.urllib3.disable_warnings()

#print(init_upload_data)
# Make the POST request
response = requests.post(init_upload_endpoint, json=init_upload_data, headers=headers, verify=False)
#response = requests.post(init_upload_endpoint, data=json.dumps(init_upload_data), headers=headers, verify=False)

if response.status_code != 200:
    print('Error initializing upload:', response.text)
    exit()
else:
    print('Response Data: \n',response.json())

upload_url = response.json()['data']['upload_url']
publish_id = response.json()['data']['publish_id']

# Upload video in chunks
with open(video_file_path, 'rb') as video_file:
    for chunk_number in range(chunk_count):
        start_byte = chunk_number * chunk_size
        end_byte = min((chunk_number + 1) * chunk_size, video_size)
        chunk_size = end_byte - start_byte

        headers = {
            'Content-Type': 'video/mp4',
            'Content-Range': f'bytes {start_byte}-{end_byte - 1}/{video_size}',
            'Content-Length': str(chunk_size),
        }

        video_chunk = video_file.read(chunk_size)
        response = requests.put(upload_url, data=video_chunk, headers=headers, verify=False)

        if response.status_code != 206:
            print(f'Error uploading chunk {chunk_number + 1}:', response.text)
            exit()
        else:
            print(response.text)

print('Video upload complete.', upload_url, publish_id)
