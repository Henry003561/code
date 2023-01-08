import tkinter
from tkinter import ttk
import pymysql
import Main
from tkinter import messagebox

class Logup:
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
    def exit(self):
        main = Main.Main(self.dbuser,self.dbpassword,self.dbport,self.dbhost,self.database,self.windows)
        self.cursor.close()
        self.conn.close()
        main.main_windows()
    
    def logup(self):
        self.user = self.user_entry.get()
        self.password = self.password_entry.get()
        self.passwd_again = self.passwd_again_entry.get()
        self.email = self.email_entry.get()
        if len(self.password) == 0 or len(self.user)==0 or len(self.email)==0:
            messagebox.showerror(title='注册操作',message="请输入用户名或者密码")
        elif self.password == self.passwd_again:
            try:
                self.cursor.execute("select * from user where user='%s'and passwd='%s'and emai='%s'"%(self.user,self.password,self.email))
                self.conn.commit()
            except Exception as e:
                print(e)
                self.conn.rollback()
            else:
                result = self.cursor.fetchall()
                
                if len(result) == 0:
                    try:
                        self.cursor.execute('insert into user (user,passwd,emai) values ("%s","%s","%s")'%(self.user,self.password,self.email))
                        self.conn.commit()
                    except Exception as e:
                        print(e)
                        self.conn.rollback()
                    else:
                        messagebox.showinfo(title="注册操作",message="注册成功")
                        main = Main.Main(self.dbuser,self.dbpassword,self.dbport,self.dbhost,self.database,self.windows)
                        main.main_windows()
                else:
                    messagebox.showinfo(title='注册操作',message='该用户已经存在')
        else:
            messagebox.showerror(title="注册操作",message="密码不一致")
            
        
    def logup_windows(self):
        self.windows = tkinter.Tk()
        self.windows.title("图书库-注册界面")
        #用户名搭建
        self.user_label = ttk.Label(self.windows, text="用户名")
        self.user_label.grid(row=0,column=0)
        self.user_entry = ttk.Entry(self.windows)
        self.user_entry.grid(row=0,column=1)
        
        #密码搭建
        self.password_label =  ttk.Label(self.windows,text="密码") 
        self.password_label.grid(row=2,column=0)
        self.password_entry = ttk.Entry(self.windows,show='*')
        self.password_entry.grid(row=2,column=1)
        
        #再次确认密码搭建
        self.passwd_again_label = ttk.Label(self.windows, text="再次确认密码")
        self.passwd_again_label.grid(row=4, column=0)
        self.passwd_again_entry = ttk.Entry(self.windows,show='*')
        self.passwd_again_entry.grid(row=4,column=1)
        
        # 邮箱
        self.email_label = ttk.Label(self.windows, text="邮箱")
        self.email_label.grid(row=6,column=0)
        self.email_entry = ttk.Entry(self.windows)
        self.email_entry.grid(row=6,column=1)
        
        # 注册和退出搭建
        self.logup_button = ttk.Button(self.windows,text="注册",command=self.logup)
        self.logup_button.grid(row=8,column=0)
        self.exit_button = ttk.Button(self.windows,text="退出",command=self.exit)
        self.exit_button.grid(row=8,column=2)
        self.windows.mainloop()

if __name__ == '__main__':
    windows = tkinter.Tk()
    logup=Logup('root','hwh003561', 3306,'localhost','Bms',windows)
    logup.logup_windows()