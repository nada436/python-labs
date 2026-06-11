#1
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
print(last_name + " " + first_name)

#2
n = input("Enter an integer: ")
nn = n * 2
nnn = n * 3
result = int(n) + int(nn) + int(nnn)
print(result)

#3
print("""a string that you "don't" have to escape 
This 
is a ....... multi-line 
heredoc string --------> example""")

#4
r=6
volume_of_sphere=4/3*3.14*r**3
print(volume_of_sphere) 

#5
base=input("enter base:")    
height=input("enter height:")
area=(base*height)/2
print(area)
print("area of triangle is:",area)   

#6
for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()

for i in range(4, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()


#7
word=input("enter a word:")
print(word[::-1]) 



#8
for i in range(0, 6):
    if i == 3:
        continue
    print(i)


#9
a = 0
b = 1
print(a, b, end=" ") 

for i in range(10):
    c = a + b
    print(c, end=" ")
    a = b
    b = c


#10
str = input("enter a string:")
letter_count = 0
num_count = 0
for i in str:
    if i.isalpha():
        letter_count += 1
    elif i.isdigit():
        num_count += 1 

print("number of letters:", letter_count)
print("number of numbers:", num_count)        
    