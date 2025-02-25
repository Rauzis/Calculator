
# The main file should contain a class Calculator that can perform the following actions:

#     Addition / Subtraction.
#     Multiplication / Division.
#     Take (n) root of a number.
#     Reset memory. This means the calculator should perform actions using the value stored
#     in its memory, with memory starting at 0. For example, if the first operation performed
#     is calculator.add(2), the result is 2. If calculator.add(2) is performed again, the result is 4.
#     At this point the value stored in memory is 4. If the calculator memory is then reset,
#     the value stored in memory returns to 0.
import numpy as np


class Calculator:
    def __init__(self, n1, current = 0):
        self.current = current
        self.n1 = n1
        
    def __str__(self):
        return f"{self.current}"

    def add(self):
        self.current = self.current + self.n1

    def sub(self):
        self.current = self.current - self.n1

    def multi(self):
        self.current = self.current * self.n1

    def div(self):
        self.current = self.current / self.n1

    def root(self):
        self.current = self.current ** (1 / 2)
        
        #  memory
    @property
    def size(self, current=0):
        self.current = current


    # take user inputs for math and print answers
def main():
    
    while True:
        n = input("").strip()
        if "+" in n:
            addition(n)
            continue
        else:
            raise ValueError("Bad input")
        
def addition(n):
    n = n.replace("+", "")
    n = int(n)
    calc = Calculator(n)
    calc.add()
    print(calc)


if __name__ == "__main__":
    main()