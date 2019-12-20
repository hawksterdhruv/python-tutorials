#Iterators
# class PowTwo:
#     """Class to implement an iterator
#     of powers of two"""
#
#     def __init__(self, max = 0):
#         self.max = max
#
#     def __iter__(self):
#         self.n = 0
#         return self
#
#     def __next__(self):
#         if self.n <= self.max:
#             result = 2 ** self.n
#             self.n += 1
#             return result
#         else:
#             raise StopIteration
#
# # list(1, 2,3 4,5)
# # # a = PowTwo(4)
# # # i = iter(a)
# # # print(next(i))
# # # print(next(i))
# # # print(next(i))
# # # print(next(i))
# # # print(next(i))
# # # # should throw error
# # # # print(next(i))
#
#
# for x in PowTwo(8):
#     print(x)



# def PowTwo(n = 0):
#     print('This is printed first{}'.format(n))
#     # Generator function contains yield statements
#     yield 2**n
#
#     n += 1
#     print('This is printed second{}'.format(n))
#     yield 2**n
#
#     n += 1
#     print('This is printed at last{}'.format(n))
#     yield 2**n


# a = PowTwo(4)
# print(a)
# print(a)
# print(a)
# # #print(next(a))
# for i in PowTwo(4):
#     print(i)


# def fibonacci(n):
#     """ A generator for creating the Fibonacci numbers """
#     a, b, counter = 0, 1, 0
#     while True:
#         if (counter > n):
#             return
#         yield a
#         a, b = b, a + b
#         counter += 1
# f = fibonacci(1000)
# for x in f:
#     print(x, " ", end="")



# send/coroutines
# def gen():
#     i = 1
#     while True:
#         i *= 1
#         # yield i
#         # print(i)
#         x = yield i
#         print(x)
#
#
# m = gen()
# next(m)
# m.send(4)



