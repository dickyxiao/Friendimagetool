__author__ = 'Administrator'
import tkinter as tk
from tkinter import filedialog,messagebox
import Friendimage,os

#定义GUI界面，名字及大小和在桌面位置
window = tk.Tk()
window.title('逛逛小工具')
window.geometry('550x400+460+100')

#选择图片
def upload_file():
    selectfile = tk.filedialog.askopenfilename(title = '请选择您要剪裁的图片',
                                               filetype = [('image','*.jpg;*jepg;*png;*bmp')])
    # 清空文本框数据
    text1.delete(0,'end')
    # 图片路径显示在文本框中
    text1.insert(0,selectfile)

#获取文本框中图片路径，并将它变成字符串形式，方便传值
def print_file():
    a = '{}'.format(text1.get())
    return a

#销毁窗口界面
def closewindow():
    window.destroy()

# 利用StringVar接收用户输入
var = tk.StringVar()
var.set(None)
#选择照片张数提示
def print_selection():
    label2.config(text = '您选择了截成' + var.get() + '张')

# 处理过程
def manage():
    path = print_file()
    if os.path.exists(path) and var.get() in ['4','9']:
        result = Friendimage.success_image(path,int(var.get()))
        if result == 'success':
            tk.messagebox.showinfo('',"裁剪图片成功啦，快去查看吧")
        else:
            tk.messagebox.showinfo('',"不好意思，裁剪图片失败")
    elif path == '':
        tk.messagebox.showinfo('',"请选择您需要裁剪的图片")
    elif os.path.exists(path) == False:
        tk.messagebox.showinfo('',"图片路径不存在")
    elif os.path.exists(path) and var.get() == 'None':
        tk.messagebox.showinfo('',"请您选择需要裁剪图片的张数")

#界面上的控件、元素
# 文字提示
label1 = tk.Label(window,text = '请选择图片:',font = ('',10))
# 图片路径的文本框
text1 = tk.Entry(window,bg = 'white',width = 45)
# 选择图片的按钮
browse_button = tk.Button(window,text='浏览',width = 8,command=upload_file)
label2 = tk.Label(window,text = '您想截成几张图呢：')
# 单选框，默认不选
radiobutton_4 = tk.Radiobutton(window, text = '4', variable = var, value = '4',command = print_selection )
radiobutton_9 = tk.Radiobutton(window, text = '9', variable = var, value = '9',command = print_selection)
# 处理及退出按钮
manage_button = tk.Button(window,text='处理',width = 8,command=manage)
quit_button = tk.Button(window,text='退出',width = 8,command=closewindow)

# 界面上的布局，pack()一种布局方式，它会按照上下左右的方式排列
label1.pack()
text1.pack()
browse_button.pack()
label2.pack()
radiobutton_4.pack()
radiobutton_9.pack()
manage_button.pack()
quit_button.pack()
# place（）一种布局方式，给精确的坐标来定位
label1.place(x = 30,y = 100)
text1.place(x = 110,y = 100)
browse_button.place(x = 450,y = 96)

label2.place(x = 120,y = 130)
radiobutton_4.place(x = 240,y = 130)
radiobutton_9.place(x = 310,y = 130)

manage_button.place(x = 190,y = 170)
quit_button.place(x = 290,y = 170)

# 进入消息循环
window.mainloop()