import tkinter
import random
import funtion
import time
import threading


def tkkd():
    t = random.randint(1, 256)
    u = random.randint(1, 59)
    x = funtion.colors()[t]
    y = funtion.zhufuh()[u]
    f = funtion.colors()[random.randint(1, 256)]
    t = str(random.randint(1, 1700))
    u = str(random.randint(1, 1000))
    cct = '+'+t+'+'+u
    win1 = tkinter.Tk()
    win1.geometry(cct)
    frm1 = tkinter.Frame(win1)
    frm1.pack()
    lab1 = tkinter.Label(frm1, bg=x, fg=f, text=y, height='2',
                         width='12', font=('微软雅黑', '28'))
    lab1.pack()
    win1.mainloop()


def thera():
    threads = []
    m = ent.get()
    lab.grid_forget()
    but.grid_forget()
    ent.grid_forget()
    lab2 = tkinter.Label(frm, bg='#80752c', text='开心就好！', height='1', relief='groove', fg='#f391a9',
                         width='16', font=('微软雅黑', '28'))
    lab2.pack()

    for i in range(int(m)):
        t = threading.Thread(target=tkkd)
        threads.append(t)
        time.sleep(.3)
        threads[i].start()


def main():
    global m
    global ent
    global frm
    global lab
    global but

    win = tkinter.Tk()
    addr = tkinter.StringVar(value='0')
    frm = tkinter.Frame(win, bg='#80752c')
    frm.pack()
    lab = tkinter.Label(frm, bg='#80752c', text='你想要几个祝福窗口：', height='1', relief='groove', fg='#f391a9',
                        width='16', font=('微软雅黑', '28'))
    lab.grid(row=0, column=0)
    ent = tkinter.Entry(frm, width='3', bg='#b2d235',
                        fg='#f391a9', font=('微软雅黑', '28'), textvariable=addr)
    ent.grid(row=0, column=1)
    but = tkinter.Button(frm, font=('微软雅黑', '14'), text='确认',
                         bg='#b2d235', fg='#f391a9', height='1', command=lambda: thera())
    but.grid(row=1, column=0, pady=1, columnspan=2)
    win.mainloop()


if __name__ == '__main__':
    main()
