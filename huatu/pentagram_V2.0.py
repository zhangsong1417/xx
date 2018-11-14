"""
作者：
功能：五角星绘制
版本：2.0
日期：10/18/2018
新增功能：加入循环操作绘制重复不同大小的图形
"""
import turtle


def draw_pentagram(size):
    # 绘制五角星
    # 计数器
    count = 1
    while count <= 5:
        turtle.forward(size)
        turtle.right(144)
        # count = count + 1
        count += 1


def main():
    """
    主函数
    """
    turtle.penup()
    turtle.backward(200)
    turtle.pendown()
    turtle.pensize(2)
    turtle.pencolor("blue")
    size = 100
    while size <= 150:
        # 调用函数
        draw_pentagram(size)
        # size = size + 10
        size += 10

    turtle.exitonclick()
    # turtle.forward(100)
    # turtle.right(144)
    # turtle.forward(100)
    # turtle.right(144)
    # turtle.forward(100)
    # turtle.right(144)
    # turtle.forward(100)
    # turtle.right(144)
    # turtle.forward(100)
    # turtle.right(144)
    # turtle.exitonclick()


if __name__ == '__main__':
    main()
