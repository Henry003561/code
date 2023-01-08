import tkinter
from tkinter import ttk
import pymysql
from tkinter import messagebox
import Main

class Login:
    def __init__(self, dbuser, dbpassword, dbport, dbhost,database, windows):
        self.dbuser = dbuser
        self.dbpassword = dbpassword
        self.dbport = dbport
        self.dbhost = dbhost
        self.database = database
        # 删除上一个窗口
        windows.destroy()
        # 搭建数据库的数据链路
        self.conn = pymysql.connect(user=self.dbuser, password=self.dbpassword,port=self.dbport, host=self.dbhost, charset='utf8',database=self.database)
        self.cursor = self.conn.cursor()
    
    def exit(self):
        # 返回主页面
        self.main = Main.Main(self.dbuser, self.dbpassword, self.dbport, self.dbhost, self.database, self.windows)
        self.cursor.close()
        self.conn.close()
        self.main.main_windows()
    def login(self):
        self.user = self.user_text.get()
        self.password = self.password_text.get()
        try:
            # 服务器提取数据
            self.cursor.execute("select * from user where user='%s' and passwd='%s'"%(self.user,self.password))
            self.conn.commit()
            # 判断该用户是否存在
        except Exception as e:
            print(e)
            self.conn.rollback()
        else:
            result = self.cursor.fetchall()
            if len(result) == 0:
                messagebox.showwarning(title='登录操作',message='密码或者用户名错误')
            else:
                messagebox.showinfo(title='登录操作',message='登录成功')
                #TODO 进入系统
        
    def login_windows(self):
        self.windows = tkinter.Tk()
        self.windows.title("图书库-登录界面")
        # 用户名布局的创建
        self.user_label = ttk.Label(self.windows,text="用户名")
        self.user_label.grid(row=0, column=0)
        self.user_text = ttk.Entry(self.windows)
        self.user_text.grid(row=0,column=2)      
        # 密码布局的创建
        self.password_label = ttk.Label(self.windows, text='密码')
        self.password_label.grid(row=2,column=0)
        self.password_text = ttk.Entry(self.windows, show='*')
        self.password_text.grid(row=2, column=2)
        self.login_button = ttk.Button(self.windows, text='登录', command=self.login) #登录按钮
        self.login_button.grid(row=3,column=0)
        self.exit_button = ttk.Button(self.windows, text='退出', command=self.exit)
        self.exit_button.grid(row=3, column=2)
        self.windows.mainloop()

if __name__ == '__main__':
    windows = tkinter.Tk()
    login=Login('root','hwh003561', 3306,'localhost','Bms',windows)
    login.login_windows()