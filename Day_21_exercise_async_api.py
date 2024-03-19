import asyncio
import aiohttp
from pprint import pprint

# async def get_names(url):
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url) as response:
#             users = await response.json()
#             # print(users)
#     return "\n".join([user["name"] for user in users])


# async def main():
#     names_url = "https://65f82895b4f842e808871430.mockapi.io/users"
#     print("Task 5")
#     # do not need gather as we are firing one api
#     print(await get_names(names_url))


# delete user with id 10 with async
# async def delete_user_by_id(id):
#     url = f"https://65f82895b4f842e808871430.mockapi.io/users/{id}"
#     async with aiohttp.ClientSession() as session:
#         async with session.delete(url) as response:
#             user = await response.json()
#             return user


# async def main(id):
#     user = await delete_user_by_id(id)
#     print(user)


# asyncio.run(main(10))


# Task: delete first 5
# async def fetch_first_user_ids():
#     url = "https://65f8284cb4f842e808871337.mockapi.io/users"
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url) as response:
#             users = await response.json()
#             return [user["id"] for user in users[:5]]


# async def delete_user_by_id(id):
#     url = f"https://65f8284cb4f842e808871337.mockapi.io/users/{id}"
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url) as response:
#             return await response.json()


# async def main():
#     user_ids = await fetch_first_user_ids()
#     print(user_ids)
#     await asyncio.gather(*(delete_user_by_id(user_id) for user_id in user_ids))

# Ragavs code
# async def get_users():
#     url = f"{API}/users"
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url) as response:
#             users = await response.json()
#             return users


# async def delete_user_by_id(id):
#     url = f"{API}/users/{id}"
#     print(f"Deleting user...{id}")
#     async with aiohttp.ClientSession() as session:
#         async with session.delete(url) as response:
#             user = await response.json()
#             return user


# # Task - 1
# # Delete the first 5 users
# # Performant < 0.5s
# # Clue: 2 Steps
# # Clue: GET & Delete


# async def main():
#     users = await get_users()
#     first_five_users = users[:5]  # slice
#     first_five_users_co_routine = [
#         delete_user_by_id(user["id"]) for user in first_five_users
#     ]
#     deleted_users = await asyncio.gather(*first_five_users_co_routine)
#     pprint(deleted_users)
#     # pprint(first_five_users)
#     # print(len(first_five_users))


# asyncio.run(main())

# day 22 async post
# async def create_user(new_user):
#     print(new_user)
#     url = f"https://65f82895b4f842e808871430.mockapi.io/users"
#     async with aiohttp.ClientSession() as session:
#         async with session.post(url, json=new_user) as response:
#             user = await response.json()
#             return user

# # Task 2: Create 5 users using the user_list
# async def main():
#     # new_user = {
#     #     "name": "Dhara Tina Kara",
#     #     "avatar": "https://static.vecteezy.com/system/resources/previews/020/297/008/non_2x/south-africa-human-rights-day-march-21-for-greeting-card-poster-banner-template-free-vector.jpg",
#     # }
#     # user_data = await create_user(new_user)
#     # print(user_data)

#     user_list = ["Alex", "Gemma", "Thato", "Lilitha", "Dhara"]
#     create_user_tasks = [
#         create_user(
#             {
#                 "name": name,
#                 "avatar": "https://th.bing.com/th/id/OIP.K4XfRyYNnlwsR9-qdE-lrQAAAA?rs=1&pid=ImgDetMain",
#             }
#         )
#         for name in user_list
#     ]
#     user_data = await asyncio.gather(*create_user_tasks)
#     pprint(user_data)


# asyncio.run(main())

# task 3: human rights day
# async def fetch_users():
#     url = "https://65f82895b4f842e808871430.mockapi.io/users"
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url) as response:
#             users = await response.json()
#             return [user["id"] for user in users]


# async def update_avatar(user_id):
#     url = f"https://65f82895b4f842e808871430.mockapi.io/users/{user_id}"
#     data = {
#         "avatar": "https://static.vecteezy.com/system/resources/previews/020/297/008/non_2x/south-africa-human-rights-day-march-21-for-greeting-card-poster-banner-template-free-vector.jpg"
#     }
#     async with aiohttp.ClientSession() as session:
#         async with session.put(url, json=data) as response:
#             if response.status == 200:
#                 print(f"Avatar updated for user with ID {user_id}")
#             else:
#                 print(f"Failed to update avatar for user with ID {user_id}")


# async def main():
#     user_ids = await fetch_users()
#     tasks = [update_avatar(user_id) for user_id in user_ids]
#     await asyncio.gather(*tasks)


# asyncio.run(main())
