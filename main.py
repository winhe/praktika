from tkinter import *
from tkinter import ttk 
from tkinter.ttk import Combobox

logins = []

def registration():
	log = login.get()
	pas = password.get()
	a = chk_state.get()
	f = open('pl.txt','a')
	f.write(log+'@'+pas+'@'+str(a)+'\n')
	f.close()

def au():
	a = chk_state.get()
	f = open('pl.txt','r')
	lpp = f.read()
	log = login.get()
	pas = password.get()
	lp = lpp[:-1]
	lp = lp.split('\n')
	logpas = log+'@'+pas+'@'+str(a)
	if logpas in lp:
		lbl.configure(text='welcome')
		if a:
			tab_control.tab(tab2,state = 'normal')
		else:
			tab_control.tab(tab3,state = 'normal')
	else:
		lbl.configure(text='Не верно')
	f.close()

	for loginn in lp:
		logins.append(loginn[:loginn.index('@')])

def go():
	f = open('books.txt','a')
	f.write(who.get()+'@'+avtor.get()+'@'+book.get()+'@'+date.get()+'\n')
	f.close()

def wat():
	log = login.get()
	pas = password.get()
	f = open('books.txt','r')
	all_bookss = f.read()
	all_books = all_bookss[:-1]
	all_books = all_books.split('\n')
	my_books = []
	for b in all_books:
		if b[:b.index('@')] == log:
			my_books.append(b[b.index('@')+1:])
	for mb in my_books:
		wa.insert(END,mb)

window = Tk()
window.title("biblioteka")
window.geometry('500x400')

tab_control = ttk.Notebook(window)

tab1 = ttk.Frame(tab_control)  
tab2 = ttk.Frame(tab_control) 
tab3 = ttk.Frame(tab_control)

tab_control.add(tab1, text='Регистрация/Вход')  
tab_control.add(tab2, text='Личный кабинет',state = 'hidden')
tab_control.add(tab3, text='Личный кабинет',state = 'hidden')
# ---------------------------------1
l1 = Label(tab1,text = "login")
l1.grid(column = 0,row = 0)

login = Entry(tab1,width=10,textvariable = 'login')  
login.grid(column=0, row=1)  

l2 = Label(tab1,text = "Password")
l2.grid(column = 1,row = 0)

password = Entry(tab1,width=10)  
password.grid(column=1, row=1) 

btn = Button(tab1, text="Регистрация", command=registration)  
btn.grid(column=2, row=1) 

btn2 = Button(tab1, text="Вход", command=au)  
btn2.grid(column=3, row=1)   

chk_state = BooleanVar() 
chk_state.set(False)
chk = Checkbutton(tab1, text='Администратор', var=chk_state)  
chk.grid(column=4, row=1)  

lbl = Label(tab1, text="")
lbl.grid(column=1, row=3) 

au()
# ---------------------------------2

l3 = Label(tab2,text = 'Кто взял')
l3.grid(column = 0, row = 0)

who = Combobox(tab2)
who['values'] = logins
who.grid(column=0, row=1)  

l4 = Label(tab2,text = 'Автор')
l4.grid(column = 0, row = 2)

avtor = Entry(tab2,width=10)
avtor.grid(column=0, row=3)

l5 = Label(tab2,text = 'Книга')
l5.grid(column = 0, row = 4)

book = Entry(tab2,width=10)
book.grid(column=0, row=5)

l6 = Label(tab2,text = 'Дата')
l6.grid(column = 0, row = 6)

date = Entry(tab2,width=10)
date.grid(column=0, row=7)

btn3 = Button(tab2, text="Занести в бд", command=go)  
btn3.grid(column=0, row=8)   

# --------------------------------3

btn4 = Button(tab3, text="Что я взял?", command=wat)  
btn4.grid(column=0, row=0)  

wa = Listbox(tab3, selectmode = SINGLE,width = 50)
wa.grid(column=0, row=1)

tab_control.pack(expand=1, fill='both') 

window.mainloop()