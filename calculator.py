
# The main file should contain a class Calculator that can perform the following actions:

#     Addition / Subtraction.
#     Multiplication / Division.
#     Take (n) root of a number.
#     Reset memory. This means the calculator should perform actions using the value stored
#     in its memory, with memory starting at 0. For example, if the first operation performed
#     is calculator.add(2), the result is 2. If calculator.add(2) is performed again, the result is 4.
#     At this point the value stored in memory is 4. If the calculator memory is then reset,
#     the value stored in memory returns to 0.

class Calculator:
    def __init__(self, n1, n2, current = 0):
        self.current = current
        self.n1 = n1
        self.n2 = n2
        
    def __str__(self):
        return f"{self.current}"

    def add(self):
        self.current = self.n1 + self.n2

    def sub(self):
        self.current = self.n1 - self.n2

    def multi(self):
        self.current = self.n1 * self.n2

    def div(self):
        self.current = self.n1 / self.n2

    def root(self):
        self.current = self.n1, self.n2
        
        #  memory
    @property
    def size(self, current=0):
        self.current = current


    # take user inputs for math and print answers
def main():
    n = input("").strip()
    if "+" in n:
        addition(n)
    elif "-" in n:
        subtract(n)
    elif "*" in n:
        multiply(n)
    elif "/" in n:
        divide(n)
    elif "root" in n:
        root(n)
    else:
        raise ValueError("Bad input")
        
def addition(n):
    num = []
    n = n.split("+")
    for numbers in n:
        num.append(int(numbers))
    calc = Calculator(num[0], num[1])
    calc.add()
    print(calc)

def subtract(n):
    num = []
    n = n.split("-")
    for numbers in n:
        num.append(int(numbers))
    calc = Calculator(num[0], num[1])
    calc.sub()
    print(calc)
        
def multiply(n):
    num = []
    n = n.split("*")
    for numbers in n:
        num.append(int(numbers))
    calc = Calculator(num[0], num[1])
    calc.multi()
    print(calc)
        
def divide(n):
    num = []
    n = n.split("/")
    for numbers in n:
        num.append(int(numbers))
    calc = Calculator(num[0], num[1])
    calc.div()
    print(calc)
        
def root(n):
    num = []
    n = n.split("root")
    for numbers in n:
        num.append(int(numbers))
    calc = Calculator(num[0], num[1])
    calc.root()
    print(calc)
        

if __name__ == "__main__":
    main()