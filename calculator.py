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
            if isinstance(current, (int, float)):
                self.current = current
            else:
                self.current = 0
                print("Invalid input, initialized with 0")

        except EOFError:
            exit

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
        try:
            if isinstance(n1, (int, float)):
                self.n1 = n1
                self.current = self.current + self.n1
            else:
                print("Invalid input")
        except EOFError:
            return self.current

    def sub(self, n1):
        """Subtracts given value (n1) from current value.

        Args:
            n1 (float or int): Value to subtract from current value.

        Returns:
            current (float or int): Total current value after subtracting n1.
        """
        try:
            if isinstance(n1, (int, float)):
                self.n1 = n1
                self.current = self.current - self.n1
            else:
                print("Invalid input")
        except EOFError:
            return self.current

    def multi(self, n1):
        """Multiplies current value  by given value (n1).

        Args:
            n1 (float or int): Value that multiplies current value.

        Returns:
            current (float or int): Total current value after multiplying by n1.
        """
        try:
            if isinstance(n1, (int, float)):
                self.n1 = n1
                self.current = self.current * self.n1
            else:
                print("Invalid input")
        except EOFError:
            return self.current

    def div(self, n1):
        """Divides current value  by given value (n1).

        Args:
            n1 (float or int): Value that divides current value.

        Returns:
            current (float or int): Total current value after dividing by n1.
        """

        try:
            if n1 == 0:
                print("Can't divide by 0")
            elif isinstance(n1, (int, float)):
                self.n1 = n1
                self.current = self.current / self.n1
            else:
                print("Invalid input")
        except EOFError:
            print(self.current)

    def root(self, n1):
        """Takes (n1) root from current value.

        Args:
            n1 (float or int): Value that takes n'th root from current value.

        Returns:
            current (float or int): Total current value after taking n1 root from current.
        """

        try:
            if self.current < 0:
                print("Can't extract root from negative numbers")
            elif isinstance(n1, (int, float)):
                self.n1 = n1
                self.current = self.current ** (1 / self.n1)
            else:
                print("Invalid input")
        except EOFError:
            print(self.current)

    def reset(self):
        """Sets **current** value to zero"""
        self.current = 0
