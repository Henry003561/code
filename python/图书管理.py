import pymysql
import tkinter as tk
from tkinter import messagebox
import email
import random

class StartPage:
    def __init__(self, parent_windows):
        parent_windows.destroy()
        self.windows = tk.Tk()
        self.windows.title("图书管理系统")
    
    def signin(self):
        signin = Sigin(self.windows)
        signin.signin_windows()

    def signup(self):
        signup = Signup(self.windows)
        signup.signup_windows()
    def pages(self):
        self.signin_button = tk.Button(self.windows, text="登录按钮", command=self.signin)
        self.signin_button.pack()
        self.sighup_button = tk.Button(self.windows, text='注册', command=self.signup)
        self.sighup_button.pack()
        self.windows.mainloop()

class Sigin:
    def __init__(self, parent_windows):
        parent_windows.destroy()
        self.windows = tk.Tk()
        self.windows.title("图书管理系统")
        self.conn = pymysql.connect(user='root', host='localhost', port=3306, database='Bms', charset='utf8', password='hwh003561')
        self.cursor = self.conn.cursor()
    
    def signin(self):
        try:
            self.cursor.execute('select * from users where username="%s",password="%s"'%(self.username, self.password))
            self.conn.commit()
            self.a = self.cursor.fetchall()
            messagebox.showinfo(title="登录操作", message='登录成功')
            #TODO 进入下一个窗口

        except Exception as e:
            messagebox.showerror(title="登录操作",message="登录失败")
        
        
    def exit(self):
        startpage = StartPage(self.windows)
        startpage.pages()

    def signin_windows(self):
        self.username_label = tk.Label(self.windows,text='用户名')
        self.username_label.pack()
        self.username_entry = tk.Entry(self.windows)
        self.username_entry.pack()
        self.username = self.username_entry.get()
        self.password_label = tk.Label(self.windows,text="密码")
        self.password_label.pack()
        self.password_entry = tk.Entry(self.windows, show="*")
        self.password_entry.pack()
        self.password = self.password_entry.get()
        self.sigin_button = tk.Button(self.windows, text="登录", command=self.signin)
        self.sigin_button.pack()
        self.exit_button = tk.Button(self.windows, text='退出', command=self.exit)
        self.exit_button.pack()
        self.windows.mainloop()

class Signup:
    def __init__(self, parent_windows):
        parent_windows.destroy()
        self.windows = tk.Tk()
        self.windows.title("图书管理系统")
        self.conn = pymysql.connect(user='root', port=3306, host='localhost', password='hwh003561', database='Bms', charset='utf8')
        self.cursor = self.conn.cursor()
    #TODO 邮件发送功能
    def email_send(self):
        j = 6
        code_list = random.sample(range(0,9), j)
        for code in code_list:
            self.code_check = code
        
        self.Captcha_code()
    
    def Captcha_code(self):
        self.code_label = tk.Label(self.windows, text="验证码")
        self.code_label.pack()
        self.code_entry = tk.Entry(self.windows)
        self.code_entry.pack()
        self.code = self.code_entry.get()
        def code_jugement():
            pass
        self.yes_button = tk.Button(self.windows, text='确认', command=code_jugement)
    def signup(self):
        try:
            self.cursor.execute('insert into Bms ("%s", "%s", "%s")'%(self.username, self.password, self.email))
            self.conn.commit()
        except Exception as e:
            pass
    
    def exit(self):
        startpage = StartPage(self.windows)
        startpage.pages()

    def signup_windows(self):
        self.username_label = tk.Label(self.windows, text="用户名")
        self.username_label.pack()
        self.username_entry = tk.Entry(self.windows)
        self.username_entry.pack()
        self.uername = self.username_entry.get()
        self.password_label = tk.Label(self.windows, text="密码")
        self.password_label.pack()
        self.password_entry = tk.Entry(self.windows, show="*")
        self.password_entry.pack()
        self.password = self.password_entry.get()
        self.email_label = tk.Label(self.windows, text="邮箱地址")
        self.email_label.pack()
        self.email_entry = tk.Entry(self.windows)
        self.email_entry.pack()
        self.email = self.email_entry.get()
        self.signup_button = tk.Button(self.windows, text="注册", command=self)
        self.signup_button.pack()
        self.exit_button = tk.Button(self.windows, text="退出注册", command=self.exit)

class Bms:
    def __init__(self, parent_windows):
        parent_windows.destroy()
        self.conn = pymysql.connect(user='root', port=3306, host='localhost', password='hwh003561', database='Bms', charset='utf8')
        self.cursor = self.conn.cursor()
        
if __name__ == '__main__':
    windows = tk.Tk()
    startpage = StartPage(windows)
    startpage.pages()
