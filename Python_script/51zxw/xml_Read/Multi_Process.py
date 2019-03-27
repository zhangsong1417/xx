from time import ctime, sleep
import multiprocessing


# 定义说和写的方法
def talk(content, loop):
    for i in range(loop):
        print("Start talk:%s %s" % (content, ctime()))
        sleep(3)


def write(content, loop):
    for i in range(loop):
        print("Start write:%s %s" % (content, ctime()))
        sleep(5)


# 定义两个进程
process = []
p1 = multiprocessing.Process(target=talk, args=('Hello 51zxw!', 2))
process.append(p1)

p2 = multiprocessing.Process(target=write, args=('Life is short,You need Python!', 2))
process.append(p2)

# 执行多线程
if __name__ == '__main__':

    for p in process:
        p.start()
    for p in process:
        p.join()
    print("All process is run! %s" % ctime())
