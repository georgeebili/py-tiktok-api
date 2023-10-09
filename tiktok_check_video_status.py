import requests

def check_status():
    # Replace these values with your actual data
    # Your TikTok access token
    access_token = ''
    publish_id = ''

    # TikTok API endpoint
    endpoint = 'https://open.tiktokapis.com/v2/post/publish/status/fetch/'

    # Set headers
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json; charset=UTF-8',
    }

    # Create the JSON data payload
    data = {
        'publish_id': publish_id
    }

    # Send the POST request
    response = requests.post(endpoint, headers=headers, json=data)

    # Check the response
    if response.status_code == 200:
        print('Request successful.')
        response_data = response.json()
        # Process the response data here
        print('Response data:', response_data)
    else:
        print(f'Error: {response.status_code} - {response.text}')
