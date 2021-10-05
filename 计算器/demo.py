import tkinter as tk
from tkinter import StringVar


class container(tk.Tk):

#! 窗口初始化
    def __init__(self):
        self.txt = ''
        self.txt1 = ''
        self.txt2 = ''
        self.fuhao = 0
        super().__init__()
        self.title('计算器')
        self.geometry('350x500+800+250')
        self.resizable(0, 0)
        self.xianshi()
        self.jiemian()

# !显示界面
    def xianshi(self):
        self.str = StringVar()
        frame1 = tk.Frame(self)
        frame1.pack()
        self.lat = tk.Label(frame1, textvariable=self.str,
                            bg='red', width='350', height='2', font=('微软雅黑', 28))
        self.lat.pack()

# !计算函数
    def jisu(self, m):

        if m == 'C':
            self.txt = ''
            self.txt1 = ''
            self.txt2 = ''
            self.str.set(0)
        elif(m in ['7', '8', '9', '1', '2', '3', '4', '5', '6', '00', '0', '.']):
            self.back = m
            self.txt = self.txt+m
            self.txt1 = self.txt1+m
            self.str.set(self.txt1)
        elif m == '+':
            self.fuhao = 1
            self.txt2 = self.txt
            self.txt = ''
            self.txt1 = self.txt1+m
            self.str.set(self.txt1)
        elif m == '-':
            self.fuhao = 2
            self.txt2 = self.txt
            self.txt = ''
            self.txt1 = self.txt1+m
            self.str.set(self.txt1)
        elif m == '*':
            self.fuhao = 3
            self.txt2 = self.txt
            self.txt = ''
            self.txt1 = self.txt1+m
            self.str.set(self.txt1)
        elif m == '/':
            self.fuhao = 4
            self.txt2 = self.txt
            self.txt = ''
            self.txt1 = self.txt1+m
            self.str.set(self.txt1)
        elif m == '<':
            if self.txt1 != '':
                s = list(self.txt1)
                s[-1] = ''
                self.txt1 = ''.join(s)
                self.str.set(self.txt1)
                s = list(self.txt)
                s[-1] = ''
                self.txt = ''.join(s)
        elif m == '%':
            self.fuhao = 5
            self.txt2 = self.txt
            self.txt = ''
            self.txt1 = self.txt1+m
            self.str.set(self.txt1)
        elif m == '=':
            if self.fuhao == 1:
                self.str.set(float(self.txt2)+float(self.txt))
                # self.txt2 = str(float(self.txt2)+float(self.txt))
                # self.txt = ''
            elif self.fuhao == 2:
                self.str.set(float(self.txt2)-float(self.txt))
                # self.txt2 =str( float(self.txt2)-float(self.txt))
                # self.txt = ''
            elif self.fuhao == 3:
                self.str.set(float(self.txt2)*float(self.txt))
                # self.txt2 = str(float(self.txt2)*float(self.txt))
                # self.txt = ''
            elif self.fuhao == 4:
                self.str.set(float(self.txt2)/float(self.txt))
                # self.txt2 = str(float(self.txt2)/float(self.txt))
                # self.txt = ''
            elif self.fuhao == 5:
                self.str.set(float(self.txt2) % float(self.txt))
                # self.txt2 = str(float(self.txt2)%float(self.txt))
                # self.txt = ''

#!生成按钮
    def but(self, f, a, x, i, y):
        but = tk.Button(f, text=a, width='3', font=(
            '微软雅黑', '18'), command=lambda: self.jisu(x))
        but.grid(row=i, column=y,padx=15,pady=10)

# ! 按钮界面
    def jiemian(self):

        lis = ['C', '%', '<', '/', '7', '8', '9', '*', '4', '5',
               '6', '-', '1', '2', '3', '+', '00', '0', '.', '=']
        frame1 = tk.Frame(self)
        frame1.pack()
        for n in range(5):
            for i in range(4):
                name = self.but(frame1, lis[i+n*4], lis[i+n*4], n, i)


if __name__ == '__main__':
    app = container()
    app.mainloop()
