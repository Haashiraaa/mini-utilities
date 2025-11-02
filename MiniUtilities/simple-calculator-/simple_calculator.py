# simple_calculator.py
"""
Main entry point for the Simple Calculator project.

This script coordinates user interaction (via CalculatorUi),
mathematical operations (via OperatorLogic),
and signature display (via Signature).

It handles the calculator's main loop, menu selection, and result display.
"""

from operator_logic import OperatorLogic
from calculator_ui import CalculatorUi
from maker import Signature
from icecream import ic
import sys
import emoji  # Currently unused but retained in case of future UI improvements

DEBUG = False

# Configure IceCream debugging
if not DEBUG:
    ic.disable()
else:
    ic.enable()


def main():
    """Run the main calculator loop."""
    ol = OperatorLogic()
    ui = CalculatorUi()
    sign = Signature()

    print("Simple Calculator 🔢")

    while True:
        try:
            # Clear previous user inputs before each new operation
            ui.input_values.clear()

            ui.main_menu()
            choice = input("\nEnter an option from 1 to 5\n>>> ").strip()

            if choice == "1":
                ui.get_number()
                ic(ui.input_values)
                ui.last_result = ol.add(ui.input_values)
                ic(ui.last_result)

            elif choice == "2":
                ui.get_number()
                ui.last_result = ol.subtract(ui.input_values)

            elif choice == "3":
                ui.get_number()
                ui.last_result = ol.multiply(ui.input_values)

            elif choice == "4":
                ui.get_number()
                try:
                    ui.last_result = ol.divide(ui.input_values)
                except ZeroDivisionError:
                    print("\nYou can't divide by 0!")

            elif choice == "5":
                print("\nExiting program...")
                sign.print_slowly(sign.sig())
                print("Goodbye!\n")
                sys.exit()

            else:
                print("\nOption is out of range!")
                continue

            print(f"\n= {ui.last_result}")

        except KeyboardInterrupt:
            # Graceful exit on Ctrl+C
            sys.exit()


if __name__ == "__main__":
    main()
