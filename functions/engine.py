import os
from tkinter import ttk,  filedialog as filedia
from dotenv import load_dotenv
from pathlib import Path

#LOAD APP SETTINGS FROM THE .ENV FILE
env_path=Path('.')/'.env'

load_dotenv(dotenv_path=env_path)



def openDialog():
    filedia.askopenfilenames(initialdir="./MyFiles")


def saveReceipt(receipt):

    file = os.open(os.getenv("FILENAME"),os.O_RDWR|os.O_CREAT)
    rec=str.encode(receipt.get("1.0","end"))
    os.write(file,rec)

    os.close(file)
    openDialog()


def clearScreen(receipt):
    receipt.delete("2.0", "end")


def daysCalculator(nodays,toPay,daysInMonth):
    if (nodays > 29):  # enable calculation in terms of months
        months = int(nodays / 31) + 1

        arrears = round(float(months * toPay), 2)
        print(arrears)
        return m_round(arrears,trac=0.5)
    else:  # enable calculation in terms of days where dates fall within the same month
        ndays = float(nodays / daysInMonth)

        arrears = round(float(ndays * toPay), 2)

        df = round(arrears % 1, 2)
        print(arrears)

        return m_round(arrears,trac=0.5)


def m_round(amnt,trac=0.05):#ENABLE PRECISION ON CENTS
    getNumber=0.5 if amnt>=0 else -0.5

    print(getNumber)
    return int(amnt/trac+getNumber)*trac

def genTable():
    tree=ttk.Treeview()
    tree["columns"]=("DESCRIPTION","WEF","END_DATE","RIGHT_PAY","PAID","ARREARS")
    tree.column("DESCRIPTION",width=50, anchor=ttk.CENTER)
    tree.column("WEF", width=50, anchor=ttk.CENTER)
    tree.column("END DATE", width=50, anchor=ttk.CENTER)
    tree.column("RIGHT PAY", width=50, anchor=ttk.CENTER)
    tree.column("PAID", width=50, anchor=ttk.CENTER)
    tree.column("ARREARS", width=50, anchor=ttk.CENTER)

    #Assign the heading names to the respective columns
    tree.heading("DESCRIPTION",text="DESCRIPTION", anchor=ttk.CENTER)
    tree.heading("WEF", text="WEF", anchor=ttk.CENTER)
    tree.heading("END_DATE", text="END DATE", anchor=ttk.CENTER)
    tree.heading("RIGHT_PAY", text="RIGHT PAY", anchor=ttk.CENTER)
    tree.heading("PAID", text="PAID", anchor=ttk.CENTER)
    tree.heading("ARREARS", text="ARREARS", anchor=ttk.CENTER)



