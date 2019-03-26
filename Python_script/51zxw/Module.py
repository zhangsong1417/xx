#import time
import random
from time import sleep
from student import Student 


#print(time.ctime())
num = random.randint(1, 10)
print(num)
sleep(5)
print("sleep over！")

stu1 = Student('jack', 'Beijing')
stu1.talk()
stu2 = Student('Mary', 'Shanghai')
stu2.talk()
