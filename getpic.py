import urllib
import urllib.request
import re


# 打开网页下载器
def open_html(url):
    require = urllib.request.Request(url)
    reponse = urllib.request.urlopen(require)
    html = reponse.read()
    return html


# 下载图片
def load_image(html):
    regx = 'http://[\S]*jpg'
    pattern = re.compile(regx)
    get_image = re.findall(pattern, repr(html))

    num = 1
    for img in get_image:
        photo = open_html(img)

        with open(r'D:\Photo\%s.jpg' % num, 'wb') as f:
            print('开始下载图片')
            f.write(photo)
            print('正在下载第%s张图片' % num)
            f.close()
        num = num + 1
    if num > 1:
        print('下载成功！！！')
    else:
        print('下载失败！！！')


url = 'http://www.qiqipu.com/'
html = open_html(url)
load_image(html)
