'''import keyword
print("Total keywords:",len(keyword.kwlist))
print(keyword.kwlist)
name="vasu"
college="GCEM"
age=20
salary=2500.5
print(type(name))
print(type(college))
print(type(age))
print(type(salary))
a=10
print(float(a))
print(complex(a))
weight=float(input("Enter your weight in kg: "))
if weight>100:
    print("Madhu you are  overweight")
elif weight<100 and weight>90:
    print("madhu you should increase your weight")
elif weight<50 and weight>10:
    print("madhu you are underweight")
else:
     print("bakkodu")'''
class Demo:
    a=10
    b=20
    def __init__(self,c,d):
        self.c=c
        self.d=d
    def display(self):
        print(self.c,self.d)
    def ch_c(self,new):
        self.c=new
    @classmethod
    def disp(cls):
        print(cls.a,cls.b)
    @staticmethod
    def msg():
        print("Public Access specifiers")
user=Demo(10,20)
user.display()
user.ch_c(58)
user.display()        
user.msg()
user.disp()
n=[1,2,3,4,5]
n.remove(2)
n.append(10)
print(n)
print(type(n))
n.extend([20,40])
print(n)
n.insert(1,200)
print(n)