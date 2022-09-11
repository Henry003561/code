import pymysql
import tkinter as tk
from tkinter import messagebox
from email.mime.text import MIMEText
import smtplib
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
            #TODO 进入Bms
            bms = Bms(self.windows)
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
    # 邮件发送功能
    def get_user(self):
        if self.username == '' or self.password == '':
            messagebox.showwarning(title='登录操作', message='请输入用户名或密码')
        else:
            if self.password == self.check_password:
                self.email_send()
            else:
                messagebox.showwarning(title='登录操作', message='再次确认密码')
        
    def email_send(self):
        mail_host = 'smtp.163.com'
        mail_user = 'hgpfj016'
        mail_pass = 'JBLBFTYFKXJDOXOD'
        sender = 'hgpfj016@163.com'
        receivers = [self.email]
        j = 6
        code_list = random.sample(range(0,9), j)
        self.code_check = ''
        for code in code_list:
            self.code_check = self.code_check.join(str(code))
        message = MIMEText('验证码：'+self.code_check, 'plain', 'utf-8')
        message['Subject'] = 'title'
        message['From'] = sender
        message['To'] = receivers[0]
        try:
            stmpObj = smtplib.SMTP()
            stmpObj.connect(mail_host, 465)
            stmpObj.login(mail_user, mail_pass)
            stmpObj.sendmail(sender, receivers, message.as_string())
            stmpObj.quit()
            self.Captcha_code()
        except smtplib.SMTPException as e:
            print(e)
            messagebox.showwarning(title='邮件操作', message='请检查你的邮箱地址')
        
    
    def Captcha_code(self):
        self.windows.destroy()
        self.captcha = tk.Tk()
        self.captcha.title("图书管理系统")
        self.code_label = tk.Label(self.captcha, text="验证码")
        self.code_label.pack()
        self.code_entry = tk.Entry(self.captcha)
        self.code_entry.pack()
        self.code = self.code_entry.get()
        #验证码判断功能
        def code_jugement():
            if self.code ==  self.code_check:
                self.signup()
            else:
                messagebox.showwarning(title='验证码', message='验证码错误')
        self.yes_button = tk.Button(self.captcha, text='确认', command=code_jugement)
    def signup(self):
        try:
            self.cursor.execute('insert into Bms ("%s", "%s", "%s")'%(self.username, self.password, self.email))
            self.conn.commit()
            #TODO 进入Bms
            bms = Bms(self.captcha)

        except Exception as e:
            self.conn.rollback()
    
    def exit(self):
        startpage = StartPage(self.windows)
        startpage.pages()

    def signup_windows(self):
        self.username_label = tk.Label(self.windows, text="用户名")
        self.username_label.pack()
        self.username_entry = tk.Entry(self.windows)
        self.username_entry.pack()
        self.username = self.username_entry.get()
        self.password_label = tk.Label(self.windows, text="密码")
        self.password_label.pack()
        self.password_entry = tk.Entry(self.windows, show="*")
        self.password_entry.pack()
        self.password = self.password_entry.get()
        self.check_password_label = tk.Label(self.windows, text='确认密码')
        self.check_password_label.pack()
        self.check_password_entry = tk.Entry(self.windows, show='*')
        self.check_password_entry.pack()
        self.check_password = self.check_password_entry.get()
        self.email_label = tk.Label(self.windows, text="邮箱地址")
        self.email_label.pack()
        self.email_entry = tk.Entry(self.windows)
        self.email_entry.pack()
        self.email = self.email_entry.get()
        self.signup_button = tk.Button(self.windows, text="注册", command=self.get_user)
        self.signup_button.pack()
        self.exit_button = tk.Button(self.windows, text="退出", command=self.exit)
        self.exit_button.pack()

class Bms:
    def __init__(self, parent_windows):
        parent_windows.destroy()
        self.conn = pymysql.connect(user='root', port=3306, host='localhost', password='hwh003561', database='Bms', charset='utf8')
        self.cursor = self.conn.cursor()
    


class Book_insert:
    def __init__(self, parent_windows):
        parent_windows.destroy()
        self.conn = pymysql.connect(user='root', port=3306, host='localhost', password='hwh003561', database='Bms', charset='utf8')
        self.cursor = self.conn.cursor()
        
if __name__ == '__main__':
    windows = tk.Tk()
    startpage = StartPage(windows)
    startpage.pages()
