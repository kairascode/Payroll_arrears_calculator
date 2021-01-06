import os

def saveReceipt(receipt):

    file = os.open('MyFiles/Receipt.doc',os.O_RDWR|os.O_CREAT)
    rec=str.encode(receipt.get("1.0","end"))
    os.write(file,rec)

    os.close(file)

def clearScreen(receipt):
    receipt.delete("2.0", "end")


def daysCalculator(nodays,toPay,daysInMonth):
    if (nodays > 29):  # enable calculation in terms of months
        months = int(nodays / 31) + 1

        arrears = round(float(months * toPay), 2)

        df = round(arrears % 1, 2)

        return arrears
    else:  # enable calculation in terms of days where dates fall within the same month
        ndays = float(nodays / daysInMonth)

        arrears = round(float(ndays * toPay), 2)

        df = round(arrears % 1, 2)

        return arrears

