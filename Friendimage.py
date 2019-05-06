__author__ = 'Administrator'
from PIL import Image
import os,math,shutil

#在图片路径下新建与图片名一致的文件夹
def image_dir(image_path):
    #去掉图片路径，获取图片名及格式
    base_name = os.path.basename(image_path)
    #获取图片路径，去掉图片名及格式
    dir_path = os.path.dirname(image_path)
    #获取图片名及格式元组
    splitext = os.path.splitext(base_name)
    #获取图片名
    dirname = splitext[0]
    #以图片名新建文件夹
    folder = os.path.join(dir_path,dirname )
    #判断是否存在该文件夹，有则删除再新建
    if os.path.exists(folder):
        shutil.rmtree(folder)
        os.mkdir(folder)
    else:
        os.mkdir(folder)
    return folder

#在原图片上合成新图片
def fill_image(image):
    #获取图片宽、高
    width,height = image.size
    #取原图片宽、高更长者作为新图片的边长
    new_img_length = width if width > height else height
    #新建白色背景图
    newImg = Image.new(image.mode,(new_img_length,new_img_length),color='white')
    #将原图“黏贴”在背景图上并居中显示，合成新图片
    if width > height:
        newImg.paste(image,(0,int((new_img_length-height)/2)))
    else:
        newImg.paste(image,(int((new_img_length-width)/2),0))

    return newImg

#剪裁新图片，image为需要裁剪的图片，num为需要裁剪的数量
def cut_image(image,num):
    # x为裁剪数量的平方根，比如朋友圈发9张图，x为3
    x = int(math.sqrt(num))
    #裁剪成小图的边长
    item_width = int(image.width/x)
    #裁剪时的位置坐标
    box_list = []
    for i in range(0,x):
        for j in range(0,x):
            box = (j*item_width, i*item_width, (j+1)*item_width,(i+1)*item_width)
            box_list.append(box)
    #将裁剪后的图放入列表
    image_list = [image.crop(box) for box in box_list]
    return image_list

#保存图片到同路径下的同名文件夹下
def save_image(image_list,folder_path):
    index = 1
    for image in image_list:
        image.save("%s/%s.png" %(str(folder_path),str(index)), 'PNG')
        index += 1

#检查图片是否裁剪成功
def check_image(image_list,folder_path,num):

    if os.path.exists(folder_path) and len(image_list) == num:
        res ='success'
        print(res)
        return res
    else:
        res = 'fail'
        print(res)
        return res

#输入图片路径及需要裁剪的数量，裁剪后并检查是否成功
def success_image(image_path,num):
    folder_path = image_dir(image_path)
    image = Image.open(image_path)
    new_image = fill_image(image)
    image_list = cut_image(new_image,num)
    save_image(image_list,folder_path)
    res = check_image(image_list,folder_path,num)
    return res

#实例一个
if __name__ == '__main__':
    success_image("C:/Users/Administrator/Desktop/图片/1.jpg",4)