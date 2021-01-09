import tkinter as tk
from calendar import monthlen
from datetime import datetime
from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
from functions.engine import *
from dotenv import load_dotenv
from pathlib import Path

#LOAD APP SETTINGS FROM THE .ENV FILE
env_path=Path('.')/'.env'
load_dotenv(dotenv_path=env_path)



root=tk.Tk()

root.geometry("1400x800+0+0" )
root.title(os.getenv("TITLE"))


TopFrame=tk.Frame(root,width=1400, height=50,bd=20, padx=0,pady=0, relief='flat')
TopFrame.pack(side=TOP)

toplabel=tk.Label(TopFrame,relief='sunken',width=100,bg='#030407',fg='#986706',justify='center', font=('cambria',26,'bold'),text=os.getenv("APPNAME")).pack()

workspace=tk.Frame(root,width=1400, pady=0, relief='sunken', bg='#456479', bd=20)
workspace.pack(side=TOP)

form=tk.Frame(workspace, width=400 , padx=20, pady=80,bg='gray',relief='sunken', bd=15)
form.pack(side=LEFT)

results=tk.Frame(workspace, width=700 ,bg='gray',relief='flat', bd=0)
results.pack(side=RIGHT)

footer=tk.Frame(root, width=1400, height=100, bg='#573402', relief='raise', bd=10)
footer.pack(side=BOTTOM)

#////////////////////////////////////////////////VARIABLES//////////////////////////////////////////////////////////////
arrtype=StringVar()
wef=StringVar()
end_date=StringVar()
paid_amount=StringVar()
right_pay=StringVar()

#////////////////////////////////////////////////FORM///////////////////////////////////////////////////////////////////

lblarrears=tk.Label(form, text='Arrears Type', bd=10,  font=('cambria',12,'bold')).grid(row=0,column=0)

arrears_choice=ttk.Combobox(form, textvariable=arrtype,state='readonly',font=('cambria',12),width=20)
arrears_choice['value']=('','BasicSalary','HouseAllowance','CommuterAllowance','HardshipAllowance')
arrears_choice.current(0)
arrears_choice.grid(row=0,column=1)

#REGISTER VALIDATOR

reg=form.register(myValidator)

lblwef=tk.Label(form, text='W.E.F', bd=10, justify='right', font=('cambria',12,'bold')).grid(row=1,column=0)
wef_field=DateEntry(form,textvariable=wef, background='#569708', font=('cambria',12),bd=16, width=25).grid(row=1,column=1)

lbl_end_date=tk.Label(form, text='End Date', bd=10, justify='right', font=('cambria',12,'bold')).grid(row=2,column=0)
end_date_field=DateEntry(form,textvariable=end_date,bd=16, background='#569708', font=('cambria',12), width=25).grid(row=2,column=1)

lbl_right_pay=tk.Label(form, text='Right Pay', bd=10, justify='right', font=('cambria',12,'bold')).grid(row=3,column=0)
right_pay_field=tk.Entry(form,textvariable=right_pay, bd=16, font=('cambria',12), width=25).grid(row=3,column=1)


lbl_paid=tk.Label(form, text='Paid Amount', bd=10, justify='right', font=('cambria',12,'bold')).grid(row=4,column=0)
paid_amount_field=tk.Entry(form,textvariable=paid_amount,bd=16, font=('cambria',12),justify='left', width=25).grid(row=4,column=1)

receipt=tk.Text(results, relief='sunken', state='normal',  bd=20,font=('cambria',12,'bold'))
receipt.grid(row=0,column=0)

scroll=tk.Scrollbar(workspace,command=receipt.yview)
scroll.pack(side=RIGHT, fill=Y)
receipt.insert(END,"\n\n")#START OF THE RECEIPT FORMATTING TO ALLOW SPACE FOR CAPTURE SHEET HEADING
receipt.insert(END,"\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tARREARS\n\n")
receipt.insert(END,"DESCRIPTION\t\tW.E.F\tEND DATE\t\tRIGHT PAY\t\tAMOUNT PAID\t\tARREARS\t\n")

def calculate():
    rightPay=m_round(float(right_pay.get()),trac=0.5)
    wrongPay=m_round(float(paid_amount.get()),trac=0.5)

    toPay = float(rightPay - wrongPay)
    startdate=datetime.strptime(wef.get(),'%m/%d/%y').date()
    enddate = datetime.strptime(end_date.get(),'%m/%d/%y').date()

    nodays=abs(enddate-startdate).days +1

    daysInMonth = monthlen(enddate.year, enddate.month)


    receipt.insert(END,arrears_choice.get()+"\t\t"+str(startdate)+"\t"+str(enddate)+"\t\t"+str(rightPay)+"\t\t" +str(wrongPay)+"\t\t"+ str(daysCalculator(nodays,toPay,daysInMonth))+"\n")

def genReceipt():
    saveReceipt(receipt)
    openDialog()



btn_calculate=Button(form, text='Calculate', command=calculate, padx=0, pady=1, bd=10,bg='green', fg="black", font=('cambria',12,"bold")).grid(row=5,column=0)

btn_cancel=Button(form, text='SAVE', command=genReceipt, padx=0, pady=1, bd=10, bg='red', fg="black", font=('cambria',12,"bold")).grid(row=5,column=1)





root.mainloop()
