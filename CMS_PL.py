# Cms-project-using-my-sql-database-
from tkinter import *
import BLL_CMS_MySql
from tkinter import messagebox
from tkinter import ttk

def btnAddCustomer_click():
    cus=BLL_CMS_MySql.Customer()
    cus.id=varId.get()
    cus.name=varName.get()
    cus.address=varAddress.get()
    cus.mob=varMob.get()
    cus.Add_Customer()
    messagebox.showinfo("My CMS", "Customer Added Successfully")
    varMob.set('')
    varAddress.set('')
    varName.set('')
    varId.set('')
def btnSearchCustomer_click():
    cus=BLL_CMS_MySql.Customer()
    cus.id=varId.get()
    cus.Search_Customer()
    varId.set(cus.id)
    varName.set(cus.name)
    varAddress.set(cus.address)
    varMob.set(cus.mob)
    messagebox.showinfo("Customer Search Successfully")
    varMob.set('')
    varAddress.set('')
    varName.set('')
    varId.set(0)


def btnDeleteCustomer_Click():
    cus=BLL_CMS_MySql.Customer()
    cus.id=varId.get()
    cus.Delete_Customer()
    messagebox.showinfo("Delete Customer Successfully")
    varMob.set('')
    varAddress.set('')
    varName.set('')
    varId.set(0)


def btnModifyCustomer_click():
    id=varId.get()
    cus = BLL_CMS_MySql.Customer()
    cus.id=varId.get()
    cus.name=varName.get()
    cus.address=varAddress.get()
    cus.mob=varMob.get()
    cus.Update_Customer(id)
    messagebox.showinfo("Update Customer Successfully")



def showAllCustomer_click():
    cus=BLL_CMS_MySql.Customer()
    allData=cus.getAlldata()
    root1 = Tk()

    lblId1 = Label(root1, text='Customer Id', font=1, width=15, bg='pink')
    lblId1.grid(row=0, column=0)

    lblIName1 = Label(root1, text='Customer Name', font=1, width=15, bg='pink')
    lblIName1.grid(row=0, column=1)

    lblAddress1 = Label(root1, text='Customer Address', font=1, width=15, bg='pink')
    lblAddress1.grid(row=0, column=2)

    lblmob1 = Label(root1, text='Customer Mobile', font=1, width=15, bg='pink')
    lblmob1.grid(row=0, column=3)

    i = 1
    for id,name,address,mob in allData:
        lblId2 = Label(root1, text=str(id), font=1, width=15, bg='orange')
        lblId2.grid(row=i, column=0)

        lblId2 = Label(root1, text=str(name), font=1, width=15, bg='orange')
        lblId2.grid(row=i, column=1)

        lblId2 = Label(root1, text=str(address), font=1, width=15, bg='orange')
        lblId2.grid(row=i, column=2)

        lblId2 = Label(root1, text=str(mob), font=1, width=15, bg='orange')
        lblId2.grid(row=i, column=3)
        i += 1



root=Tk()
root.geometry('800x200')
root.title("CustomerManagementSystem")


levelId=Label(text='Customer_Id',font=('arial',20,'bold'))
levelId.grid(row=0,column=0)

varId=IntVar()
EnteryId=Entry(textvariable=varId,font=('arial',20,'bold'),bd=20,bg="powder blue")
EnteryId.grid(row=0,column=1)


levelName=Label(text='Customer_Name',font=('arial',20,'bold'))
levelName.grid(row=1,column=0)


varName=StringVar()
EnteryName=Entry(textvariable=varName,font=('arial',20,'bold'),bd=20,bg="powder blue")
EnteryName.grid(row=1,column=1)


levelAddress=Label(text='Customer_Address',font=('arial',20,'bold'))
levelAddress.grid(row=2,column=0)

varAddress=StringVar()
EnteryAddress=Entry(textvariable=varAddress,font=('arial',20,'bold'),bd=20,bg="powder blue")
EnteryAddress.grid(row=2,column=1)


levelMob=Label(text='Customer_Mob',font=('arial',20,'bold'))
levelMob.grid(row=3,column=0)


varMob=StringVar()
EnteryMob=Entry(textvariable=varMob,font=('arial',20,'bold'),bd=20,bg="powder blue")
EnteryMob.grid(row=3,column=1)


btnAddCustomer=Button(root,padx=16,bd=8,fg='black',text='AddCustomer',command=btnAddCustomer_click,font=('arial',20,'bold'))
btnAddCustomer.grid(row=6,column=0)

btnSearch=Button(root,padx=16,bd=8,fg='black',text='SearchCustomer',command=btnSearchCustomer_click,font=('arial',20,'bold'))
btnSearch.grid(row=0,column=2)

btnModifyCustomer=Button(root,padx=16,bd=8,fg='black',text='UpdateCustomer',command=btnModifyCustomer_click,font=('arial',20,'bold'))
btnModifyCustomer.grid(row=6,column=1)

btnDeleteCustomer=Button(root,padx=16,bd=8,fg='red',text='DeleteCustomer',command=btnDeleteCustomer_Click,font=('arial',20,'bold'))
btnDeleteCustomer.grid(row=6,column=2)

btnshowAllCustomer=Button(root,padx=16,bd=8,fg='black',text='ShowALLCustomer',command=showAllCustomer_click,font=('arial',20,'bold'))
btnshowAllCustomer.grid(row=6,column=3)








root.mainloop()
