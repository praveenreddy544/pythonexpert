import os
#print('data is this')

class FirstTest:
    def m(self):
        self.a=int(input("Enter no: "))
        self.b=(self.a*self.a)
        print(f"b value is {self.b}")

'''a=FirstTest()
a.m()'''


def takeinp(a):
    print(f"first no is {a[0]}")

'''b=[1213,2,3]
takeinp(b)'''

if __name__ == "__main__":
    a=FirstTest()
    a.m()
    b=[1213,2,3]
    takeinp(b)   