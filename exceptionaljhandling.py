# try:
#     a=10/0
# except Exception as e:
#     print("Exception",e)
# except ValueError as e:
#     print("value error",e)
# except ZeroDivisionError as e:
#     print("exception occured",e)
# else:
#     print(f"Resut{a}")
# finally:
#     print("finally")


# check age

# def checkage(x):
#     if(x<18):
#         raise ValueError("Age should be >18")
#     else:
#         print("done")
# try:
#     checkage(17)
# except ValueError as e:
#     print("error occured",e)
# finally:
#     print("finally")



# userdefined exception

# class NotEligibeForVote(Exception):
#     pass

# def checkage(x):
#     if(x<18):
#         raise NotEligibeForVote("Age should be >18")
#     else:
#         print("done")
# try:
#     checkage(17)
# except NotEligibeForVote as e:
#     print("error occured",e)
# finally:
#     print("finally")

# try:
#     # risky code that might raise multiple exceptions
#     x = int(input("Enter a number: "))
#     result = 10 / x
#     my_list = [1, 2]
#     print(my_list[5])
# except ValueError:
#     print("Invalid input. Please enter a number.")
# except ZeroDivisionError:
#     print("Can't divide by zero!")
# except IndexError:
#     print("List index is out of range.")


# try:
#     x = int(input("Enter a number: "))
#     result = 10 / x
#     my_list = [1, 2]
#     print(my_list[5])
# except (ValueError, ZeroDivisionError, IndexError) as e:
#     print("An error occurred:", e)


# File Handling Exception

# file=("test.txt"'w')
import os
data="Writtn Done"
try:
    if os.path.exists:
       with open("test3.txt",'r')as file:
          content =file.read()
          print(content)
       with open ("test.txt",'w')as filewrite:
          filewrite.write(data)
       with open("test.txt",'r')as file:
          con =file.read()
          print(con)
except FileNotFoundError as e:
    print(e,"error")