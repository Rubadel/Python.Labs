import random # for random method

""""
# The First Lab

# 1
    print("Hello Python")
    
# 2
x, y, z = 1, 2, 3
print("The summation of there three numbers is", x+y+z)

# 3
a, b = int(input("Enter your first number: \n")), int(input("Enter your second number: \n"))
res = a * b
print("The result of product them is ", res, "\n")

# 4
c1, c2 = 2 + 4j, 3 + 1j
rAdd = c1 + c2
rSub = c1 - c2
print("The result of Adding them is:", rAdd, "\n", "The result of subtract them is:", rSub)

# Second Lab
# 1
print("Enter your line\n")
u = input()

print("Lower case :", u.lower(), "\nUpper case :", u.upper())

# 2
print("Enter Three numbers to get the median\n")
a, b, c = input(), input(), input()

if a < b and a > c:
    m = a
elif b < c and b > a:
    m = b
elif c > a and c < b:
    m = c

print("Median is :", m)

# 3
fn, ln = input("Enter your first name\n"), input("Enter your last name\n")

print(ln[::-1] + " " + fn[::-1])

# 4
s1 = input("Enter first str\n")
s2 = input("Enter second str\n")

print( s1.replace( s1[-1], s2[-1]))
print( s2.replace( s2[-1], s1[-1])) 

# Lab 3
#5
str = input("Enter your string\n")
fr = str[0]
str = str.replace(fr, "$")
res = fr + str[1:]
print(res)

#6
for x in range(6):
    if == 3:
        continue
    print(X)
___________________
def mys(i):
    return lambda a: a * i


x = input("Enter first\n")

b = mys(x)
b(2)
print(" The result is: ", b)
---------------------------

# Lab 4
#1
def rev(string):

    lin = ""

    for i in string:

        lin = i + lin

    return lin

string = input("Enter your string\n")
print(rev(string))

# 2
def string_test(str):

  up, low = 0, 0

  for c in str:

    if c.isupper():

      up += 1

    elif c.islower():

      low += 1

    else:

      pass

  print("No. of Upper case characters : ", up)

  print("No. of Lower case Characters : ", low)

st = input("Enter string")
string_test(st)

# 3
def rep(str):
    fr = str[0]
    str = str.replace(fr, "$")
    res = fr + str[1:]
    print(res)

str = input("Enter your string\n")

rep(str)

# 4
def multi(int):

    num = 1

    for x in list:

       num = num * x

    return num

list=[1,2,3,4]

print(multi(list))

# 5
def uniquelist(l):

 x=[]

 for a in l:

  if a not in x:

   x.append(a)

 return x

print(uniquelist([1,2,2,2,3,4,5]))

output: [1, 2, 3, 4, 5]

# Exercise
Ruba = list(('java','python','c++'))

Ruba.append('c')

print(Ruba)

Ruba.insert(2, 'c#')

print(Ruba)

Ruba.sort()

print(Ruba)

Ruba.copy()

print(Ruba)

Ruba.reverse()

print(Ruba)

Ruba.count( 2 )

print(Ruba)

Ruba.index('java')

print(Ruba)

Ruba.extend('java script')

print(Ruba)

Ruba.remove('java')

print(Ruba)

Ruba.pop(2)

print(Ruba)

Ruba.clear()

print(Ruba)


# Lab 5
#6
def retx(lis, x):

  count = 0

  for i in lis:

    if (i == x):

      count += 1

  return count


list = [1,1,2,2,4,3,3,5,6,6]

x = 3

print(retx(list, x))

# 7
def extst(li,n):
    for i in li:
        if (i==n):
            return "true"

        else:
            return "false"

lis=[1,3,5,7]
n=5
print("Value is here? ",extst(lis,n))


# 1-8
Ruba = list((0,5,5,2,10,4))
print("The List is as:",Ruba)

Rl = Ruba.copy()

Ruba.clear()
print("List now is as:",Ruba)

print("A copy of Ruba list before clear ",Rl)

Ruba.count(5)
Ruba.append(8)
Ruba.index(0)
Ruba.reverse()
print("The sorted list is ", Ruba.sort())

def smallestNUM(list):

  small=0

  for x in list:

    if x<small:

      small=x

  return small

list=[1,-8,2,8,-3]

print("Smallest value in list: ",smallestNUM(list))

# 3

list = ['one' , 'two' , 'third']

for n in list:

   if 3 <  len(n)  :

      print(n)


# 4
lis1 = [0,2,4,6]
lis2 = [0,3,5,7]

for x1 in lis1:
    for x2 in lis2:
        if x1 == x2:
            print(x1)
# 5
listr = [3, 5, 7, 9]
print(random.choice(listr))
"""
# Exercise

Ruba = set(("Hi","I","am","here","Hi"))
Raya = set(("Hi","I","am","not","here","Hi"))

cr = Ruba.copy()
Ruba.add("Hello")
print("The copy of Ruba set is:", cr)
print("The dif in set is:", Ruba.difference("Hi"))
p = Ruba.pop()
print("The poped item is :",p )
Ruba.remove("I")
print(Ruba)
print("intersection is as: ", Ruba.intersection(Raya,Ruba))
print("Union is as: ", Ruba.union(Raya))









