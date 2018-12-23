
import os
from urllib.parse import urlencode
from



def get_images(json):
    data = json.get('data')
    print(data)
    if data:
        for item in data:
            image_list = item.get('image_list')
            title = item.get('title')
            if image_list:
                for image in image_list:
                    yield {
                        'image':image.get('url')
                        'title':title
                    }


#保存图片
def save_image(item):
    if not os.path.exits(item.get('title')):#如果目录不存在的话
        os.mkdir(item.get('title'))#创建文件夹


    local_image_url = item.get('image')#获取小图片
    new_image_url = local_image_url.replace('list','large')#大图片
    response = response.get('http:'get_url')#拼接图片地址
    if response.status_code == 200:

def main(offset):
    json = get_page(offset)
    for item in get_images(json):
        print(item)
        save_image(item)#保存图片


def if __name__ == '__main__':
    pool = pool()
    groups = ([x*20 for x in range(start,end)]) #列表生成式
    pool.map(main,groups)#整个队列就绪后，才会运行程序
    pool.