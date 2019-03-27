# try:
#     fileName = input("please input fileName:")
#     open("%s.txt" %fileName)
# except FileNotFoundError:
#     print("%s.txt file not found " %fileName)

# try:
#     stu = 'jack'
#     print(stu)
# except NameError:
#     print("stu not define!")
# try:
#      #stu = 'jack'
#      print(stu)
# except BaseException:
#     print("stu not define!")
'''
try:
    print(stu)
except BaseException as msg:
    print(msg)
'''
'''
try:
    stu = 'jack'
    print(stu)
except BaseException as msg:
    print(msg)
else:
    print("stu is definded!")
'''
'''
try:
    #stu = 'jack'
    print(stu)
except BaseException as msg:
    print(msg)
else:
    print("stu is definded!")
finally:
    print("The end!")
'''


def division(x, y):
    if y == 0:
        raise ZeroDivisionError("Zero is not allow!")
    return x/y
try:
    division(8, 0)
except BaseException as msg:
    print(msg)
