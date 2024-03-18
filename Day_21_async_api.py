import requests
from pprint import pprint
import aiohttp
import asyncio
from time import time

TOKEN = "56cb09d3121e47ed8f793329241503"

# Sync
# def get_city_temp(city_name):
#   response =  requests.get(f"https://api.weatherapi.com/v1/current.json?key={TOKEN}&q={city_name}&aqi=no", verify=False)
#   weather = response.json()
#   return f"The temperature in {weather['location']['name']} is {weather['current']['temp_c']}°C"

# print(get_city_temp("Cape Town"))


# async def get_city_temp(city_name):
#     print(f"Getting temp of {city_name}")
#     await asyncio.sleep(2)
#     url = f"https://api.weatherapi.com/v1/current.json?key={TOKEN}&q={city_name}&aqi=no"
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url) as response:
#             weather = await response.json()
#             print(
#                 f"The temperature in {weather['location']['name']} is {weather['current']['temp_c']}°C"
#             )


# # task 1: gather tasks
# async def main():
#     all_co_routines = [
#         get_city_temp("Chennai"),
#         get_city_temp("Johannesburg"),
#         get_city_temp("Durban"),
#     ]
# schedule starts here without create_task
#     await asyncio.gather(*all_co_routines)


# task 2: gather tasks and create task
# async def main():
#     all_tasks = [
# schedule starts right there with create_task
#         asyncio.create_task(get_city_temp("Chennai")),
#         asyncio.create_task(get_city_temp("Johannesburg")),
#         asyncio.create_task(get_city_temp("Durban")),
#     ]
#     await asyncio.gather(*all_tasks)
# * will unpack each element, each element is parsed as a co routine

# Task 3 - dry
cities = [
    "New York",
    "Tokyo",
    "London",
    "Paris",
    "Dubai",
    "Singapore",
    "Sydney",
    "Istanbul",
    "Hong Kong",
    "Cape Town",
]


# task 3: dry with cities
# async def main():
#     # list comp will still it all in one
#     tasks = [get_city_temp(city) for city in cities]
#     await asyncio.gather(*tasks)
#     # gather will fire it at the same time


# task 4: create a func which takes a list of cities and provide the corresponding temperature in a dict
# async
# clues -> 1. dict(arr), 2. return value
async def get_city_name_temp(city_name):
    print(f"Getting temp of {city_name}")
    url = f"https://api.weatherapi.com/v1/current.json?key={TOKEN}&q={city_name}&aqi=no"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            weather = await response.json()
            return (weather["location"]["name"], weather["current"]["temp_c"])


# async def main(cities):
#     # print(await get_city_name_temp("New York"))
#     # print(await get_city_name_temp("Hong Kong"))
#     cities_data = [await get_city_name_temp(city) for city in cities]
#     pprint(dict(cities_data))


# asyncio.run(main(cities))


# Performance
async def main(cities):
    cities_data_co_current = [get_city_name_temp(city) for city in cities]
    cities_data = await asyncio.gather(*cities_data_co_current)
    pprint(dict(cities_data))


# time taken and run
start_time = time()
asyncio.run(main(cities))
end_time = time()

print(f"Time take: {end_time - start_time}")
# asyncio.run(get_city_temp("Chennai"))
# asyncio.run(get_city_temp("Johannesburg"))
# asyncio.run(get_city_temp("Durban"))
