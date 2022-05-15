import asyncio
import aiohttp
import os
import time
download_uris = [
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip'
]

api_key = os.getenv('ALPHAVANTAGE_API_KEY')


start = time.time()

def get_tasks(session):
    tasks = []
    for url in download_uris:
        tasks.append(asyncio.create_task(session.get(url.format(url, api_key), ssl=False)))
    return tasks

async def get_symbols():
    async with aiohttp.ClientSession() as session:
        tasks = get_tasks(session)
        # you could also do
        # tasks = [session.get(URL.format(symbol, API_KEY), ssl=False) for symbol in symbols]
        responses = await asyncio.gather(*tasks)
        # for response in responses:
        #     results.append(await response.json())

asyncio.run(get_symbols())

end = time.time()
total_time = end - start
print("It took {} seconds to make {} API calls".format(total_time, len(symbols)))
print('You did it!')
