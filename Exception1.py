# Few Exceptions :
#print(b)

#'2' + 2

# # try & except
# num = 10
# # try:
# print(num / 0)

# except ZeroDivisionError:
#     print("Can't divide by Zero")

# try except & else
# num = 10
# try:
#     print(num / 0)
# except ZeroDivisionError:
#     print("Can't divide by Zero")
# else:
#     print("operation succeeded")

# try with multiple Except :
# num = 10
# try:
#     print(num / 'a')
# except ValueError:
#     print("ValueError Occurred")
# except ZeroDivisionError:
#     print("Can't divide by Zero")
# except TypeError:
#     print("TypeError Occurred")

# except with no specific exception
#print(len())
# try:
#     print(len())
# except:
#     print("All exceptions are handled")

# except with multiple exceptions
# try:
#     print(10 / 0)
# except Exception as ex:
#     print("Exception occurred from above exception list", ex)

# except having exception hierarchy
# num = 10
# try:
#     print(num / 0)
# except TypeError:
#     print("TypeError Occurred")
# except Exception:
#     print("Exception Occurred")

# try finally
# try:
#     print(10 / 0)
# finally:
#      print("finally blocked is executed")
#  # exception is raised after finally statement


# #try except finally
# try:
#     print(10 / 0)
# except ZeroDivisionError:
#     print("Exception Handled")
# finally:
#     print("finally blocked is executed")

# # try except else finally
# try:
#     num = 10/0
# except ZeroDivisionError:
#     print("Exception Handled")
# else:
#     print("Executing else block")
# finally:
#     print("finally blocked is executed")

# Nested try finally
# try:
#     print(10 / 0)
#     try:
#         print(10/0)
#     except:
#         print("HEllo")
#     finally:
#         print("Finally block")
# except:
#     print("exception handled by outer block")
# else : print("Bye")
