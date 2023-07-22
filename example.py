class ArithmeticPair:
    """
    Arithmetic operations on a given  pair of numbers

    Args:
        x:
            The first operand.
        y:
            The second operand.
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def sum(self):
        """
        Compute :math:`x + y`.
        """
        print('computing sum!')
        return self.x + self.y

    def difference(self):
        """
        Compute :math:`x - y`.
        """
        print('computing difference')
        return self.y - self.x

    def product(self):
        """
        Compute :math:`x * y`.
        """
        print('computing multiplication')
        return self.x * self.y

    def quotient(self):
        """
        Compute :math:`x / y`.
        """
        print("computing quotient")
        return self.x / self.y
    
