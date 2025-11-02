def if_prime():
    """Check if a number is a prime number"""
    checking_prime = True
    while checking_prime:
        n = input("\nEnter a number (or '0000' to end): ")
        if n:  # Ensure input isn’t empty
            if n == '0000':  # Exit condition
                checking_prime = False
                print("Exiting prime checker...")
            else:
                num = int(n)  # Convert input; will raise ValueError if invalid
                if num < 2:  # Handle 0, 1, and negatives (not prime)
                    print(f"Nope, {num} is not a prime number.")
                    continue
                # Check divisibility from 2 up to sqrt(num)
                for i in range(2, int(num**0.5) + 1):
                    if num % i == 0:  # Found a divisor, so not prime
                        print(f"Unfortunately, {num} is not a prime number.")
                        break
                else:
                    # The for/else construct: runs only if loop didn't break
                    print(f"Yes! {num} is a prime number.")
        else:
            print("Input is empty!")  # Covers when user just presses Enter