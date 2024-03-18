import asyncio

# example of async
# async def hello_world():
#     print("Started 🌍")
#     await asyncio.sleep(3)  # sleep | async func | you have to await until its completed
#     print("Hello, Sanlam 🌍")


# asyncio.run(hello_world())


# task 1: do a countdown
# async def countdown():
#     print("3")
#     await asyncio.sleep(1)
#     print("2")
#     await asyncio.sleep(1)
#     print("1")
#     await asyncio.sleep(1)
#     print("Happy New Year! 🥳")

# asyncio.run(countdown())

# task 2: DRY - do a countdown
# async def countdown():
#     for i in range(3, 0, -1):
#         print(i)
#         await asyncio.sleep(1)
#     print("Happy New Year! 🥳")

# asyncio.run(countdown())


# task 3: without any loop
# async def countdown(num):
#     if num > 0:
#         print(num)
#         await asyncio.sleep(1)  # you can only use await on asyn funcs
#         await countdown(num - 1)
#     else:
#         print("Happy New Year! 🥳")


# asyncio.run(countdown(3))


# def add(x):
#     return x + 1


# def sum(a, b):
#     c = add(a) + add(b)
#     return c


# print(sum(3, 5))

# growing stack infinitely
# def dbl(x):
#     y = x * 2
#     dbl(3)
# dbl(10)


# async def background_task():
#     print("Start background task")
#     await asyncio.sleep(3)


# async def main():
#     # request to event loop to schedule
#     task = asyncio.create_task(background_task())
#     # waiting for the background_task
#     print("Main function says - Hi")
#     print("Main function says - Hi")
#     print("Main function says - Hi")
#     print("Main function says - Hi")


# asyncio.run(main())


# eggs cooked example
async def cooking_eggs():
    print("Eggs cooking")
    await asyncio.sleep(3)
    print("Eggs cooked")
    return f"Data - Eggs"


async def make_coffee():
    print("Coffee brewing")
    await asyncio.sleep(2)
    print("Coffee done")
    return f"Data - Coffee"


async def make_cereal():
    print("Making cereal bowl")
    await asyncio.sleep(5)
    print("Cereal done")
    return f"Data - Cereal"


# Async func with event loop
# async def main():
#     await cooking_eggs()
#     await make_coffee()
#     print("Bread Toast 1")
#     print("Bread Toast 2")
#     print("Bread Toast 3")
#     print("Bread Toast 4")
#     await task1


# Async func with event loop
async def main():
    # all async funcs returns a co-coroutine
    # you can do it this way as well:
    all_co_routines = [cooking_eggs(), make_coffee(), make_cereal()]
    # task1 = asyncio.create_task(cooking_eggs()) # schedule things in event loop
    # task2 = asyncio.create_task(make_coffee())
    # task3 = asyncio.create_task(make_cereal())
    # all_tasks = [task1, task2, task3]
    print("Bread Toast 1")
    print("Bread Toast 2")
    print("Bread Toast 3")
    print("Bread Toast 4")
    await asyncio.sleep(6)
    # await task2
    # wait is to complete tasks but not the best when you dont know how long each task is, so you use gather
    # if not scheduled (create task) then it starts here
    data = await asyncio.gather(
        *all_co_routines
    )  # dtype - not a dict, a set of tasks to complete all, wait till longest one is completed
    print(data)  # order of tasks


asyncio.run(main())
