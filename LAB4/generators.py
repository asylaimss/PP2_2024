#1
def val():
    l = list()
    for i in range(0,int(input())):
        l.append(i**2)
        print(l)     
val()

#2
n = int(input())
for i in range(0, n + 1, 2):
        if i < n - 1:
            print(i, end = ",")
        else:
            print(i)

#3
def even(n):
 for i in range(0, n+1):
     if i % 12 == 0:    # 3*4 = 12
        yield i

n=int(input())
l = list()
for i in even(n):
    l.append(str(i))
print(l, sep = ",")

#4
def squares(a,b):
    while a <= b:
        yield a*a
        a += 1
        
for i in squares(a = int(input()), b = int(input())):
    print(i, end = " ")
        
#5
def all(n):
    while n >= 0:
        yield n
        n -= 1
for i in all(n = int(input())):
    print(i, end = " ")