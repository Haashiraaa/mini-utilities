def even_odd():
    """
    Receive user input
    Then check if it is even or odd
    """
    checking_number = True  # Control flag for the while loop
    while checking_number:
        number = input("\nEnter a number (or '0000' to end): ")

        if number:  # Make sure input is not empty
            if number == '0000':  # Sentinel value to stop the loop
                checking_number = False
                print("Exiting even/odd checker.....")
            else:
                # Convert input to float first (to allow decimal input)
                # then to int (to check even/odd)
                num = int(float(number))

                # Even/odd check using modulo operator
                if num % 2 == 0:
                    print(f"Yes! {num} is an even number.")
                else:
                    print(f"{num} is an odd number.")
        else:
            # Handles case when user just presses Enter with no input
            print("Input is empty")