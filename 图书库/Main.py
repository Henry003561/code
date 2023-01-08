import tkinter
from tkinter import ttk
import pymysql
import Login
import Logup

class Main:
    def __init__(self, dbuser, dbpassword, dbport, dbhost,database, windows):
        self.dbuser = dbuser
        self.dbpassword = dbpassword
        self.dbport = dbport
        self.dbhost = dbhost
        self.database = database
        # 删除上一个窗口
        windows.destroy()
        # 搭建数据库的数据链路
        self.conn = pymysql.connect(user=dbuser, password=dbpassword,port=dbport, host=dbhost, charset='utf8',database=database)
        self.cursor = self.conn.cursor()
    def login(self): #登录函数
        login = Login.Login(self.dbuser,self.dbpassword,self.dbport,self.dbhost,self.database,self.windows)
        login.login_windows()
    
    def logup(self): #注册函数
        logup = Logup.Logup(self.dbuser,self.dbpassword,self.dbport,self.dbhost,self.database,self.windows)
        logup.logup_windows()
    def main_windows(self):
        self.windows = tkinter.Tk()
        self.windows.title("图书库")
        self.login_button = ttk.Button(self.windows,text="登录",command=self.login)
        self.login_button.grid(row=0,column=0)
        self.logup_button = ttk.Button(self.windows,text="注册",command=self.logup)
        self.logup_button.grid(row=0, column=2)
        self.windows.mainloop()

if __name__ == '__main__':
    windows = tkinter.Tk()
    main = Main('root','hwh003561', 3306,'localhost','Bms',windows)
    main.main_windows()