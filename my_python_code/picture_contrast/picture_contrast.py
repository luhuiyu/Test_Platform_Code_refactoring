# coding : utf-8

from PIL import Image,ImageDraw
from PIL import ImageChops
import numpy
def  make_thumbnail(image1,size=(720, 720), box = (0, 0, 720, 720)):#这个函数用于给需要对比的图片进行剪裁到合适的尺寸
    print(type(image1))
    image1.thumbnail(size)  #压缩
    region = image1.crop(box)  #剪裁
    return region

def img_difference(image1,image2):
    a = numpy.array(image1)
    b = numpy.array(image2)
    b = b - a
    if  (b != numpy.array([0])).any():
        return Image.fromarray(b.astype('uint8'))
    else:
        return None


def contrast(image1,image2):
    image1=make_thumbnail(image1).convert("L")
    image2=make_thumbnail(image2).convert("L")
   # diff = ImageChops.difference(image1, image2)
   # image1_1 = image1.convert("L")#转灰度图
   # image1_2 = image2.convert("L")  从效果上面看，转灰度图准确性没有提高
  #  diff = ImageChops.difference(image1, image1)
    diff=img_difference(image1,image2)
    if diff is None:
        return   {'image1':image1,'image2':image2,'result':True}
    else:
        print('不匹配')
        diff.show()
        raw_list=similarity_degree(diff)
       # draw = ImageDraw.Draw(image2)
       # for x in raw_list:
        #    draw.arc((x[1]-x[2], x[0]-x[2], x[1]+x[2], x[0]+x[2]), 0, -1)
        return {'image1':image1,'image2':image2,'diff':diff,"result":False}

def get_raw(image3):
    A = numpy.array(image3)
    c = numpy.zeros(3)
    height = 0
    ima_arr = []
    for x in A:  # 找出所有的不同的点 [高，宽]
        width = 0
        for y in x:
            if (y != numpy.array([0, 0, 0])).all():
                ima_arr.append([height, width])
            width = width + 1
        height = height + 1
    i = 0
    max_height = 0  # 间隔的高度
    all_a = 0
    all_b = 0
    index_i = 0
    k_start = 0
    k_end = 0
    raw_arr = []
    print(ima_arr)
    while i < len(ima_arr):
        index_i = index_i + 1
        a = ima_arr[i][0]
        b = ima_arr[i][1]
        all_a = all_a + a
        all_b = all_b + b
        if a - max_height == 1 :
            max_height = max_height + 1
            if k_start ==0:
                k_start = ima_arr[i][1]
        elif a - max_height > 5:

            k_end = ima_arr[i - 1][1]
            # print(k_end,k_start)
            max_height = a
            if k_start == 0:
                raw_arr.append([int(all_a / index_i), int(all_b / index_i), 30])
            elif int(k_end - k_start) < 10:
                    raw_arr.append([int(all_a  / index_i), int(all_b / index_i), 20])
            else:
                    raw_arr.append([int(all_a / index_i), int(all_b / index_i), int(k_end - k_start)] * 2)
            index_i = 0
            all_a, all_b = 0, 0
            k_start=0
        i = i + 1
   # raw_arr = raw_arr[1:]
        print(raw_arr)
    return  raw_arr
def similarity_degree(image1,image2):
    print(type(image1))
    print(type(image2))
    image1 = make_thumbnail(image1).convert("L")
    image2 = make_thumbnail(image2).convert("L")
    image3 = img_difference(image1, image2)
    if  None == image3:
        return 100
    print(image3.size)
    a=image3.size[0]
    b=image3.size[1]
    sua= int(a)*int(b)
    A = numpy.array(image3)
    c = numpy.zeros(3)
    height = 0
    ima_arr = []
    for x in A:  # 找出所有的不同的点 [高，宽]
        width = 0
        for y in x:
            if (y != numpy.array([0, 0, 0])).all():
                ima_arr.append([height, width])
            width = width + 1
        height = height + 1
    print(len(ima_arr),sua,(len(ima_arr)/sua)*100)
    return 100-(len(ima_arr)/sua)*100
if __name__ == '__main__':
    image1 = Image.open(r'F:\Test_Platform\my_python_code\myCase\appium_case\快快教瘦\test_case\img\登录页面.png')
    image2 = Image.open(r'F:\Test_Platform\my_python_code\myCase\appium_case\快快教瘦\test_case\img\登录页面YVF6R15A29000229.png')
    a=similarity_degree(image1,image2)
   # a["image2"].show()