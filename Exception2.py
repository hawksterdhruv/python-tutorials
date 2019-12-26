#Raising exceptions
#raise NameError

#Handling raised Exception
# try:
#     raise ZeroDivisionError("can't divide by zero")
# except ZeroDivisionError as ex :
#     print("Raised Exception is Handled", ex)


# User Defined Exceptions
#Example 1:
# class UserdefExcept(TypeError):
#     pass

# try:
#    raise UserdefExcept
# # except UserdefExcept:
# #     print("I handled used defined exception")
# except TypeError :
#     print("Handled by parent class")

#Example 2:
# class UserdefinedError(ZeroDivisionError):
#     def __init__(self, arg):
#         self.arg = arg
#
# try:
#      raise UserdefinedError("Raised exception")
# except UserdefinedError as ex:
#     print("Handled :", ex.arg)



