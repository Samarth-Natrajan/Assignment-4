'''# Q.2
n = int(input("Enter no. of rows to be printed: "))
# iterative approach for pascal's triangle
for i in range(1,n+1):    
    for j in range(0,n-i+1):
        print(' ',end='')
    c = 1
    for k in range(1,i+1):
        print(' ',c,sep='',end='')
        c = (c * (i-k))//k
    print()
    

 
# Q.3
global a , b
def func1(a,b):
    print(divmod(a,b))

    
print("is the function?? -  ",func1)
# b)
if (a or b) == 0:
    print("All values are not non-zero")
else:
    print("All values are non-zero")
# c)
addval1 = divmod(a,b) + (4,5,6)
filtered_addval1 = filter(lambda x: x<=4,addval1)
print(filtered_addval)
# d)
addval2 = set(filtered_addval1)
print(addval2)
# e)
addval3 = froenset(addval2)
'''

# Q.4
class student:
    def __init__(self,name,roll_number):
        self.name = name
        self.roll_number = roll_number
        print("record created!!!")
    def details(self):
        print(self.name,self.roll_number)
        print()
    def __del__(self):
        print("record deleted!!!!")
record1 = student("Rahul",21)
record2 = student("Anjali",22)
record3 = student("Virat",23)
print()
record1.details()
record2.details()
record3.details()

del record1


        
        
        
