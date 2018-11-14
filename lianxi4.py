"""
复制图片某个位置的图像到其它位置
img（x, y)分别为图片的(y, x)坐标
"""
import  numpy as np
import cv2

img = cv2.imread('BMW1.jpg', cv2.IMREAD_COLOR)
img2 = cv2.imread('BMW2.jpg', cv2.IMREAD_COLOR)
"""# 将图片55*55的地方用白色填充
img[55, 55] = [255, 255, 255]
px = img[55,55]
# 将图片（100-1500,100-150）的地方用户白色进行填充
img[100:150, 100:150] = [255, 255, 255]
"""
# 复制图片中的一部分
car = img[200:500, 347:647]
# 将复制的图片填充到其它位置
img[0:300, 0:300] = car
img[0:300,724:1024] = car
img[468:768,0:300] = car
img[468:768, 724:1024] = car
# 将复制的图片填充到其它图片
img2[0:300, 0:300] = car
img2[0:300,724:1024] = car
img2[468:768,0:300] = car
img2[468:768, 724:1024] = car
# 打印显示图片1
cv2.imshow('image', img)
# 显示2s时间后关闭
cv2.waitKey(2000)
# 将图片1写入新的文件中
cv2.imwrite("D:\\xx\\bm1.jpg", img)
# 打印显示图片2
cv2.imshow('image', img2)
# 将图片2写入新文件中
cv2.imwrite("D:\\xx\\bm2.jpg", img2)
# 一直显示图片
cv2.waitKey(0)
cv2.destroyAllWindows()
