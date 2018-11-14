import random
times = 5
secret = random.randint(1,10)
print('---------------------工作室------------------')
guess = 0
print("不妨猜一下我现在心里想的是哪个数字：",end="")
while (guess != secret) and (times > 0):
    temp = input()
    while not temp.isdigit():
        temp = input("抱歉，您的输入有误，请输入一个整数：")
    guess = int(temp)
    times = times - 1#用户每输入一次，可用机会就-1
    if guess == secret:
        print("我曹，你是小甲鱼心里的蛔虫吗？！")
        print("哼，猜中了也没有奖励！")
    else:
        if guess > secret:
            print("嘿，哥，大了大了~~~~~")
        else:
            print("嘿，小了，小了---")
        if times > 0:
            print("再试一次吧;",end="")
        else:
            print("机会用光咯")
print("游戏结束，不玩啦")
