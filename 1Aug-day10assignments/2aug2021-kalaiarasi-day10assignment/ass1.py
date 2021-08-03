empdic={}
from os import name
import re,collections,time
def getdatetime():
    ti=time.localtime()
    currentime=time.strftime("%Y-%m-%d %H:%M:%S ",ti)
    return currentime
def addEmployee():
    id=input("enter the id :")
    name=input("enter the name: ")
    designation=input("enter the Designation: ")
    salary=input("Enter the salary :")
    address=input("Enter the address : ")
    pincode=input("Enter the pincode : ")
    timedate1=getdatetime()
    dict1={"id":id,"name":name,"designation":designation,"salary":salary,"address":address,"pincode":pincode,'addedOn':timedate1}
    return dict1
def validatation(dict1):
    vname=re.search("[A-Z]{1}[^A-Z]{0,25}$",dict1["name"])
    vsalary=re.search("[0-9]{0,7}$",dict1["salary"])
    vpincode=re.search("(^6)[0-9]{5}$",dict1["pincode"])
    if vname and vsalary and vpincode:
        return True
    else:
        return False

while(1):
    print("1. add emplyee")
    print("2. view employee")
    print("3. salary")
    print("4. exit")
    choice=int(input("Enter your choice :"))
    if choice==1:
        a=addEmployee()
        if validatation(a):
            if len(empdic)==0:
                empdic=collections.ChainMap(a)
            else:
                empdic=empdic.new_child(a)
    if choice==2:
        print(empdic.maps)
    if choice==3:
        s=int(input("Enter the Salary : "))
        for i in empdic.maps:
            if (i['salary'])>=s:
                print(i)
    if choice==4:
        break
