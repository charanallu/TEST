print("press 1 to creat details of the patient")
print("press 2 to read details of patient")
print("press 3 to update details of patient")
print("press 4 to retrive particular patient details")
print("press 5 to delete details of particular patient")
print("press 6 to exit")
class Patient:
            def getpatientDetails(self):
                self.name=(input("Enter name of patient : "))
                self.opnumber = input("Enter op number : ")
                self.mobilenumber =int(input("Enter Mobile number : "))
                self.problemtovisit =(input("Enter Problem to visit : "))
                self.lastdateofvisit =(input("Enter Last Date of visit : "))
                self.doctorallocated =(input("Enter the visited doctor name : "))
            def printResult(self):
                print(self.name,self.opnumber, self.mobilenumber,self.problemtovisit,self.lastdateofvisit,self.doctorallocated)
            def get_opnumber(self):
                return self.opnumber
temp=[]
def find(val):
    for i in temp:
        if(i.get_opnumber()==val):
            return i
def retirve():
    for i in temp:
        i.printResult()
def delete(val):
    for i in temp:
        if(i.get_opnumber()==val):
            temp.remove(i)
def modify(val):
    print("----Items to Modify----")
    print("1.mobile number")
    print("2.last date of visit")
    print("3.last visited doctor")
    n=int(input("enter field id  to modify :"))
    for i in temp:
         if(i.get_opnumber()==val):
            new=input("enter new value : ")
            if(n==1):
                i.mobilenumber=int(new)
            elif(n==2):
                i.lastdateofvisit=(new)
            elif(n==3):
                i.problemtovisit=(new)
            else:
                i.doctorallocated=int(new)
            break
for i in range (1,100):
    a=int(input("enter the choice:-"))
    S1=Patient()           
    if a==1:
        S1.getpatientDetails()
        temp.append(S1)
    elif a==2:
            retirve()
    elif a==3:
        val=int(input("enter opnumber to modify :"))
        modify(val)
    elif a==4:
        val=(input('enter opnumber: '))
        st=find(val)
        st.printResult()
    elif a==5:
        val=(input("enter opnumber to delete :"))
        delete(val)
    else:
        break
