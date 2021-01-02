#//////////////////////////////////////////////////EXCEL SHEET//////////////////////////////////////////////////////////

wb = openpyxl.Workbook()
wb.save(filename='.\MyFiles\calculate.xlsx')


wb = openpyxl.load_workbook('.\MyFiles\calculate.xlsx')

sheet = wb.active

# SET THE STRUCTURE OF THE EXCEL SHEET
def excel():


    sheet.column_dimensions['A'].width = 30
    sheet.column_dimensions['B'].width = 30
    sheet.column_dimensions['C'].width = 30
    sheet.column_dimensions['D'].width = 30
    sheet.column_dimensions['E'].width = 30
    sheet.column_dimensions['E'].width = 30

    sheet.cell(row=1, column=1).value = "ARREARS TO PAY"
    sheet.cell(row=1, column=2).value = "W.E.F"
    sheet.cell(row=1, column=3).value = "TO"
    sheet.cell(row=1, column=4).value = "RIGHT PAY"
    sheet.cell(row=1, column=5).value = "PAID AMOUNT"
    sheet.cell(row=1, column=6).value = "TO PAY"

#EVENT HANDLERS FOR DATA ENTRY WIDGETS
def focus1(event):
    arrears_choice.focus_set()
def focus2(event):
    wef_field.focus_set()
def focus3(event):
    end_date_field.focus_set()
def focus4(event):
    right_pay_field.focus.set()
def focus5(event):
    paid_amount_field.event.focus.set()

#CLEAR CONTENT FROM DATA ENTRY WIDGETS
def clear_content():
    arrears_choice.delete(0,END)
    wef_field.delete(0,"end")
    end_date_field.delete(0,"end")
    right_pay_field.delete(0,"end")
    paid_amount_field.delete(0,"end")

def insert():

    if(arrtype.get()=="" and
       wef.get()=="" and
       end_date.get()
       ==""and
       right_pay.get()==""and
       paid_amount.get()==""):
        print("empty input")
    else:
        current_row=sheet.max_row
        current_column=sheet.max_column
    sheet.cell(row=current_row + 1, column=1).value = arrtype.get()
    sheet.cell(row=current_row + 1,column=2).value=wef.get()
    sheet.cell(row=current_row + 1, column=3).value = end_date.get()
    sheet.cell(row=current_row + 1, column=4).value = right_pay.get()
    sheet.cell(row=current_row + 1, column=5).value = paid_amount.get()

#SAVE WORKBOOK
    wb.save('.\MyFiles\calculate.xlsx')
    # wb.close()

    arrears_choice.focus_set()

    clear_content()
# startfile('.\MyFiles\calculate.xlsx')
# arrears_choice.bind("<Return>",focus1)
# wef_field.bind("<Return>",focus2)
# end_date_field.bind("<Return>",focus3)
# right_pay_field.bind("<Return>",focus4)
# paid_amount_field.bind("<Return>",focus5)

excel()