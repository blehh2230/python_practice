class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def average(self):
        sum=0
        for i in self.marks:
            sum+=i 
        return sum/3

name=input("Enter the name of the student")
marks=list(map(int,input("enter the 3 subject marks").split()))
a=student(name,marks)
print("the average marks is:",a.average())