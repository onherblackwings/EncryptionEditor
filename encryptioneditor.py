import Tkinter
from Tkinter import *
from ScrolledText import *
import tkFileDialog #dialog box for saving files
import tkMessageBox
import binascii
import base64
import os
from random import shuffle
from random import randint
from Crypto.Cipher import AES



first_rule='!A?E(F&H@I1K3L5M7N9T:V+W/X[YZBCDGJOPQRSU.a,e)f#hi2k4l6m8n0t;v=w-x]yzbcdgjopqrsu ' #list all letters w/o curves first
even=[]
odd=[]
c=0
while c<len(first_rule):
    if c%2!=0:
        odd.append(first_rule[c])
        c+=1
    elif c%2==0:
        even.append(first_rule[c])
        c+=1
    else:
        c+=1
second_rule=''.join(odd+even)


root = Tkinter.Tk(className="NestorEdit v1.0")
textPad = ScrolledText(root, width=100, height=80)
textPad.focus_set()
def new_file():
	textPad.delete('1.0', END)
	


def open_file():
	file=tkFileDialog.askopenfile(parent=root, mode='rb', filetypes=[("Python", "*.py"), ("Plain Text", "*.txt"), ("All Files", "*.*") ], title="Select a file")
	if file != None:
		contents=file.read()
		textPad.insert('1.0', contents)
		file.close()

def save_file():
	'''file=open("README.txt",'rb')
	file_read=file.read()
	print file_read
	file.close()'''
	file=tkFileDialog.asksaveasfile(mode='w', filetypes=[("Python", "*.py"), ("Plain Text", "*.txt"), ("All Files", "*.*") ])
	if file != None:
		data=textPad.get('1.0', END+' -1c')
		
		file.write(data)
		file.close()

def exit_editor():
	if tkMessageBox.askokcancel("Quit", "Do you really want to quit?"):
		root.destroy()

def about_menu():
	tkMessageBox.showinfo("About", "Just Another Text Editor \n Copyright 2016")

def rule_map_cipher():
	data=textPad.get('1.0', END+' -1c')
	cipher=''
	for i in data:
		if i in  first_rule:
			num=first_rule.find(i)
			cipher=cipher+second_rule[num]
		else:
			cipher=cipher+i
	textPad.delete('1.0', END)		
	textPad.insert('1.0', cipher)
			
def rule_map_decipher():
	data=textPad.get('1.0', END+' -1c')
	decipher=''
	for i in data:
		if i in second_rule:
			num=second_rule.find(i)
			decipher=decipher+first_rule[num]
		else:
			decipher=decipher+i	
	
	textPad.delete('1.0', END)
	textPad.insert('1.0', decipher)
		
def email_menu():
	var=''
	var2=''
	var3=''
	var4=''
	email = Tkinter.Tk(className="Email Menu")
	entry1=Entry(email, width=25)
	entry2=Entry(email, width=25)
	
	#entry1.insert(10,0)
	#entry2.insert(10,0)
	label1=Label(email, text="Your Email").grid(row=0, column=0)
	entry1.grid(row=1, column=0)
	label2=Label(email, text="Recipient Email").grid(row=2, column=0)
	entry2.grid(row=3, column=0)
	#label3=Label(email, text="Gmail").grid(row=4,column=0)
	Rbutton1=Radiobutton(email, text="Google", variable=var, value='smtp.gmail.com')
	Rbutton1.grid(row=0, column=1)
	Rbutton2=Radiobutton(email, text="Outlook", variable=var2, value='smtp-mail.outlook.com')
	Rbutton2.grid(row=1, column=1)
	Rbutton3=Radiobutton(email, text="Yahoo", variable=var3, value='smtp.mail.yahoo.com')
	Rbutton3.grid(row=2, column=1)
	Rbutton4=Radiobutton(email, text="Icloud", variable=var4, value='smtp.mail.me.com')
	Rbutton4.grid(row=3, column=1)
	Button(email, text="SEND", width=25, command='').grid(row=4,column=0)
	Button(email, text="Quit", width=10, command='').grid(row=4,column=1)
	email.mainloop()





#Initialize menu
menu=Menu(root)
root.config(menu=menu)

#create a cascade
filemenu=Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=new_file)
filemenu.add_command(label="Open", command=open_file)
filemenu.add_command(label="Save", command=save_file) #add selections to cascade
filemenu.add_separator()
filemenu.add_command(label="Exit", command=exit_editor)
#end of first cascade
encryptmenu=Menu(menu)
menu.add_cascade(label="Encrypt/Decrypt", menu=encryptmenu)
encryptmenu.add_command(label="Encrypt" ,command=rule_map_cipher)
encryptmenu.add_command(label="Decrypt", command=rule_map_decipher)

emailmenu=Menu(menu)
menu.add_cascade(label="Email", menu=emailmenu)
emailmenu.add_command(label="Send as Email", command=email_menu)

helpmenu=Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About", command=about_menu)



textPad.pack()
root.mainloop()
