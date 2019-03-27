from time import ctime, sleep
# 说


def talk():
    print("Start talk %r" % ctime())
    sleep(2)


# 写
def write():
    print("Start Write %r" % ctime())
    sleep(3)


if __name__ == "__main__":
    talk()
    write()
    print("All end %r" % ctime())
