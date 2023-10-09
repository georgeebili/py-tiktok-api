import requests
import json

def upload_via_url():
    # TikTok API endpoint for initiating video upload
    uploadEndpoint = 'https://open.tiktokapis.com/v2/post/publish/video/init/'

    # Your TikTok access token
    accessToken = ''

    # Data to send in the request body
    data = {
        'post_info': {
            'title': 'this will be a funny #cat video on your',
            'privacy_level': 'PUBLIC_TO_EVERYONE',
            'disable_duet': False,
            'disable_comment': True,
            'disable_stitch': False,
            'video_cover_timestamp_ms': 1000
        },
        'source_info': {
            'source': 'PULL_FROM_URL',
            'video_url': 'https://www.example.space/videos/1696518451part1.mp4'
        }
    }

    # Convert the data to JSON
    jsonData = json.dumps(data)

    # Set headers
    headers = {
        'Authorization': 'Bearer ' + accessToken,
        'Content-Type': 'application/json; charset=UTF-8',
    }

    # Disable SSL certificate verification (for testing purposes)
    requests.packages.urllib3.disable_warnings()

    # Send the POST request
    response = requests.post(uploadEndpoint, data=jsonData, headers=headers, verify=True)  # Set verify=True for SSL certificate verification

    # Check for errors
    if response.status_code != 200:
        print('Error:', response.status_code, response.text)
    else:
        # Handle the response (you may want to parse the JSON response)
        print('Response:', response.text)
