#1
class Strings:
    def __init__(self, getString):
        self.getString = getString
    def printString(self):
        return self.getString.upper()
        
s = Strings(input())
print(s.printString())

#2
class Shape:
    def __init__(self, area):
        self.idea = 0

class Square(Shape):
    def __init__(self, length):
        self.length = length
        super().__init__(area)
    def area(self):
        return self.length * self.length
    
#3
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
#4
class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, money):
        self.balance += money
        print("+ Deposit")

    def withdraw(self, money):
        if money > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= money
            print("- Withdrawal")

#5
numbers = list(map(int, input().split()))

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True
primes = list(filter(lambda x: is_prime(x), numbers))
print(primes)