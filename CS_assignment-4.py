# Q.1
def TowerOfHanoi(n ,sourcepole,destinationpole, auxiliarypole):
	if n==1:                # base case
		print ("Move disk 1 fromsourcepole",sourcepole,"todestinationpole",destinationpole)
		return
	TowerOfHanoi(n-1,sourcepole, auxiliarypole,destinationpole)      # recursive call
	print ("Move disk",n,"fromsourcepole",sourcepole,"todestinationpole",destinationpole)
	TowerOfHanoi(n-1, auxiliarypole,destinationpole,sourcepole)
TowerOfHanoi(3,'pole-A','pole-B','pole-C')


# Q.2

# iterative approach for pascal's triangle
n = int(input("Enter no. of rows to be printed: "))
for i in range(1,n+1):    
    for j in range(0,n-i+1):
        print(' ',end='')
    c = 1
    for k in range(1,i+1):
        print(' ',c,sep='',end='')
        c = (c * (i-k))//k
    print()
    
# recursive approach for pascal's triangle
def pascals_triangle(n):
    if n == 1:
        return [[1]] # base case
    else:
        result = pascals_triangle(n-1) # Recursive call
        current_row = [1]
        previous_row = result[-1] 
        for i in range(len(previous_row)-1):
            current_row.append(previous_row[i] + previous_row[i+1])
        current_row += [1]
        result.append(current_row)
        return result

# to print the series in triangle form and not list form
triangle = pascals_triangle(8)          
n = 8     # for making a well spaced triangle
for row in triangle:
    n = n -1
    row = [" "*(n)] + row 
    for row_element in row:
            print('',row_element,end='')
    print()
        
 
# Q.3

def func1(a,b):
    print(divmod(a,b))
    
    # a)
    print("is the function callable??(True/False) ",callable(func1))  # to check whether function callable or not

    # b)
    if (a or b) == 0:
        print("All values are not non-zero")
    else:
        print("All values are non-zero")

    # c)
    addval_1 = divmod(a,b) + (4,5,6)                 # using filter and lambda function to filter out some elements
    filtered_addval_1 = list(filter(lambda x: x<=4,addval_1))
    print("filtered sequence:-\n",filtered_addval_1)

    # d)
    addval_2 = set(filtered_addval_1)                # converting to set data type
    print("converting to set data type!!1")
    print(addval_2)

    # e)
    addval_3 = frozenset(addval_2)                   # to make the set immutable
    print("Sequence made immutable")

    # f)
    maxnum = max(addval_3)                           # to find max value
    print("Maximum value = ",maxnum )
    print("Hash-value: ",hash(maxnum))


# Q.4
class Student:
    def __init__(self,name,roll_number):             # constructor
        self.name = name
        self.roll_number = roll_number
        print("record created!!!")
    def details(self):                               # function to display records
        print(self.name,self.roll_number)
        print()
    def __del__(self):                               # destructor
        print("record deleted!!!!")
        
record1 = Student("Rahul",21)
record2 = Student("Rohit",22)
record3 = Student("Virat",23)
print()

record1.details()
record2.details()
record3.details()

del record1


# Q.5
class Employee:
    def __init__(self,name,salary):               # constructor
        self.name = name
        self.salary = salary
    def details(self):
        print("record created!!!")
        print(self.name,'\t',self.salary)
        print() 
    def __del__(self):                            # destructor
        print("record deleted!!!")
        
emp1 = Employee("Mehak",40000)
emp1.details()

emp2 = Employee("Ashok",50000)
emp2.details()

emp3 = Employee("Viren",60000)
emp3.details()
# a)
emp1.salary = 70000                              # updating salary of Mehak
print("salary of",emp1.name,"updated!!!")
print(emp1.name,'\t',emp1.salary)

# b)
del emp3


# Q.6
word_george = input("Enter the word George utters: ")
word_barbie = input("enter the word barbie utters: ")

def anagrams(word_george):         # to find all possible anagrams whether meaningfull or not
    if word_george == "":
        return [word_george]
    else:
        ans = []
        for w in anagrams(word_george[1:]):
            for pos in range(len(w)+1):
                ans.append(w[:pos]+word_george[0]+w[pos:])
        return ans
if word_barbie in anagrams(word_george):
    result = input("Is the word uttered by barbie meaningfull???(Y/N)")  # user input to check if the word is meaningfull or not
    if result.upper() == 'Y':
        print("Their friendship is real!!!")
    else:
        print("Their friendship is fake!!!")


 
