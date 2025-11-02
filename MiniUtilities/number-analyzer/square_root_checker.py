import math


class SquareRootChecker:
    """Class to calculate and display square roots."""

    def float_square_root(self, n):
        """Return float (precise decimal) square root of n."""
        return math.sqrt(n)  # Always returns a float, even for perfect squares

    def round_square_root(self, n):
        """Return square root of n rounded to 2 significant figures."""
        return round(math.sqrt(n), 2)

    def int_square_root(self, n):
        """
        Return integer-rounded square root of n.

        Uses round() instead of int() to avoid truncation:
        - int() simply drops the decimal part (flooring the value)
        - round() gives a fairer integer by rounding up when >= .5
        """
        return round(math.sqrt(n))

    def square_root(self, n):
        """Display all square root variations for a given number."""
        decimal_value = self.float_square_root(n)  # Exact float value
        rounded_value = self.round_square_root(n)  # Rounded to 2 s.f
        int_value = self.int_square_root(n)        # Rounded to nearest int

        # Display results clearly
        print(f"Square root (decimal): {decimal_value}")
        print(f"Rounded square root (2 s.f): {rounded_value}")
        print(f"Integer-rounded square root: {int_value}")

    def run(self):
        """Loop to handle user input for square root checking."""
        checking_root = True
        while checking_root:
            number = input("\nEnter a number (or '00' to end): ")
            if number:  # Ensure input isn’t empty
                if number == '00':  # Exit condition
                    checking_root = False
                    print("Exiting square root checker...")
                else:
                    try:
                        num = float(number)  # Convert input safely
                        self.square_root(num)
                    except ValueError:  # Handle invalid numeric input
                        print("Oops! That's not a number.")
            else:
                print("Input is empty!")  # Handle Enter with no value
