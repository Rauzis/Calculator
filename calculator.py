class Calculator:
    """
    A simple calculator class to perform basic arithmetic operations.

    This class supports addition, subtraction, multiplication, division, and root operations.

    Attributes:
        current (float): The current value of the calculator. Initialized by assigning value `Calculator(0)`.
        n1 (float): The first operand for the operation.
    """
    def __init__(self, current):
        """
        Initializes the Calculator with an initial number.

        Args:
            current (float or int): The current value of the calculator.
        """
        try:
            self.current = float(current)
        except TypeError:
            print("Invalid Input")
        self.current = current #if current is not None else self.n1

    def __str__(self):
        """
        Returns a string representation of the current value.

        Returns:
            str: The **current** value as a string.
        """
        return f"{self.current}"

    def add(self, n1):
        """Adds given value (n1) to current value.

        Args:
            n1 (float or int): Value to add to current value.

        Returns:
            current (float or int): Total current value after adding n1.
        """
        self.n1 = n1
        self.current = self.current + self.n1
        return self.current

    def sub(self, n1):
        """Subtracts given value (n1) from current value.

        Args:
            n1 (float or int): Value to subtract from current value.

        Returns:
            current (float or int): Total current value after subtracting n1.
        """
        self.n1 = n1
        self.current = self.current - self.n1

    def multi(self, n1):
        """Multiplies current value  by given value (n1).

        Args:
            n1 (float or int): Value that multiplies current value.

        Returns:
            current (float or int): Total current value after multiplying by n1.
        """
        self.n1 = n1
        self.current = self.current * self.n1

    def div(self, n1):
        """Divides current value  by given value (n1).

        Args:
            n1 (float or int): Value that divides current value.

        Returns:
            current (float or int): Total current value after dividing by n1.
        """
        self.n1 = n1
        try:
            if self.n1 == 0:
                print("Can't divide by 0")
            else:
                self.current = self.current / self.n1
        except EOFError: print(self.current)

    def root(self, n1):
        """Takes (n1) root from current value.

        Args:
            n1 (float or int): Value that takes n'th root from current value.

        Returns:
            current (float or int): Total current value after taking n1 root from current.
        """
        self.n1 = n1
        try:
            if self.current < 0:
                print("Can't extract root from negative numbers")
            else:
                self.current = self.current ** (1 / self.n1)
        except EOFError: print(self.current)

    def reset(self):
        """Sets **current** value to zero
        """
        self.current = 0


    

def main():
    calc = Calculator(10)
    while True:
        n = (
            input("+, -, *, / or root (ex.: +20), 'done' to end, 'reset' to restart: ")
            .lower()
            .strip()
        )
        if "+" in n:
            addition(n, calc)
        elif "*" in n:
            multiply(n, calc)
        elif "/" in n:
            divide(n, calc)
        elif "-" in n:
            subtract(n, calc)
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
        n = float(n)
        calc.add(n)
        print(calc)


def subtract(n, calc):
    n = n.replace("-", "").strip()
    if n:
        n = float(n)
        calc.sub(n)
        print(calc)


def multiply(n, calc):
    n = n.replace("*", "").strip()
    if n:
        n = float(n)
        calc.multi(n)
        print(calc)


def divide(n, calc):
    n = n.replace("/", "").strip()
    if n:
        n = float(n)
        calc.div(n)
        print(calc)


def root(n, calc):
    n = n.replace("root", "").strip()
    if n:
        n = float(n)
        calc.root(n)
        print(calc)


def reset(calc):
    calc.reset()
    print(calc)


if __name__ == "__main__":
    main()
