import logging  # <--- If you wish to debug (currently unused)
import sys
from even_odd_checker import even_odd
from prime_checker import if_prime
from square_root_checker import SquareRootChecker

# Create a single instance of SquareRootChecker to use in main loop
square = SquareRootChecker()

def menu():
    """Display menu of options to user"""
    options = ["get square root", "check if prime", "even/odd checker", "quit"]
    print("\nMain Menu")
    # Enumerate gives (index, option); start=1 makes it user-friendly
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option.title()}")  # Display each option nicely


def main():
    """
    Runs the main program loop:
    - Shows menu
    - Gets user choice
    - Calls the right checker function
    """
    print("NUMBER ANALYZER")
    while True:
        try:
            menu()
            choice = input("\nEnter an option in range(1,4): ")
            if choice:  # Ensure input isn’t empty
                if choice == "1":
                    square.run()   # Handle square root operations
                elif choice == "2":
                    if_prime()     # Handle prime checking
                elif choice == "3":
                    even_odd()     # Handle even/odd checking
                elif choice == "4":
                    print("Goodbye!")
                    print("\nMADE BY HAASHIRAA")
                    sys.exit()  # Exit program
                else:
                    print("Input out of range!")
            else:
                print("Input is empty!")
        except ValueError:
            # Only triggers if int/float conversion fails inside checker funcs
            print("Oops! Not a number.")
        except KeyboardInterrupt:
            print("\nExiting program...") 
            sys.exit()

if __name__ == "__main__":
    # Run the main loop only if this file is executed directly
    main()
