import tkinter
import random
import quci
import win32com.client
import time
import threading

class zhuce(tkinter.Tk):

    def __init__(self):
        super().__init__()
        self.title("跳跳诗词学习系统")
        self.geometry("+300+50")
        self.resizable(0, 0)
        self.denglu()

    def ss(self, t):
        x = random.randint(1, 255)
        y = random.randint(1, 255)
        s = color_list[x]
        s1 = color_list[y]
        self.labn[t].config(bg=s, fg=s1)
    
    def sound(self):
        t=self.listt()
        t=''.join(t)
        speaker = win32com.client.Dispatch("SAPI.SpVoice")
        speaker.Speak(t)
    
    def okk(self):
        threading.Thread(target=self.okkk).start()
        time.sleep(.1)
        threading.Thread(target=self.sound).start()


    def listt(self):
        list_22 = []
        con = self.ent1.get()
        if len(con) == 3:
            a = con[0]
            b = con[1]
            c = con[2]
            for i in range(iss):
                if a == list1[i] and b == list1[i+1] and c == list1[i+2]:
                    x = i+3
                    break
            while list1[x] != list1[0] and list1[x] != list1[1]:
                list_22 += list1[x]
                x += 1
        else:
            a = con[0]
            b = con[1]
            for i in range(iss):
                if a == list1[i] and b == list1[i+1]:
                    x = i+2
                    break
            while list1[x] != str(0) and list1[x] != str(1) and list1[x] != str(2) and list1[x] != str(3) and list1[x] != str(4) and list1[x] != str(5) and list1[x] != str(6) and list1[x] != str(7) and list1[x] != str(8) and list1[x] != str(9):
                list_22 += list1[x]
                x += 1
        return list_22

    def okkk(self):
        for widget in self.frm2.winfo_children():
            widget.destroy()
        for widget in self.frm3.winfo_children():
            widget.destroy()
        self.frm1.grid_forget()
        self.frm2.grid_forget()
        self.frm3.grid_forget()
        x = random.randint(1, 255)
        y = random.randint(1, 255)
        s = color_list[x]
        s1 = color_list[y]
        self.frm1.config(bg=s)
        self.lab1.config(bg=s, fg=s1)
        self.ent1.config(bg=s, fg=s1)
        self.lab2.config(bg=s, fg=s1)
        self.but1.config(bg=s, fg=s1)
        w = 0
        o = 0
        l = 0
        y=0
        self.labn = {}
        list_22 = []
        self.frm1.grid(row=0,column=0)
        self.frm2.grid(row=1,column=0)  
        list_22=self.listt()
        for list_221 in list_22:
            if list_221 == '\t' or list_221 == '。' or list_221 == '，' or list_221 == '？'or list_221 == '！':
                pass
            elif list_221 == '\n':
                y+=1
                if y==7:
                    w=0
                    o=0
                else:
                    w += 1
                    o = 0            
            else:
                if y>=7:
                    self.frm1.grid(row=0,column=0,columnspan=2)
                    self.frm3.grid(row=1,column=1)
                    self.labn[l] = tkinter.Button(self.frm3, text=list_221,
                                                font=('微软雅黑', '24'), relief='groove', command=lambda t=l: self.ss(t))
                    self.labn[l].grid(row=w, column=o, padx=3, pady=2)
                    o += 1
                    l += 1
                else:                    
                    self.labn[l] = tkinter.Button(self.frm2, text=list_221,
                                                font=('微软雅黑', '24'), relief='groove', command=lambda t=l: self.ss(t))
                    self.labn[l].grid(row=w, column=o, padx=3, pady=2)
                    o += 1
                    l += 1          


    def denglu(self):
        addr = tkinter.StringVar(value='0')
        x = random.randint(1, 255)
        y = random.randint(1, 255)
        s = color_list[x]
        s1 = color_list[y]
        self.frm1 = tkinter.Frame(self, bg=s)
        self.frm1.grid(row=0,column=0,columnspan=2)
        self.frm2 = tkinter.Frame(self)
        self.frm3 = tkinter.Frame(self)
        self.lab1 = tkinter.Label(self.frm1, text='大家好!我是谢修一，我想学第：',
                             bg=s, fg=s1, font=('微软雅黑', '28'), relief='groove')
        self.lab1.grid(row=0, column=0)
        self.ent1 = tkinter.Entry(self.frm1, font=('微软雅黑', '28'), width='4', bg=s, fg=s1,
                                  insertbackground='red', highlightbackground='red', textvariable=addr)
        self.ent1.grid(row=0, column=1)
        self.lab2 = tkinter.Label(self.frm1, text='首诗，我要加油哦!', bg=s,
                             fg=s1, font=('微软雅黑', '28'), relief='groove')
        self.lab2.grid(row=0, column=2)
        self.but1 = tkinter.Button(self.frm1, text='点我去读诗吧!', bg=s, fg=s1, font=(
            '微软雅黑', '28'), command=lambda: self.okk())
        self.but1.grid(row=1, column=0, pady=1, columnspan=3)

if __name__ == '__main__':
    list1=quci.quci()
    iss=len(list1)
    color_list=quci.colors()
    app = zhuce() 
    app.mainloop()           
