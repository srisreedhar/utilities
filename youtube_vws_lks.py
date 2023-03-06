# Import the necessary libraries
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os
import pandas as pd
import csv


# Define the API credentials and build the YouTube API client
API_KEY = 'YOUR_API_KEY_HERE'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'
youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=API_KEY)


# Define the channel ID for which you want to get video details
channel_id = 'CHANNEL_ID_HERE'

try:
    # Use the channels().list method to get the channel details
    channel_response = youtube.channels().list(
        part='statistics',
        id=channel_id
    ).execute()

    # Get the total number of views and subscribers for the channel
    total_views = channel_response['items'][0]['statistics']['viewCount']
    total_subscribers = channel_response['items'][0]['statistics']['subscriberCount']

    # Use the search().list method to get the videos for the channel
    search_response = youtube.search().list(
        part='id,snippet',
        channelId=channel_id,
        maxResults=50
    ).execute()

    # Loop through each video and get the details
    for item in search_response['items']:
        if item['id']['kind'] == 'youtube#video':
            video_id = item['id']['videoId']
            video_title = item['snippet']['title']

            # Use the videos().list method to get the video details
            video_response = youtube.videos().list(
                part='statistics',
                id=video_id
            ).execute()

            # Get the number of views and likes for the video
            views = video_response['items'][0]['statistics']['viewCount']
            likes = video_response['items'][0]['statistics']['likeCount']

            # Print the video details
            print(f'Title: {video_title}')
            print(f'Views: {views}')
            print(f'Likes: {likes}')
            print('---')

except HttpError as error:
    print(f'An HTTP error {error.resp.status} occurred: {error.content}')


# write to CSV


# Upload CSV to Google Drive