import pymysql
class Customer:
    con=pymysql.connect(host="localhost",user="root",password="8755",database="CMS")
    def __init__(self):
        self.id=0
        self.name=""
        self.address=""
        self.mob=""

    def Add_Customer(self):
        myCursor = Customer.con.cursor()
        qry=" insert into CustomerData values(%s,'%s','%s','%s')"%(self.id,self.name,self.address,self.mob)
        myCursor.execute(qry)
        Customer.con.commit()

    def Search_Customer(self):
        myCursor = Customer.con.cursor()
        qry="select * from CustomerData where id=%s"%(self.id)
        rowAffected=myCursor.execute(qry)
        if rowAffected!=0:
            data=myCursor.fetchone()
            self.id=data[0]
            self.name=data[1]
            self.address=data[2]
            self.mob=data[3]

        else:
            raise Exception("Id not found")  # Wrong code handle in Exception Handling
    def Delete_Customer(self):
        myCursor=Customer.con.cursor()
        qry="delete from CustomerData where id = %s"
        rowAffected=myCursor.execute(qry,(self.id))
        if rowAffected!=0:
           Customer.con.commit()

    def Update_Customer(self,id):
        myCursor = Customer.con.cursor()
        qry = "update CustomerData set id = %s ,name = '%s' , address='%s',mob=%'s' where id = %s "
        rowAffected = myCursor.execute(qry,(self.id,self.name,self.address,self.mob))
        if rowAffected != 0:
            data = myCursor.fetchall()
            data[0]= self.id
            data[1]= self.name
            data[2]= self.address
            data[3]= self.mob
        else:
            raise Exception("Id not found")  # Wrong code handle in Exception Handling
    @staticmethod
    def getAlldata():
        myCursor = Customer.con.cursor()
        qry="select * from CustomerData "
        myCursor.execute(qry)
        data=myCursor.fetchall()
        return data






