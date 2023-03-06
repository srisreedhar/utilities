from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import csv
import os

# authenticate and create a Google Drive API client
gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

# FolderID -> Destination
folder_id = 'your_folder_id'

# define the chunk size (number of rows per file)
chunk_size = 1000

# open the large CSV file and read the header row
with open('large_file.csv', 'r') as file:
    reader = csv.reader(file)
    header = next(reader)

    # loop through the rows in the file and create chunks
    chunk_number = 1
    current_chunk_size = 0
    current_chunk_data = []
    for row in reader:
        current_chunk_data.append(row)
        current_chunk_size += 1

        # if the chunk size is reached, create a new file and upload it to Google Drive
        if current_chunk_size == chunk_size:
            # create a new file in Google Drive
            file_name = f'chunk_{chunk_number}.csv'
            file_metadata = {'title': file_name, 'parents': [{'id': folder_id}]}
            file_drive = drive.CreateFile(file_metadata)
            file_drive.Upload()

            # write the chunk data to a CSV file and upload it to Google Drive
            with open(file_name, 'w', newline='') as chunk_file:
                writer = csv.writer(chunk_file)
                writer.writerow(header)
                writer.writerows(current_chunk_data)
            chunk_file.close()

            # reset the chunk variables for the next chunk
            chunk_number += 1
            current_chunk_size = 0
            current_chunk_data = []

    # upload the final chunk (if there are any remaining rows)
    if current_chunk_size > 0:
        # create a new file in Google Drive
        file_name = f'chunk_{chunk_number}.csv'
        file_metadata = {'title': file_name, 'parents': [{'id': folder_id}]}
        file_drive = drive.CreateFile(file_metadata)
        file_drive.Upload()

        # write the chunk data to a CSV file and upload it to Google Drive
        with open(file_name, 'w', newline='') as chunk_file:
            writer = csv.writer(chunk_file)
            writer.writerow(header)
            writer.writerows(current_chunk_data)
        chunk_file.close()

print("Chunks uploaded successfully!")
