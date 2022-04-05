
from tkinter import *
import tkinter.messagebox
from tkinter import ttk,messagebox
import random
import time
import datetime
import sqlite3
#from tkmacosx import Button
from PIL import Image,ImageTk


class Login:
    def __init__(self,root):
        self.root = root
        self.root.title("Login Window")
        self.root.geometry("1200x700+100+100")
        self.root.config(bg="alice blue")

        self.bg = ImageTk.PhotoImage(file="Images/bg4.png")
        bg = Label(self.root, image= self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        #----Frame-------

        login_frame = Frame(self.root,bg="alice blue")
        login_frame.place(x=200, y=100 ,width= 800, height= 500)

        title = Label(login_frame,text="RTO Management System",font=("times new roman",40,"bold"),justify= CENTER, bg="#033054",fg="alice blue").place(width=800, height=60)

        log = Label(login_frame,text="LOGIN HERE",font=("times new roman",30,"bold"),fg="cyan4",bg="alice blue").place(x=80 ,y=80)

        self.bg1 = ImageTk.PhotoImage(file="Images/log1.png")
        bg1 = Label(login_frame, image= self.bg1 ,bg="alice blue").place(x=300,y=130,width=150,height=147)

        email = Label(login_frame,text="Email Id",font=("times new roman",25,"bold"),bg="alice blue").place(x=200 ,y=290)
        self.txt_email = Entry(login_frame,font=("times new roman",20),bg="light grey")
        self.txt_email.place(x=320 ,y=290)

        passw = Label(login_frame,text="Password",font=("times new roman",25,"bold"),bg="alice blue").place(x=200 ,y=340)
        self.txt_passw = Entry(login_frame,font=("times new roman",20),bg="light grey",show="*")
        self.txt_passw.place(x=320 ,y=340)


        btn_reg = Button(login_frame,text="Register New Account",font=("times new roman",14),fg="#B00857",bg="alice blue",bd=0,command=self.reg_window ).place(x=200,y=390)

        btn_fgt = Button(login_frame,text="Forgot Password ?",font=("times new roman",14),fg="#B00857",bg="alice blue",bd=0,command= self.forget_pass_window).place(x=390,y=390)

        self.btn_img = ImageTk.PhotoImage(file = "Images/log_btn.png")
        btn_login = Button(login_frame,image =self.btn_img,bd=0,bg="alice blue",command=self.login).place(x=300,y=430,width=150,height=41)


    def forget_pass(self):
        if self.cmb_question.get()=="Select the Question" or self.txt_ans.get()=="" or self.txt_new_passw.get()=="" or self.txt_new_cpassw.get()=="":
            messagebox.showerror("Error !","All fields are required", parent = self.root2)

        elif self.txt_new_passw.get()!=self.txt_new_cpassw.get():
            messagebox.showerror("Error !","Your password doesn't matches with confirm password", parent = self.root2)

        else:

            try:
                con= sqlite3.connect(database ="RTO.db")
                cur=con.cursor()

                cur.execute("Select * from Employee where email=? and question=? and answer=?",(self.txt_email.get(),self.cmb_question.get(),self.txt_ans.get()))
                row=cur.fetchone()

                if row==None:
                    messagebox.showerror("Error !","Please enter correct Security Question/Answer", parent = self.root2)

                else:
                    cur.execute("update Employee set passw=? where email=? ",(self.txt_new_passw.get(),self.txt_email.get()))
                    messagebox.showinfo("Success","Password Changed !",parent =self.root2)
                    con.commit()
                    self.root2.destroy()

            except Exception as ex:
                messagebox.showerror("Error !",f"Error due to {str(ex)}")

    def forget_pass_window(self):

        if self.txt_email.get()=="":
            messagebox.showerror("Error !","Email ID is required", parent = self.root)

        else:
            try:
                con= sqlite3.connect(database ="RTO.db")
                cur=con.cursor()

                cur.execute("Select * from Employee where email=?",(self.txt_email.get(),))
                row=cur.fetchone()

                if row==None:
                    messagebox.showerror("Error !","Email Id does not exists", parent = self.root)

                else:
                    con.commit()
                    self.root2 = Toplevel()
                    self.root2.title("Forget Password")
                    self.root2.geometry("350x400+530+290")
                    self.root2.config(bg="alice blue")
                    self.root2.focus_force()
                    

                    t=Label(self.root2,text="Forget Password",font=("times new roman",25,"bold"),bg="alice blue",fg="red").place(x=0,y=5,relwidth=1)

                    self.var_question = StringVar()
                    self.var_ans = StringVar()
                    self.var_passw = StringVar()
                    self.var_cpassw = StringVar()



                    question = Label(self.root2, text="Security Question", font=("times new roman",15,"bold"),bg="alice blue",fg="grey").place(x=50,y=50)
                    self.cmb_question = ttk.Combobox(self.root2, font=("times new roman",13), state='readonly',textvariable = self.var_question)
                    self.cmb_question["values"]=("Select the Question","What's your pet name ?","What's your favourite place ?","What's your hero name ?")
                    self.cmb_question.current(0)
                    self.cmb_question.place(x=50,y=80,width=250)

                    ans = Label(self.root2, text="Answer", font=("times new roman",15,"bold"),bg="alice blue",fg="grey").place(x=50,y=110)
                    self.txt_ans = Entry(self.root2, textvariable = self.var_ans, font=("times new roman",15))
                    self.txt_ans.place(x=50,y=140)


                    passw = Label(self.root2, text="New Password", font=("times new roman",15,"bold"),bg="alice blue",fg="grey").place(x=50,y=180)
                    self.txt_new_passw = Entry(self.root2, textvariable = self.var_passw, font=("times new roman",15),show='*')
                    self.txt_new_passw.place(x=50,y=210)

                    cpassw = Label(self.root2, text="Confirm Password", font=("times new roman",15,"bold"),bg="alice blue",fg="grey").place(x=50,y=250)
                    self.txt_new_cpassw = Entry(self.root2, textvariable = self.var_cpassw, font=("times new roman",15),show='*')
                    self.txt_new_cpassw.place(x=50,y=280)

                    #----Check Button------------------

                    def mark():

                        if var.get()==1:
                            self.txt_new_passw.configure(show="")
                            self.txt_new_cpassw.configure(show="")
                        if var.get()==0:
                            self.txt_new_passw.configure(show="*")
                            self.txt_new_cpassw.configure(show="*")

                    var = IntVar()

                    bt = Checkbutton(self.root2,text="Show Password", font=("times new roman",15), command= mark, offvalue=0 , onvalue = 1, variable = var,bg="alice blue")
                    bt.place(x=50,y=320)

                    btn_change_pass = Button(self.root2, text="Reset Password",font=("times new roman",15),bg="green",fg="white",command=self.forget_pass).place(x=100,y=360)




                    


            except Exception as ex:
                messagebox.showerror("Error !",f"Error due to {str(ex)}")








    def login(self):
        if self.txt_email.get()=="" or self.txt_passw=="" :
            messagebox.showerror("Error !","All Fields are required", parent = self.root)

        else:

            try:
                con= sqlite3.connect(database ="RTO.db")
                cur=con.cursor()

                cur.execute("Select * from Employee where email=? and passw=?",(self.txt_email.get(),self.txt_passw.get()))
                row=cur.fetchone()

                if row==None:
                    messagebox.showerror("Error !","Invalid Username and Password", parent = self.root)

                else:
                    messagebox.showinfo("Success",f"Welcome {row[0]} !",parent =self.root)
                    self.dash_window()


            except Exception as ex:
                messagebox.showerror("Error !",f"Error due to {str(ex)}")

    def reg_window(self):
        self.newWindow = Toplevel(self.root)
        self.new_obj= Register(self.newWindow)

    def dash_window(self):
        self.newWindow1 = Toplevel(self.root)
        self.new_obj1 = Dashboard(self.newWindow1)


class Register:
    def __init__(self,root):
        self.root = root
        self.root.title("Registration Window")
        self.root.geometry("1200x700+100+100")
        self.root.config(bg="alice blue")

        # BG Image
        self.bg = ImageTk.PhotoImage(file="Images/bg1.jpeg")
        bg = Label(self.root, image= self.bg).place(x=350,y=0,relwidth=1,relheight=1)


        # LEFT Image
        self.left = ImageTk.PhotoImage(file="Images/left.png")
        left = Label(self.root, image= self.left).place(x=20,y=100,width=475,height=488)

        #---Variables------
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_question = StringVar()
        self.var_ans = StringVar()
        self.var_passw = StringVar()
        self.var_cpassw = StringVar()
        

        # Check Button Functonality (Show password)
        

        # Register Frame
        frame1 = Frame(self.root, bg = "alice blue" )
        frame1.place(x=495,y=100,width = 600, height=488)

        title = Label(frame1, text="REGISTER HERE", font=("times new roman",24,"bold"),bg="alice blue",fg="green").place(x=50,y=30)

        fname = Label(frame1, text="First Name", font=("times new roman",15,"bold"),bg="alice blue",fg="grey").place(x=50,y=100)
        txt_fname = Entry(frame1, textvariable = self.var_fname, font=("times new roman",15)).place(x=50,y=130)

        lname = Label(frame1, text="Last Name", font=("times new roman",15,"bold"),bg="alice blue",fg="grey").place(x=300,y=100)
        txt_lname = Entry(frame1, textvariable = self.var_lname, font=("times new roman",15)).place(x=300,y=130)

        contact = Label(frame1, text="Contact No.", font=("times new roman",15,"bold"),bg="alice blue",fg="grey").place(x=50,y=170)
        txt_contact = Entry(frame1, textvariable = self.var_contact, font=("times new roman",15)).place(x=50,y=200)

        email = Label(frame1, text="Email Id", font=("times new roman",15,"bold"),bg="alice blue",fg="grey").place(x=300,y=170)
        txt_email = Entry(frame1, textvariable = self.var_email, font=("times new roman",15)).place(x=300,y=200)


        question = Label(frame1, text="Security Question", font=("times new roman",15,"bold"),bg="alice blue",fg="grey").place(x=50,y=240)
        cmb_question = ttk.Combobox(frame1, font=("times new roman",13), state='readonly',textvariable = self.var_question)
        cmb_question["values"]=("Select the Question","What's your pet name ?","What's your favourite place ?","What's your hero name ?")
        cmb_question.current(0)
        cmb_question.place(x=50,y=270,width=180)

        ans = Label(frame1, text="Answer", font=("times new roman",15,"bold"),bg="alice blue",fg="grey").place(x=300,y=240)
        txt_ans = Entry(frame1, textvariable = self.var_ans, font=("times new roman",15)).place(x=300,y=270)


        passw = Label(frame1, text="Password", font=("times new roman",15,"bold"),bg="alice blue",fg="grey").place(x=50,y=310)
        txt_passw = Entry(frame1, textvariable = self.var_passw, font=("times new roman",15),show='*')
        txt_passw.place(x=50,y=340)

        cpassw = Label(frame1, text="Confirm Password", font=("times new roman",15,"bold"),bg="alice blue",fg="grey").place(x=300,y=310)
        txt_cpassw = Entry(frame1, textvariable = self.var_cpassw, font=("times new roman",15),show='*')
        txt_cpassw.place(x=300,y=340)

        #----Check Button------------------

        def mark():

            if var.get()==1:
                txt_passw.configure(show="")
                txt_cpassw.configure(show="")
            if var.get()==0:
                txt_passw.configure(show="*")
                txt_cpassw.configure(show="*")

        var = IntVar()

        bt = Checkbutton(frame1,text="Show Password", font=("times new roman",15), command= mark, offvalue=0 , onvalue = 1, variable = var,bg="alice blue")
        bt.place(x=50,y=375)



        #----Buttons------------------

        self.btn_img = ImageTk.PhotoImage(file = "Images/reg_btn.png")
        btn_register = Button(frame1,image =self.btn_img,bd=0,bg="alice blue",command=self.register_data).place(x=50,y=410,width=300,height=50)

        btn_login = Button(self.root ,text="Sign In",font=("times new roman",20),bg="alice blue",bd=0,command= self.root.destroy).place(x=310,y=500,width=150,height=44)

        
    

    #----Backend-------------------

    def register_data(self):

        con= sqlite3.connect(database ="RTO.db")
        cur=con.cursor()

        try:
            if self.var_fname.get()=="":
                messagebox.showerror("Error !","First Name is required", parent = self.root)

            elif self.var_lname.get()=="":
                messagebox.showerror("Error !","Last Name is required", parent = self.root)

            elif self.var_contact.get()=="":
                messagebox.showerror("Error !","Contact No is required", parent = self.root)

            elif self.var_email.get()=="":
                messagebox.showerror("Error !","Email ID is required", parent = self.root)

            elif self.var_question.get()=="Select the Question":
                messagebox.showerror("Error !","Security question is not selected", parent = self.root)

            elif self.var_ans.get()=="":
                messagebox.showerror("Error !","Security Answer is required", parent = self.root)

            elif self.var_passw.get()=="":
                messagebox.showerror("Error !","password is required", parent = self.root)

            elif self.var_cpassw.get()=="":
                messagebox.showerror("Error !","Please confirm your password", parent = self.root)

            elif self.var_cpassw.get()!=self.var_passw.get():
                messagebox.showerror("Error !","Your password doesn't matches with confirm password", parent = self.root)

            else:

                cur.execute("Select * from Employee where email=?",(self.var_email.get(),))
                row=cur.fetchone()

                if row!=None:
                    messagebox.showerror("Error !","Email ID already exists", parent = self.root)

                else:
                    cur.execute("insert into Employee(fname,lname,contact,email,question,answer,passw,cpassw) values(?,?,?,?,?,?,?,?)", (
                        self.var_fname.get(),
                        self.var_lname.get(),
                        self.var_contact.get(),
                        self.var_email.get(),
                        self.var_question.get(),
                        self.var_ans.get(),
                        self.var_passw.get(),
                        self.var_cpassw.get()
                        ))
                    con.commit()
                    messagebox.showinfo("Success","Registered Successfully !",parent =self.root)

                    #---Clearing all values------
                    
                    self.var_lname.set("")
                    self.var_fname.set(""),
                    self.var_contact.set(""),
                    self.var_email.set(""),
                    self.var_question.set("Select the Question"),
                    self.var_ans.set(""),
                    self.var_passw.set("")
                    self.var_cpassw.set("")

        except Exception as ex:
            messagebox.showerror("Error !",f"Error due to {str(ex)}")


        self.var_lname.set("")
        self.var_fname.set(""),
        self.var_contact.set(""),
        self.var_email.set(""),
        self.var_question.set("Select the Question"),
        self.var_ans.set(""),
        self.var_passw.set("")
        self.var_cpassw.set("")
        
                


        
class Dashboard:
    def __init__(self,root):
        self.root=root
        self.root.title("RTO Management System")
        self.root.geometry("1200x700+100+100")
        self.root.config(bg="alice blue")

        # BG Image
        self.bg_dash = ImageTk.PhotoImage(file="Images/bg_dash.png")
        bg1 = Label(self.root, image= self.bg_dash).place(x=0,y=0,width=1200,height=630)
        bg2 = Label(self.root,bg="gray29").place(x=0,y=625,width=1200,height=80)

        dashboard_frame = LabelFrame(self.root,text="Services",font=("times new roman",30,"bold"),bg="light blue",)
        dashboard_frame.place(x=20, y=20 ,width= 500, height= 200)

        btn_veh_reg = Button(dashboard_frame,text="Vehicle Registration",font=("times new roman",20),bg="peach puff",bd=0,command=self.VehicleReg_window).place(x=150,y=20)
        btn_lic = Button(dashboard_frame,text="Manage License",font=("times new roman",20),bg="peach puff",bd=0,command=self.DrivingLic_window).place(x=170,y=80)

    def VehicleReg_window(self):
        self.newWindow = Toplevel(self.root)
        self.new_obj=RegClass(self.newWindow)
        
    def DrivingLic_window(self):
        self.newWindow1 = Toplevel(self.root)
        self.new_obj1 = DriClass(self.newWindow1)       

class RegClass:
    def __init__(self,root):
        self.root=root
        self.root.title("RTO Management System")
        self.root.geometry("1200x700+100+100")
        self.root.config(bg="white")
        
        # Title
        title = Label(self.root, text="Manage Vehicle Registration", font= ("goudy old style",30,"bold"),justify="center",bg="#033054",fg="white").place(width=1200,height=35)

        # Label Widgets
        l_carModel = Label(self.root, text="Car Model :", font= ("goudy old style",20,"bold"),bg="white").place(x=80,y=60)
        l_ownerName = Label(self.root, text="Owner's Name :", font= ("goudy old style",20,"bold"),bg="white").place(x=80,y=100)
        l_vehicleNo = Label(self.root, text="Vehicle No :", font= ("goudy old style",20,"bold"),bg="white").place(x=80,y=140)
        l_vehicleType = Label(self.root, text="Vehicle Type :", font= ("goudy old style",20,"bold"),bg="white").place(x=80,y=180)
        l_modelNo = Label(self.root, text="Model No :", font= ("goudy old style",20,"bold"),bg="white").place(x=80,y=220)
        l_mobileNo = Label(self.root, text="Mobile No :", font= ("goudy old style",20,"bold"),bg="white").place(x=80,y=260)
        l_emailId = Label(self.root, text="Email ID :", font= ("goudy old style",20,"bold"),bg="white").place(x=80,y=300)

        # Variables
        self.var_carmodel = StringVar()
        self.var_ownernm = StringVar()
        self.var_vehicleno = StringVar()
        self.var_vehicletype = StringVar()
        self.var_modelno = StringVar()
        self.var_mobile = StringVar()
        self.var_email = StringVar()
        self.var_search = StringVar()

        # Entry Fields
        self.txt_carModel = Entry(self.root,textvariable = self.var_carmodel,font= ("goudy old style",15),bg='lightyellow')
        self.txt_carModel.place(x=300,y=60,width=200)

        self.txt_ownerName = Entry(self.root,textvariable = self.var_ownernm, font= ("goudy old style",15),bg='lightyellow')
        self.txt_ownerName.place(x=300,y=100,width=200)

        self.txt_vehicleNo = Entry(self.root,textvariable = self.var_vehicleno, font= ("goudy old style",15),bg='lightyellow')
        self.txt_vehicleNo.place(x=300,y=140,width=200)

        self.txt_vehicleType = ttk.Combobox(self.root,textvariable = self.var_vehicletype, font= ("goudy old style",15),values=("Select Vehicle Type","Two Wheeler", "Four Wheeler"),state = 'readonly')
        self.txt_vehicleType.place(x=300,y=180,width=200)
        self.txt_vehicleType.current(0)

        self.txt_modelNo = Entry(self.root,textvariable = self.var_modelno, font= ("goudy old style",15),bg='lightyellow')
        self.txt_modelNo.place(x=300,y=220,width=200)

        self.txt_mobileNo = Entry(self.root,textvariable = self.var_mobile, font= ("goudy old style",15),bg='lightyellow')
        self.txt_mobileNo.place(x=300,y=260,width=200)

        self.txt_emailId = Entry(self.root,textvariable = self.var_email, font= ("goudy old style",15),bg='lightyellow')
        self.txt_emailId.place(x=300,y=300,width=200)

        # Buttons
        self.btn_add = Button(self.root,text="ADD",font= ("goudy old style",15,"bold"), bg="#2196f3",fg = "white",command= self.add)
        self.btn_add.place(x=60,y=400,width=100)

        self.btn_update = Button(self.root,text="UPDATE",font= ("goudy old style",15,"bold"), bg="#4caf50",fg = "white", command= self.update)
        self.btn_update.place(x=180,y=400,width=100)

        self.btn_delete = Button(self.root,text="DELETE",font= ("goudy old style",15,"bold"), bg="#f44336",fg = "white", command= self.delete)
        self.btn_delete.place(x=300,y=400,width=100)

        self.btn_clear = Button(self.root,text="CLEAR",font= ("goudy old style",15,"bold"), bg="#607d8b",fg = "white",command= self.clear)
        self.btn_clear.place(x=420,y=400,width=100)

        #search panel
        l_search = Label(self.root, text="Search By | Vehicle No  :", font= ("goudy old style",15,"bold"),bg="white").place(x=600,y=60)

        txt_search = Entry(self.root,textvariable = self.var_search,font= ("goudy old style",15),bg='lightyellow').place(x=800,y=60,width=180)

        btn_search = Button(self.root,text="Search",font= ("goudy old style",15,"bold"), bg="#03a9f4",fg = "white", command= self.search).place(x=1030,y=60,width=120)


        # Content
        self.R_Frame = Frame(self.root, bd=2, relief =RIDGE)
        self.R_Frame.place(x=600, y=100, width=550, height=340)

        scrolly = Scrollbar(self.R_Frame, orient=VERTICAL)
        scrollx = Scrollbar(self.R_Frame, orient=HORIZONTAL)
        self.RegistrationTable = ttk.Treeview(self.R_Frame,columns=("model","name","vehicleno","vehicletype","modelno","mobile","email"), xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)
        scrollx.pack(side= BOTTOM, fill=X )
        scrolly.pack(side= RIGHT, fill=Y )
        scrollx.config(command=self.RegistrationTable.xview)
        scrolly.config(command=self.RegistrationTable.yview)

        self.RegistrationTable.heading("model",text="Car Model")
        self.RegistrationTable.heading("name",text="Owner Name")
        self.RegistrationTable.heading("vehicleno",text="Vehicle No")
        self.RegistrationTable.heading("vehicletype",text="Vehicle Type")
        self.RegistrationTable.heading("modelno",text="Model No")
        self.RegistrationTable.heading("mobile",text="Mobile")
        self.RegistrationTable.heading("email",text="Email ID")

        self.RegistrationTable["show"]='headings'

        self.RegistrationTable.column("model",width=50)
        self.RegistrationTable.column("name",width=50)
        self.RegistrationTable.column("vehicleno",width=50)
        self.RegistrationTable.column("vehicletype",width=50)
        self.RegistrationTable.column("modelno",width=50)
        self.RegistrationTable.column("mobile",width=50)
        self.RegistrationTable.column("email",width=50)

        self.RegistrationTable.pack(fill=BOTH, expand=1)
        self.RegistrationTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()


    def get_data(self,ev):
        self.txt_vehicleNo.config(state='readonly')
        self.txt_vehicleType.config(state='disabled')

        r=self.RegistrationTable.focus()
        content=self.RegistrationTable.item(r)
        row=content["values"]
        
        self.var_carmodel.set(row[0])
        self.var_ownernm.set(row[1])
        self.var_vehicleno.set(row[2])
        self.var_vehicletype.set(row[3])
        self.var_modelno.set(row[4])
        self.var_mobile.set(row[5])
        self.var_email.set(row[6])


    def add(self):

        con= sqlite3.connect(database ="RTO.db")
        cur=con.cursor()

        try:
            if self.var_carmodel.get()=="":
                messagebox.showerror("Error !","Car Model is required", parent = self.root)

            elif self.var_ownernm.get()=="":
                messagebox.showerror("Error !","Owner Name is required", parent = self.root)

            elif self.var_vehicleno.get()=="":
                messagebox.showerror("Error !","Vehicle No is required", parent = self.root)

            elif self.var_vehicletype.get()=="Select Vehicle Type":
                messagebox.showerror("Error !","Vehicle Type not Selected", parent = self.root)

            elif self.var_modelno.get()=="":
                messagebox.showerror("Error !","Model No is required", parent = self.root)

            elif self.var_mobile.get()=="":
                messagebox.showerror("Error !","Mobile No is required", parent = self.root)

            elif self.var_email.get()=="":
                messagebox.showerror("Error !","Email ID is required", parent = self.root)

            else:

                cur.execute("Select * from Veh_Registration where vehicleno=?",(self.var_vehicleno.get(),))
                row=cur.fetchone()

                if row!=None:
                    messagebox.showerror("Error !","Vehicle No already exists", parent = self.root)

                else:
                    cur.execute("insert into Veh_Registration(model,name,vehicleno,vehicletype,modelno,mobile,email) values(?,?,?,?,?,?,?)", (
                        self.var_carmodel.get(),
                        self.var_ownernm.get(),
                        self.var_vehicleno.get(),
                        self.var_vehicletype.get(),
                        self.var_modelno.get(),
                        self.var_mobile.get(),
                        self.var_email.get()
                        ))
                    con.commit()
                    messagebox.showinfo("Success","Record Added Successfully !",parent =self.root)
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error !",f"Error due to {str(ex)}")
    
    def show(self):

        con= sqlite3.connect(database ="RTO.db")
        cur=con.cursor()

        try:
            cur.execute("Select * from Veh_Registration")
            rows=cur.fetchall()
            self.RegistrationTable.delete(*self.RegistrationTable.get_children())
            for row in rows:
                self.RegistrationTable.insert('',END,values=row)

            
        except Exception as ex:
            messagebox.showerror("Error !",f"Error due to {str(ex)}")



    def update(self):

        con= sqlite3.connect(database ="RTO.db")
        cur=con.cursor()

        try:
            if self.var_carmodel.get()=="":
                messagebox.showerror("Error !","Car Model is required", parent = self.root)

            elif self.var_ownernm.get()=="":
                messagebox.showerror("Error !","Owner Name is required", parent = self.root)

            elif self.var_vehicleno.get()=="":
                messagebox.showerror("Error !","Vehicle No is required", parent = self.root)

            elif self.var_vehicletype.get()=="Select Vehicle Type":
                messagebox.showerror("Error !","Vehicle Type not Selected", parent = self.root)

            elif self.var_modelno.get()=="":
                messagebox.showerror("Error !","Model No is required", parent = self.root)

            elif self.var_mobile.get()=="":
                messagebox.showerror("Error !","Mobile No is required", parent = self.root)

            elif self.var_email.get()=="":
                messagebox.showerror("Error !","Email ID is required", parent = self.root)

            else:

                cur.execute("Select * from Veh_Registration where vehicleno=?",(self.var_vehicleno.get(),))
                row=cur.fetchone()

                if row==None:
                    messagebox.showerror("Error !","Select the data to be updated from the list", parent = self.root)

                else:
                    cur.execute("update Veh_Registration set model=?,name=?,vehicletype=?,modelno=?,mobile=?,email=? where vehicleno=?", (
                        self.var_carmodel.get(),
                        self.var_ownernm.get(),
                        self.var_vehicletype.get(),
                        self.var_modelno.get(),
                        self.var_mobile.get(),
                        self.var_email.get(),
                        self.var_vehicleno.get()
                        ))
                    con.commit()
                    messagebox.showinfo("Success","Record Updated Successfully !",parent =self.root)
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error !",f"Error due to {str(ex)}")

    def delete(self):
        con= sqlite3.connect(database ="RTO.db")
        cur=con.cursor()

        try:
            if self.var_carmodel.get()=="":
                messagebox.showerror("Error !","Car Model is required", parent = self.root)

            elif self.var_ownernm.get()=="":
                messagebox.showerror("Error !","Owner Name is required", parent = self.root)

            elif self.var_vehicleno.get()=="":
                messagebox.showerror("Error !","Vehicle No is required", parent = self.root)

            elif self.var_vehicletype.get()=="Select Vehicle Type":
                messagebox.showerror("Error !","Vehicle Type not Selected", parent = self.root)

            elif self.var_modelno.get()=="":
                messagebox.showerror("Error !","Model No is required", parent = self.root)

            elif self.var_mobile.get()=="":
                messagebox.showerror("Error !","Mobile No is required", parent = self.root)

            elif self.var_email.get()=="":
                messagebox.showerror("Error !","Email ID is required", parent = self.root)

            else:

                cur.execute("Select * from Veh_Registration where vehicleno=?",(self.var_vehicleno.get(),))
                row=cur.fetchone()

                if row==None:
                    messagebox.showerror("Error !","Select the data to be deleted from the list", parent = self.root)

                else:
                    op=messagebox.askyesno("Confirm","Do you want to delete the record",parent= self.root)
                    if op==True:
                        cur.execute("delete from Veh_Registration where vehicleno=?",(self.var_vehicleno.get(),))
                        con.commit()    
                        messagebox.showinfo("Success","Record Deleted Successfully !",parent=self.root)
                        self.clear()

        except Exception as ex:
            messagebox.showerror("Error !",f"Error due to {str(ex)}")

    def search(self):
        con= sqlite3.connect(database ="RTO.db")
        cur=con.cursor()

        try:
            cur.execute(f"Select * from Veh_Registration where vehicleno LIKE '%{self.var_search.get()}%' ")
            rows=cur.fetchall()
            self.RegistrationTable.delete(*self.RegistrationTable.get_children())
            for row in rows:
                self.RegistrationTable.insert('',END,values=row)

            
        except Exception as ex:
            messagebox.showerror("Error !",f"Error due to {str(ex)}")


    def clear(self):
        self.show()
        self.txt_vehicleNo.config(state='normal')
        self.txt_vehicleType.config(state='normal')
        self.var_carmodel.set("")
        self.var_ownernm.set(""),
        self.var_vehicletype.set("Select Vehicle Type"),
        self.var_modelno.set(""),
        self.var_mobile.set(""),
        self.var_email.set(""),
        self.var_vehicleno.set("")
        self.var_search.set("")

class DriClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Driving License Services")
        self.root.geometry("1200x700+100+100")
        self.root.config(bg="white")
        
        # Title
        title = Label(self.root, text="Manage Driving License Details", font= ("goudy old style",30,"bold"),justify="center",bg="#033054",fg="white").place(width=1200,height=35)

        # Label Widgets
        l_dlllnum = Label(self.root, text="DL/LL Number", font= ("goudy old style",20,"bold"),bg="white").place(x=10,y=60)
        l_ownernm = Label(self.root, text="Owner's Name", font= ("goudy old style",20,"bold"),bg="white").place(x=10,y=100)
        l_email = Label(self.root, text="Email ID", font= ("goudy old style",20,"bold"),bg="white").place(x=10,y=140)
        l_gender = Label(self.root, text="Gender", font= ("goudy old style",20,"bold"),bg="white").place(x=10,y=180)
        l_dob = Label(self.root, text="D.O.B(dd-mm-yyyy)", font= ("goudy old style",20,"bold"),bg="white").place(x=600,y=60)
        l_mobile = Label(self.root, text="Contact No", font= ("goudy old style",20,"bold"),bg="white").place(x=600,y=100)
        l_vehicleclass = Label(self.root, text="Class of Vehicle", font= ("goudy old style",20,"bold"),bg="white").place(x=600,y=140)
        l_validupto = Label(self.root, text="Valid Upto", font= ("goudy old style",20,"bold"),bg="white").place(x=600,y=180)
        l_state = Label(self.root, text="State", font= ("goudy old style",20,"bold"),bg="white").place(x=10,y=220)
        l_city = Label(self.root, text="City", font= ("goudy old style",20,"bold"),bg="white").place(x=450,y=220)
        l_pincode = Label(self.root, text="Pincode", font= ("goudy old style",20,"bold"),bg="white").place(x=750,y=220)
        l_address = Label(self.root, text="Address", font= ("goudy old style",20,"bold"),bg="white").place(x=10,y=260)

        
        # Variables
        self.var_dlllnum = StringVar()
        self.var_ownernm = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_vehicleclass = StringVar()
        self.var_validupto = StringVar()
        self.var_state = StringVar()
        self.var_city = StringVar()
        self.var_pincode = StringVar()
        self.var_address = StringVar()
        self.var_mobile = StringVar()
        self.var_email = StringVar()
        self.var_search = StringVar()

        # Entry Fields
        self.txt_dlllnum = Entry(self.root,textvariable = self.var_dlllnum,font= ("goudy old style",15),bg='lightyellow')
        self.txt_dlllnum.place(x=200,y=60,width=200)

        self.txt_ownernm = Entry(self.root,textvariable = self.var_ownernm, font= ("goudy old style",15),bg='lightyellow')
        self.txt_ownernm.place(x=200,y=100,width=200)

        self.txt_gender = Entry(self.root,textvariable = self.var_gender, font= ("goudy old style",15),bg='lightyellow')
        self.txt_gender.place(x=200,y=180,width=200)

        self.txt_vehicleclass= ttk.Combobox(self.root,textvariable = self.var_vehicleclass, font= ("goudy old style",15),values=("Select Vehicle Type","Two Wheeler", "Four Wheeler"),state = 'readonly')
        self.txt_vehicleclass.place(x=850,y=140,width=200)
        self.txt_vehicleclass.current(0)

        self.txt_dob = Entry(self.root,textvariable = self.var_dob, font= ("goudy old style",15),bg='lightyellow')
        self.txt_dob.place(x=850,y=60,width=200)

        self.txt_mobile = Entry(self.root,textvariable = self.var_mobile, font= ("goudy old style",15),bg='lightyellow')
        self.txt_mobile.place(x=850,y=100,width=200)

        self.txt_email = Entry(self.root,textvariable = self.var_email, font= ("goudy old style",15),bg='lightyellow')
        self.txt_email.place(x=200,y=140,width=200)
        
        self.txt_validupto = Entry(self.root,textvariable = self.var_validupto, font= ("goudy old style",15),bg='lightyellow')
        self.txt_validupto.place(x=850,y=180,width=200)
        
        self.txt_state = Entry(self.root,textvariable = self.var_state, font= ("goudy old style",15),bg='lightyellow')
        self.txt_state.place(x=200,y=220,width=200)
        
        self.txt_city = Entry(self.root,textvariable = self.var_city, font= ("goudy old style",15),bg='lightyellow')
        self.txt_city.place(x=510,y=220,width=200)
        
        self.txt_pincode = Entry(self.root,textvariable = self.var_pincode, font= ("goudy old style",15),bg='lightyellow')
        self.txt_pincode.place(x=900,y=220,width=200)
        
        self.txt_address = Entry(self.root,textvariable = self.var_address, font= ("goudy old style",15),bg='lightyellow')
        self.txt_address.place(x=200,y=260,width=600,height=100)

        # Buttons
        self.btn_add = Button(self.root,text="ADD",font= ("goudy old style",15,"bold"), bg="#2196f3",fg = "white",command= self.add)
        self.btn_add.place(x=60,y=400,width=100)

        self.btn_update = Button(self.root,text="UPDATE",font= ("goudy old style",15,"bold"), bg="#4caf50",fg = "white", command= self.update)
        self.btn_update.place(x=180,y=400,width=100)

        self.btn_delete = Button(self.root,text="DELETE",font= ("goudy old style",15,"bold"), bg="#f44336",fg = "white", command= self.delete)
        self.btn_delete.place(x=300,y=400,width=100)

        self.btn_clear = Button(self.root,text="CLEAR",font= ("goudy old style",15,"bold"), bg="#607d8b",fg = "white",command= self.clear)
        self.btn_clear.place(x=420,y=400,width=100)

        #search panel
        l_search = Label(self.root, text="Search By | DL/LL No  :", font= ("goudy old style",15,"bold"),bg="white").place(x=600,y=400)

        txt_search = Entry(self.root,textvariable = self.var_search,font= ("goudy old style",15),bg='lightyellow').place(x=800,y=400,width=200)

        btn_search = Button(self.root,text="Search",font= ("goudy old style",15,"bold"), bg="#03a9f4",fg = "white", command= self.search).place(x=1030,y=400,width=120)


        # Content
        self.R_Frame = Frame(self.root, bd=2, relief =RIDGE)
        self.R_Frame.place(x=10, y=450, width=1175, height=245)

        scrolly = Scrollbar(self.R_Frame, orient=VERTICAL)
        scrollx = Scrollbar(self.R_Frame, orient=HORIZONTAL)
        self.DrivingLicenseTable = ttk.Treeview(self.R_Frame,columns=("dlllnum","ownernm","email","gender","dob","mobile","vehicleclass","validupto","state","city","pincode","address"), xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)
        scrollx.pack(side= BOTTOM, fill=X )
        scrolly.pack(side= RIGHT, fill=Y )
        scrollx.config(command=self.DrivingLicenseTable.xview)
        scrolly.config(command=self.DrivingLicenseTable.yview)

        self.DrivingLicenseTable.heading("dlllnum",text="DL/LL Number")
        self.DrivingLicenseTable.heading("ownernm",text="Name")
        self.DrivingLicenseTable.heading("email",text="Email id")
        self.DrivingLicenseTable.heading("gender",text="Gender")
        self.DrivingLicenseTable.heading("dob",text="D.O.B")
        self.DrivingLicenseTable.heading("mobile",text="Mobile")
        self.DrivingLicenseTable.heading("vehicleclass",text="C.O.V")
        self.DrivingLicenseTable.heading("validupto",text="Valid Upto")
        self.DrivingLicenseTable.heading("state",text="State")
        self.DrivingLicenseTable.heading("city",text="City")
        self.DrivingLicenseTable.heading("pincode",text="Pin Code")
        self.DrivingLicenseTable.heading("address",text="Address")


        self.DrivingLicenseTable["show"]='headings'

        self.DrivingLicenseTable.column("dlllnum",width=50)
        self.DrivingLicenseTable.column("ownernm",width=50)
        self.DrivingLicenseTable.column("email",width=50)
        self.DrivingLicenseTable.column("gender",width=50)
        self.DrivingLicenseTable.column("dob",width=50)
        self.DrivingLicenseTable.column("mobile",width=50)
        self.DrivingLicenseTable.column("vehicleclass",width=50)
        self.DrivingLicenseTable.column("validupto",width=50)
        self.DrivingLicenseTable.column("state",width=50)
        self.DrivingLicenseTable.column("city",width=50)
        self.DrivingLicenseTable.column("pincode",width=50)
        self.DrivingLicenseTable.column("address",width=50)



        self.DrivingLicenseTable.pack(fill=BOTH, expand=1)
        self.DrivingLicenseTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()


    def get_data(self,ev):
        self.txt_dlllnum.config(state='readonly')
        self.txt_vehicleclass.config(state='disabled')

        r=self.DrivingLicenseTable.focus()
        content=self.DrivingLicenseTable.item(r)
        row=content["values"]
        
        self.var_dlllnum.set(row[0])
        self.var_ownernm.set(row[1])
        self.var_email.set(row[2])
        self.var_gender.set(row[3])
        self.var_dob.set(row[4])
        self.var_mobile.set(row[5])
        self.var_vehicleclass.set(row[6])
        self.var_validupto.set(row[7])
        self.var_state.set(row[8])
        self.var_city.set(row[9])
        self.var_pincode.set(row[10])
        self.var_address.set(row[11])


    def add(self):

        con= sqlite3.connect(database ="RTO.db")
        cur=con.cursor()

        try:
            if self.var_dlllnum.get()=="":
                messagebox.showerror("Error !","DL/LL Number is required", parent = self.root)

            elif self.var_ownernm.get()=="":
                messagebox.showerror("Error !","Owner Name is required", parent = self.root)

            elif self.var_email.get()=="":
                messagebox.showerror("Error !","Email id is required", parent = self.root)

            elif self.var_gender.get()=="":
                messagebox.showerror("Error !","Gender not Selected", parent = self.root)

            elif self.var_dob.get()=="":
                messagebox.showerror("Error !","D.O.B is required", parent = self.root)

            elif self.var_mobile.get()=="":
                messagebox.showerror("Error !","Mobile No is required", parent = self.root)

            elif self.var_vehicleclass.get()=="":
                messagebox.showerror("Error !","Vehicle Class is required", parent = self.root)
                
            elif self.var_validupto.get()=="":
                messagebox.showerror("Error !","Validity Date is required", parent = self.root)
                
            elif self.var_state.get()=="":
                messagebox.showerror("Error !","Resident state is required", parent = self.root)
                
            elif self.var_city.get()=="":
                messagebox.showerror("Error !","Resident city is required", parent = self.root)
                
            elif self.var_pincode.get()=="":
                messagebox.showerror("Error !","Resident pincode is required", parent = self.root)
                
            elif self.var_address.get()=="":
                messagebox.showerror("Error !","Resident address is required", parent = self.root) 
            
            else:
                cur.execute("Select * from Dri_Registration where dlllnum=?",(self.var_dlllnum.get(),))
                row=cur.fetchone()

                if row!=None:
                    messagebox.showerror("Error !","DL/LL Number already exists", parent = self.root)

                else:
                    cur.execute("insert into Dri_Registration(dlllnum,ownernm,gender,dob,vehicleclass,validupto,state,city,pincode,address,mobile,email) values(?,?,?,?,?,?,?,?,?,?,?,?)", (
                        self.var_dlllnum.get(),
                                        self.var_ownernm.get(),
                                        self.var_gender.get(),
                                self.var_dob.get(),
                                self.var_vehicleclass.get(),
                                self.var_validupto.get(),
                                self.var_state.get(),
                                self.var_city.get(),
                                self.var_pincode.get(),
                                self.var_address.get(),
                                self.var_mobile.get(),
                                self.var_email.get(),
                        ))
                    con.commit()
                    messagebox.showinfo("Success","Record Added Successfully !",parent =self.root)
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error !",f"Error due to {str(ex)}")
    
    def show(self):

        con= sqlite3.connect(database ="RTO.db")
        cur=con.cursor()

        try:
            cur.execute("Select * from Dri_Registration")
            rows=cur.fetchall()
            self.DrivingLicenseTable.delete(*self.DrivingLicenseTable.get_children())
            for row in rows:
                self.DrivingLicenseTable.insert('',END,values=row)

            
        except Exception as ex:
            messagebox.showerror("Error !",f"Error due to {str(ex)}")



    def update(self):

        con= sqlite3.connect(database ="RTO.db")
        cur=con.cursor()

        try:
            if self.var_dlllnum.get()=="":
                messagebox.showerror("Error !","DL/LL Number is required", parent = self.root)

            elif self.var_ownernm.get()=="":
                messagebox.showerror("Error !","Owner Name is required", parent = self.root)

            elif self.var_email.get()=="":
                messagebox.showerror("Error !","Email id is required", parent = self.root)

            elif self.var_gender.get()=="":
                messagebox.showerror("Error !","Gender not Selected", parent = self.root)

            elif self.var_dob.get()=="":
                messagebox.showerror("Error !","D.O.B is required", parent = self.root)

            elif self.var_mobile.get()=="":
                messagebox.showerror("Error !","Mobile No is required", parent = self.root)

            elif self.var_vehicleclass.get()=="":
                messagebox.showerror("Error !","Vehicle Class is required", parent = self.root)
                
            elif self.var_validupto.get()=="":
                messagebox.showerror("Error !","Validity Date is required", parent = self.root)
                
            elif self.var_state.get()=="":
                messagebox.showerror("Error !","Resident state is required", parent = self.root)
                
            elif self.var_city.get()=="":
                messagebox.showerror("Error !","Resident city is required", parent = self.root)
                
            elif self.var_pincode.get()=="":
                messagebox.showerror("Error !","Resident pincode is required", parent = self.root)
                
            elif self.var_address.get()=="":
                messagebox.showerror("Error !","Resident address is required", parent = self.root) 
            else:

                cur.execute("Select * from Dri_Registration where dlllnum=?",(self.var_dlllnum.get(),))
                row=cur.fetchone()

                if row==None:
                    messagebox.showerror("Error !","Select the data to be updated from the list", parent = self.root)

                else:
                    cur.execute("update Dri_Registration set ownernm=?,gender=?,dob=?,vehicleclass=?,validupto=?,state=?,city=?,pincode=?,address=?,mobile=?,email=? where dlllnum=?", (
                                self.var_ownernm.get(),
                                self.var_gender.get(),
                                self.var_dob.get(),
                                self.var_vehicleclass.get(),
                                self.var_validupto.get(),
                                self.var_state.get(),
                                self.var_city.get(),
                                self.var_pincode.get(),
                                self.var_address.get(),
                                self.var_mobile.get(),
                                self.var_email.get(),
                                    self.var_dlllnum.get(),
                        ))
                    con.commit()
                    messagebox.showinfo("Success","Record Updated Successfully !",parent =self.root)
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error !",f"Error due to {str(ex)}")

    def delete(self):
        con= sqlite3.connect(database ="RTO.db")
        cur=con.cursor()

        try:
            if self.var_dlllnum.get()=="":
                messagebox.showerror("Error !","DL/LL Number is required", parent = self.root)

            elif self.var_ownernm.get()=="":
                messagebox.showerror("Error !","Owner Name is required", parent = self.root)

            elif self.var_email.get()=="":
                messagebox.showerror("Error !","Email id is required", parent = self.root)

            elif self.var_gender.get()=="":
                messagebox.showerror("Error !","Gender not Selected", parent = self.root)

            elif self.var_dob.get()=="":
                messagebox.showerror("Error !","D.O.B is required", parent = self.root)

            elif self.var_mobile.get()=="":
                messagebox.showerror("Error !","Mobile No is required", parent = self.root)

            elif self.var_vehicleclass.get()=="":
                messagebox.showerror("Error !","Vehicle Class is required", parent = self.root)
                
            elif self.var_validupto.get()=="":
                messagebox.showerror("Error !","Validity Date is required", parent = self.root)
                
            elif self.var_state.get()=="":
                messagebox.showerror("Error !","Resident state is required", parent = self.root)
                
            elif self.var_city.get()=="":
                messagebox.showerror("Error !","Resident city is required", parent = self.root)
                
            elif self.var_pincode.get()=="":
                messagebox.showerror("Error !","Resident pincode is required", parent = self.root)
                
            elif self.var_address.get()=="":
                messagebox.showerror("Error !","Resident address is required", parent = self.root) 

            else:

                cur.execute("Select * from Dri_Registration where dlllnum=?",(self.var_dlllnum.get(),))
                row=cur.fetchone()

                if row==None:
                    messagebox.showerror("Error !","Select the data to be deleted from the list", parent = self.root)

                else:
                    op=messagebox.askyesno("Confirm","Do you want to delete the record",parent= self.root)
                    if op==True:
                        cur.execute("delete from Dri_Registration where dlllnum=?",(self.var_dlllnum.get(),))
                        con.commit()    
                        messagebox.showinfo("Success","Record Deleted Successfully !",parent=self.root)
                        self.clear()

        except Exception as ex:
            messagebox.showerror("Error !",f"Error due to {str(ex)}")

    def search(self):
        con= sqlite3.connect(database ="RTO.db")
        cur=con.cursor()

        try:
            cur.execute(f"Select * from Dri_Registration where dlllnum=?" ,(self.var_dlllnum.get(),))
            rows=cur.fetchone()
            if rows !=None:
                self.DrivingLicenseTable.delete(*self.DrivingLicenseTable.get_children())
                for row in rows:
                    self.DrivingLicenseTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No Record found",parent=self.root)
            
        except Exception as ex:
            messagebox.showerror("Error !",f"Error due to {str(ex)}")


    def clear(self):
        self.show()
        self.txt_dlllnum.config(state='normal')
        self.txt_vehicleclass.config(state='normal')
        self.var_dob.set("")
        self.var_ownernm.set(""),
        self.var_vehicleclass.set("Select C.O.V"),
        self.var_gender.set(""),
        self.var_mobile.set(""),
        self.var_email.set(""),
        self.var_validupto.set("")
        self.var_state.set("")
        self.var_city.set("")
        self.var_pincode.set("")
        self.var_address.set("")
        self.var_search.set("")


root = Tk()
obj = Login(root)
root.mainloop()
