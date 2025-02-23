
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
    def __init__(self, total=int()):
        self.total = total

    def __str__(self):
        return f"{self.total}"

    def add(self, n):
        n = self.n + n
        self.n = n

    def sub(self, n):
        n = self.n - n
        self.n = n

    def multi(self, n):
        n = self.n * n
        self.n = n

    def div(self, n):
        n = self.n / n
        self.n = n

    @property
    def size(self, current=0):
        self.current = current


    # take user inputs for math and print answers
def main():
    n = input("")
    if "+" in n:
        n1, n2 = n.split("+")
        print(int(n1)+int(n2))
        

if __name__ == "__main__":
    main()