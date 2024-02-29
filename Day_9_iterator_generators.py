# Iterables? __iter__ | Loop it many times Which can be looped: List
# Iterator? __next__ and __iter__ | Loop it one time | Save memory

# nums = [5, 10, 20]
# print(nums)
# print(dir(nums))

# # nums_iter = nums.__iter__() # converts to Iterator | Iterable --> Iterator
# nums_iter = iter(nums)  # <list_iterator onject at 0x000002AA75C79CF0>
# print(nums_iter)  # <list_iterator onject at 0x000002AA75C79CF0>
# print(dir(nums_iter))  # Iterator --> __next__ and __iter__
# # conclusionL ALL iterators are iterables | but not the other way

# print(next(nums_iter))
# print(next(nums_iter))
# print(next(nums_iter))
# # print(next(nums_iter)) <- this will give an error

# Task: Create an Iterator loop it with while loop -> Clue is use next() and Break at Error
# nums = [5, 10, 20]

# nums_iter = iter(nums)
# iterables doesnt know where you are in the loop but iterators do


# def main():
#     while True:
#         try:
#             item = next(nums_iter)
#             print(item)
#         except StopIteration:
#             break


# theres another way to do it
# nums_iter2 = iter([80, 90, 100])
# for num in nums_iter2:
#     print(num)


# range(0, 100_000_000, 1) | list with 100 million lots of memory <--- another way
# iterator remember one thing at a time | save memory
# __next__ and __iter_
# create your own iterator
# class MyRange:
#     def __init__(self, start, end):
#         self.current = start
#         self.end = end

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.current > self.end:
#             raise StopIteration
#         self.current += 1
#         return self.current - 1


# generator - clean more concise way to create iterators - powerful syntax
# def infinite_integers():
#     n = 0
#     while True:
#         yield n


# def fib(limit):
#     a = 0
#     b = 1
#     while a < limit:
#         yield a
#         a = b
#         c = a + b
#         b = c

# or can be done like this shorter way
# def fib(limit):
#     a, b = 0, 1
#     while a < limit:
#         yield a
#         a, b = b, a + b


# a b a+b
# 0 1 1
# 1 1 2
# 1 2 3
# 2 3 5

# first is 0 so return then pause (yield) until you call next again (iterator lazy)
# generator - yield is generator syntax, iterator

# if __name__ == "__main__":
#     main()
# for n in MyRange(1, 5):
#     print(n)
# integers = infinite_integers()  # iterator cause of next
# print(next(integers))
# print(next(integers))
# print(next(integers))

# fib - generator function
# for num in fib(10):
#     print(num)
# output -> 0 1 1 2 3 5 8 13 21 34 55
