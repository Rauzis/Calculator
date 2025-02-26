
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
    def __init__(self, n1, current=0):
        if n1 == "":
            raise ValueError("missing input")
        try:
            self.n1 = float(n1)
        except ValueError:
            print("NaN")
        self.n1 = 0
        self.current = current
        
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
        



def main():
    calc = Calculator(0)
    while True:
        n = input("+, -, *, / or root (ex.: +20), 'done' to end, 'reset' to restart: ").lower().strip()
        if "+" in n:
            addition(n, calc)
        elif "-" in n:
            subtract(n, calc)
        elif "*" in n:
            multiply(n, calc)
        elif "/" in n:
            divide(n, calc)
        elif "root" in n:
            root(n, calc)
        elif "reset" in n:
            reset(calc)
        elif "done" in n:
            print(f"Final: {calc}")
            break
        
def addition(n, calc):
    n = n.replace("+", "").strip()
    if n:
        calc.n1 = float(n)
        calc.add()
        print(calc)
        
def subtract(n, calc):
    n = n.replace("-", "").strip()
    if n:
        calc.n1 = float(n)
        calc.sub()
        print(calc)
        
def multiply(n, calc):
    n = n.replace("*", "").strip()
    if n:
        calc.n1 = float(n)
        calc.multi()
        print(calc)
        
def divide(n, calc):
    n = n.replace("/", "").strip()
    if n:
        calc.n1 = float(n)
        calc.div()
        print(calc)
        
def root(n, calc):
    n = n.replace("root", "").strip()
    if n:
        calc.n1 = float(n)
        calc.root()
        print(calc)

def reset(calc):
    calc.n1 = 0
    calc.multi()
    print(calc)


if __name__ == "__main__":
    main()