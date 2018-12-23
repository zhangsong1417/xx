"""
作者：
功能：利用递归函数绘制分形树
版本：1.0
日期：10/19/2018
"""
import turtle


def draw_branch(branch_length):

    """
    绘制分形树
    """
    if  branch_length >= 5:
        if branch_length < 40:
            turtle.color('red')
        else:
            turtle.color('green')
        # 绘制右侧树枝
        turtle.forward(branch_length)
        print("向前", branch_length)
        turtle.right(30)
        print('右转30度')
        draw_branch(branch_length - 15)

        # 绘制左侧树枝
        turtle.left(60)
        print('左转60度')
        draw_branch(branch_length - 15)

        if branch_length < 40:
            turtle.color('red')

        else:
            turtle.color('green')

        # 返回之前的树枝
        turtle.right(30)
        print('右转30度')
        turtle.backward(branch_length)
        print('返回', branch_length)


def main():
    """
    主函数
    """
    turtle.color('green')
    turtle.left(90)
    turtle.penup()
    turtle.speed(10)
    turtle.backward(150)
    turtle.pendown()

    draw_branch(100)
    # 画一个框
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.penup()
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.pendown()
    turtle.write('我爱你', font=("宋体", 24))
    turtle.hideturtle()

    turtle.exitonclick()


if __name__ == '__main__':
    main()





