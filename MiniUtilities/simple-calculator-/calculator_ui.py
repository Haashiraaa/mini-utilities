"""
calculator_ui.py

This module defines the CalculatorUi class, which manages
user interaction for a simple command-line calculator.
It handles menu display, user input, and reusing previous results.

Author: [Haashiraaa]

"""


class CalculatorUi:
    """
    A class that manages the calculator's user interface (CLI).

    Attributes
    ----------
    input_values : list
        Stores numbers entered by the user for arithmetic operations.
    last_result : float | None
        Stores the result of the previous calculation, if available.
    RESULT : str
        Symbol or command that triggers result display ('=').
    options : list
        List of operation names to display in the main menu.

    Methods
    -------
    main_menu()
        Displays a list of arithmetic operation options.
    use_last_result()
        Asks the user if they want to reuse the previous result.
    get_number()
        Collects numeric inputs from the user until '=' is entered.
    """

    def __init__(self):
        """Initialize UI attributes and available options."""
        self.input_values = []
        self.last_result = None
        self.RESULT = "="
        self.options = [
            'Add➕',
            'Subtract➖',
            'Multiply✖️',
            'Divide➗',
            'Quit🚫'
        ]

    def main_menu(self):
        """Display the calculator's main menu options."""
        print("\nMain Menu")
        for i, option in enumerate(self.options, start=1):
            print(f"{i}. {option}")

    def use_last_result(self):
        """
        Ask the user if they want to reuse their last calculation result.

        If the user agrees, the previous result is added to `input_values`
        so it can be used in the next operation.
        """
        if self.last_result is not None:
            use_last = input(
                f"Do you want to use {self.last_result} as your next number? (y/n) "
            ).lower().strip()

            if use_last == 'y':
                # Allows continued calculations with the previous result.
                self.input_values.append(self.last_result)

    def get_number(self):
        """
        Prompt the user to enter numbers for the selected operation.

        The method collects user inputs until the RESULT symbol ('=') is entered.
        Non-numeric inputs trigger a ValueError message.
        """
        self.use_last_result()
        print(f"\nEnter numbers (enter '{self.RESULT}' to see result)")

        while True:
            number = input("number: ").strip()
            if number == self.RESULT:
                break
            try:
                self.input_values.append(int(number))
            except ValueError:
                print("Oops! Not a valid number ❗")
