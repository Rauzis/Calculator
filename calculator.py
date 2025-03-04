class Calculator:
    """
    A simple calculator class to perform basic arithmetic operations.

    This class supports addition, subtraction, multiplication, division, and root operations.

    Attributes:
        current (float): The current value of the calculator. Initialized by assigning value `Calculator(0)`.
        n1 (float): The first operand for the operation.
    """

    def __init__(self, current=0):
        """
        Initializes the Calculator with an initial number.

        Initializes with 0 on invalid input.

        Args:
            current (float or int): The current value of the calculator.
        """

        if isinstance(current, (int, float)):
            self.current = current
        else:
            self.current = 0
            print("Invalid input, initialized with 0")

    def __str__(self):
        """
        Returns a string representation of the current value.

        Returns:
            str: The **current** value as a string.
        """
        return f"{(self.current)}"

    def add(self, n1=None):
        """Adds given value (n1) to current value. Defaults to current memory value if None.
            Catch non (float) inputs as error.

        Args:
            n1 (float): Value to add to current value.

        Returns:
            current (float): Total current value after adding n1.
        """

        try:
            if n1 == None:
                self.current += self.current
            elif (float, (n1)):
                self.n1 = float(n1)
                self.current += self.n1
            return self.current
        except ValueError:
            print("Invalid input")

    def sub(self, n1=None):
        """Subtracts given value (n1) from current value. Defaults to 0 if None.
            Catch non (float) inputs as error.

        Args:
            n1 (float): Value to subtract from current value.

        Returns:
            current (float): Total current value after subtracting n1.
        """
        try:
            if n1 == None:
                self.current -= 0
            elif (float, (n1)):
                self.n1 = float(n1)
                self.current -= self.n1
            return self.current
        except ValueError:
            print("Invalid input")

    def multi(self, n1=None):
        """Multiplies current value  by given value (n1). Defaults to current memory value if None.
            Catch non (float) inputs as error.
        Args:
            n1 (float): Value that multiplies current value.

        Returns:
            current (float): Total current value after multiplying by n1.
        """
        try:
            if n1 == None:
                self.current *= self.current
            elif (float, (n1)):
                self.n1 = float(n1)
                self.current *= self.n1
            return self.current
        except ValueError:
            print("Invalid input")

    def div(self, n1=None):
        """Divides current value by given value (n1), can't be 0. Defaults to current memory value if None.
            Catch non (float) inputs as error.
        Args:
            n1 (float): Value that divides current value.

        Returns:
            current (float): Total current value after dividing by n1.
        """

        try:
            if n1 == 0:
                print("Can't divide by 0")
            elif n1 == None:
                if self.current != 0:
                    self.current /= self.current
                    return self.current
                else:
                    print("Can't divide by 0")
            elif (float, (n1)):
                self.n1 = float(n1)
                self.current /= self.n1
                return self.current
        except ValueError:
            print("Invalid input")

    def root(self, n1=None):
        """Takes (n1) root from current value, current value can't be negative. (n1) defaults to 2 if None.
            Catch non (float) inputs as error.
        Args:
            n1 (float): Value that takes n'th root from current value.

        Returns:
            current (float): Total current value after taking n1 root from current.
        """

        try:
            if self.current < 0:
                print("Can't extract root from negative numbers")
            elif n1 == None:
                n1 = 2
                self.current = self.current ** (1 / n1)
                return self.current
            elif n1 == 0:
                print("Invalid input")
            elif float(n1):
                self.current = self.current ** (1 / n1)
                return self.current
        except ValueError:
            print("Invalid input")

    def reset(self, n1=None):
        """Takes (n1) as custom memory reset value, defaults to 0 if None.
            Catch non (float) inputs as error.
        Args:
            n1 (float or int): Value that takes n'th root from current value.

        Returns:
            current (float): Total current value after reset.
        """
        try:
            if n1 == None:
                self.current = 0
            elif float(n1):
                self.current = float(n1)
        except ValueError:
            print("Invalid input")
        return self.current

    def memory(self):
        """Returns current memory value."""
        return self.current
