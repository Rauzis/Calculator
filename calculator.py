
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
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
     #   self.current = current

    def __str__(self):
        return f"{self.current}"

    def add(self, n1, n2):
        self.n = n1 + n2

    def sub(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
        self.n = n1 - n2

    def multi(self, n1, n2):
        self.n = n1 * n2

    def div(self, n1, n2):
        self.n = n1 / n2

    def root(self, n1, n2):
        self.n = n1, n2
        
        #  memory
    @property
    def size(self, current=0):
        self.current = current


    # take user inputs for math and print answers
def main():
    n = input("")
    if "+" in n:
        n1, n2 = n.split("+")
        Calculator.add(n1, n2)
    elif "-" in n:
        n1, n2 = n.split("-")
        Calculator.sub(n1, n2)

if __name__ == "__main__":
    main()