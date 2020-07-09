from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
import tkinter.messagebox
from sample import *

HEIGHT=500
WIDTH=550
show_password_flag=False


root=Tk()
root.title("AutonomousUMS")
root.config(background='#540C34')

canvas=Canvas(root,height=HEIGHT,width=WIDTH,relief=GROOVE,bg='#540C34')
canvas.pack()

backgroundImage=PhotoImage(file='bg.png')
showPasswordImage=PhotoImage(file='showPass.png')
unshowPasswordImage=PhotoImage(file='unshowPass.png')




title_frame=Frame(root,bg='#540C34')
title_frame.place(relx=0.07,rely=0,relwidth=0.85,relheight=0.2)

title_frame_content=Label(title_frame,image=backgroundImage,bg='#540C34')
title_frame_content.config(font=("",30))

title_frame_content.place(relx=0,rely=0,relheight=1,relwidth=1)





def loginPage():

	def storeLoginInfo():
		if(len(username_frame_input.get())==16 and len(password_frame_input.get())>0):
			with open("loginInfo.txt",'w') as f1:
				f1.write(username_frame_input.get()+"\n"+password_frame_input.get())
				with open("isLoggedIn.txt",'w') as f2:
					f2.write("true")
			login_frame.destroy()
			disclaimer.destroy()
			subjectSelectionPage()



		else:
			tkinter.messagebox.showerror("Invalid Credentials","Username must contain 16 characters \n and Password field must not be empty.")







	login_frame=Frame(root,bg='white')
	login_frame.place(relwidth=0.5,relheight=0.6,relx=0.25,rely=0.25)

	login_frame_heading=Label(login_frame,text="Login",fg='black',bg="white")
	login_frame_heading.config(font=("",15))
	login_frame_heading.place(relx=0,rely=0,relwidth=1,relheight=0.2)



	enter_username_text=Label(login_frame,text="Enter AUMS Username:",anchor='w',bg='white')
	enter_username_text.config(font=("",10))
	enter_username_text.place(relx=0.1,rely=0.2,relwidth=0.8,relheight=0.15)


	username_frame=Frame(login_frame,bg='white')
	username_frame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.15,)

	username_frame_input=Entry(username_frame,bd=2,width=16,relief=RAISED,justify=CENTER,font=("",11))
	username_frame_input.place(relx=0,rely=0,relwidth=1,relheight=1)

	enter_password_text=Label(login_frame,text="Enter AUMS Password:",anchor='w',bg='white')
	enter_password_text.place(relx=0.1,rely=0.5,relwidth=0.8,relheight=0.15)

	
	password_frame=Frame(login_frame,bg='black')
	password_frame.place(relx=0.1,rely=0.6,relwidth=0.8,relheight=0.15)


	password_frame_input=Entry(password_frame,bd=2,width=16,relief=RAISED,justify=CENTER,show="*",font=("",11))
	password_frame_input.place(relx=0,rely=0,relwidth=1,relheight=1)
	
	

	
	def showpassword():
		global show_password_flag;
		if(show_password_flag==False):
			password_frame_input.config(show="");show_password_flag=True;
			showPassword.config(image=showPasswordImage)
		else:
			password_frame_input.config(show="*");show_password_flag=False
			showPassword.config(image=unshowPasswordImage)



	showPassword=Button(login_frame,image=unshowPasswordImage,anchor=CENTER,command=showpassword,cursor="hand2")
	showPassword.place(relx=0.75,rely=0.65,relwidth=0.09,relheight=0.05)


	submit_button_frame=Frame(login_frame)
	submit_button_frame.place(relx=0.3,rely=0.8,relheight=0.15,relwidth=0.4)

	with open('configuration.txt','r+') as f4:
		submit_button=Button(submit_button_frame,relief=RIDGE,activebackground="#bfff00",bd=3,command=storeLoginInfo,cursor="hand2")
		if(f4.readline()=="false"):
			submit_button.config(text="Configure")
		else:
			submit_button.config(text="Submit")


		submit_button.place(relx=0,rely=0,relheight=1,relwidth=1)



	disclaimer=Label(root,bg='#540C34',fg='#FFDF00',text="You only need to login once,the Username and Password will be used only for logging into AUMS\n through Web Automation, user's privacy is protected.")
	disclaimer.place(relx=0.035,rely=0.9)



def loggout():
	with open("isLoggedIn.txt",'w') as f2:
		f2.write("false")
		loginPage()
	with open("loginInfo.txt",'w') as f3:
		f3.seek(0)
		f3.truncate()	





def subjectSelectionPage():

	with open("loginInfo.txt",'r') as f1:
		username_message_text=Label(root,text="Username: "+str(f1.readline()),bg='#540C34',fg='#FFDF00')
		username_message_text.config(font=("",10))
		username_message_text.place(relx=0.25,rely=0.91)



	def get_dropdown_values():
		subject=subject_dropdown.current()
		action=action_dropdown.current()
		print("Subject selected: "+subject_dropdown.get()+"\n"+"Subject Index: "+str(subject))
		print("Action selected: "+action_dropdown.get()+"\n"+"Action Index: "+str(action))
		intranet(subject,action)



	subject_selection_frame=Frame(root,bg='white')
	subject_selection_frame.place(relwidth=0.5,relheight=0.6,relx=0.25,rely=0.25)

	select_subject_text=Label(subject_selection_frame,text="Select subject:",anchor='w',bg='white')
	select_subject_text.config(font=("",10))
	select_subject_text.place(relx=0.1,rely=0.09,relwidth=0.8,relheight=0.15)

	


	subject_dropdown=Combobox(subject_selection_frame,justify=CENTER,font=("",10),state="readonly",height=20,values=["Linear Algebra Exam","Linear Algebra","Engineering Physics Exam","Engineering Physics","Computer Programming","EEE","EEE Practice","UID","Data Structures","Manufacturing Practice","Cultural Education Exam","UID Exam","Data Structures Exam","Computer Programming Exam","Discreet Mathematics","Cultural Education"])
	subject_dropdown.current(4)
	subject_dropdown.place(relx=0.1,rely=0.2,relwidth=0.8,relheight=0.15)


	select_action_text=Label(subject_selection_frame,text="Select action:",anchor='w',bg='white',font=("",10))
	select_action_text.place(relx=0.1,rely=0.39,relwidth=0.8,relheight=0.15)


	action_dropdown=Combobox(subject_selection_frame,justify=CENTER,font=("",10),values=["Assignments","Online Exams","Gradebook","Resources"],state="readonly")
	action_dropdown.current(0)
	action_dropdown.place(relx=0.1,rely=0.5,relwidth=0.8,relheight=0.15)

	openAUMS_button=Button(subject_selection_frame,text="Open AUMS",relief=RIDGE,activebackground="#bfff00",bd=3,command=get_dropdown_values,cursor="hand2")
	openAUMS_button.place(relx=0.3,rely=0.8,relheight=0.15,relwidth=0.4)

	loggout_button=Button(root,text="Log out",relief=RIDGE,activebackground="white",activeforeground='black',bd=3,cursor="hand2",command=loggout,fg='white',bg='black')
	loggout_button.place(relx=0.65,rely=0.90)


def select_frame():
	with open("isLoggedIn.txt",'r') as f2:
		if(f2.readline()=="false"):
			loginPage()
		else:
			subjectSelectionPage()





if __name__ == '__main__':
	select_frame()
	
	root.mainloop()
    


