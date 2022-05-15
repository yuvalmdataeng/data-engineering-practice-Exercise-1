import requests
import os
import zipfile
download_uris = [
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip'
]
#create the directory downloads if it doesn't exist
def directory_creation():
    path = '/Users/yuval.mutseri/repos/data-engineering-practice/Exercises/Exercise-1/downloads'
    # Check whether the specified path exists or not
    isExist = os.path.exists(path)
    if not isExist:
        # Create a new directory because it does not exist
        os.makedirs(path)
        print(f"The new directory {path} is created!")
    else:
        print(f"The directory {path} already exist")
#download the files one by one.
def download_files(url_list):
    for url in download_uris:
        # split out the filename from the uri, so the file keeps its original filename.
        file_name = url.split("/")[-1]
        r = requests.get(url)
        status = r.status_code
        print("Status of file", file_name, "is", status)
        if status == 200:
            save_path = '/Users/yuval.mutseri/repos/data-engineering-practice/Exercises/Exercise-1/downloads'
            completeName = os.path.join(save_path, file_name)
            with open(completeName, 'wb') as f:
                f.write(r.content)
            print(completeName, "Was written")
            # Each file is a zip, extract the csv from the zip and delete the zip file.
            with zipfile.ZipFile(completeName,'r') as zip_ref:
                zip_ref.extractall( save_path)
            if os.path.exists(completeName):
                os.remove(completeName)
            else:
                print("The file does not exist")
        else:
            print("Status is bad, continue to next file")
    print("Downloaded all valid files")
#For extra credit, download the files in an async manner using the Python package aiohttp. Also try using ThreadPoolExecutor in Python to download the files. Also write unit tests to improve your skills.

def main():
    directory_creation()
    download_files(download_uris)
if __name__ == '__main__':
    main()

