from tkinter import *
from datetime import datetime,date
from tkinter import ttk
import openpyxl
from os import startfile
import os.path
import tkinter as tk
from tkcalendar import DateEntry



root=tk.Tk()

root.geometry("1400x800+0+0" )
root.title("PAYROLL MASTER")


TopFrame=tk.Frame(root,width=1400, height=50,bd=20, padx=0,pady=0, relief='flat')
TopFrame.pack(side=TOP)

toplabel=tk.Label(TopFrame,relief='sunken',width=100,bg='#030407',fg='#986706',justify='center', font=('cambria',26,'bold'),text='PAYROLL ARREARS CALCULATOR').pack()

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
arrears_choice['value']=('','Basic Salary','House Allowance','Commuter Allowance','Hardship Allowance')
arrears_choice.current(0)
arrears_choice.grid(row=0,column=1)

lblwef=tk.Label(form, text='W.E.F', bd=10, justify='right', font=('cambria',12,'bold')).grid(row=1,column=0)
wef_field=DateEntry(form,textvariable=wef, background='#569708', font=('cambria',12),bd=16, width=25).grid(row=1,column=1)

lbl_end_date=tk.Label(form, text='End Date', bd=10, justify='right', font=('cambria',12,'bold')).grid(row=2,column=0)
end_date_field=DateEntry(form,textvariable=end_date,bd=16, background='#569708', font=('cambria',12), width=25).grid(row=2,column=1)

lbl_right_pay=tk.Label(form, text='Right Pay', bd=10, justify='right', font=('cambria',12,'bold')).grid(row=3,column=0)
right_pay_field=tk.Entry(form,textvariable=right_pay, bd=16, font=('cambria',12), width=25).grid(row=3,column=1)

lbl_paid=tk.Label(form, text='Paid Amount', bd=10, justify='right', font=('cambria',12,'bold')).grid(row=4,column=0)
paid_amount_field=tk.Entry(form,textvariable=paid_amount,bd=16, font=('cambria',12),justify='left', width=25).grid(row=4,column=1)




receipt=tk.Text(results, relief='sunken',bd=20,font=('cambria',12,'bold'))
receipt.grid(row=0,column=0)

scroll=tk.Scrollbar(workspace,command=receipt.yview)
scroll.pack(side=RIGHT, fill=Y)

receipt.insert(END, "\n\n\n\n\n\n\n\n")
def calculate():
    rightPay=int(right_pay.get())
    wrongPay=int(paid_amount.get())

    toPay = float(wrongPay - rightPay)
    startdate=datetime.strptime(wef.get(),'%m/%d/%y')
    enddate = datetime.strptime(end_date.get(),'%m/%d/%y')

    nodays=abs(enddate-startdate).days +1

    if(nodays>29):
        d=int(nodays/31)+1
        arrears=d*toPay
    else:
     print(nodays)




    # receipt.insert(END, "\t\t\t\tARREARS\n")
    # receipt.insert(END,"\t\t----------------------------------------------------------------------\n\n")
    receipt.insert(END,"\t\tARREARS TO PAY:\t\t" + arrears_choice.get()+ "for "+ str(nodays)+" Days\n\n")
    receipt.insert(END,"\t\tW.E.F:\t" + wef.get()+"")
    receipt.insert(END, "\t\tEND DATE:\t" + end_date.get() + "\n\n")
    receipt.insert(END,"\t\tRIGHT PAY:\t" + right_pay.get()+"")
    receipt.insert(END,"\t\tAMOUNT PAID:\t" + paid_amount.get()+"\n")
    receipt.insert(END, "\t\t==========================================================\n")
    receipt.insert(END, "\t\t THE OFFICER THEREFORE HAS AN ARREAR OF Kshs. " + str(arrears)+"\n\n")

def clearResult():
    receipt.delete("2.0","end")

btn_calculate=Button(form, text='Calculate', command=calculate, padx=0, pady=1, bd=10,bg='green', fg="black", font=('cambria',12,"bold")).grid(row=5,column=0)

btn_cancel=Button(form, text='Cancel', command=clearResult, padx=0, pady=1, bd=10, bg='red', fg="black", font=('cambria',12,"bold")).grid(row=5,column=1)





root.mainloop()
