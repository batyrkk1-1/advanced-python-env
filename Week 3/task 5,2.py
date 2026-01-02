def print_divisors():
    try:
        num = int(input("Enter a natural number: "))
        
        if num <= 0:
            print("Please enter a positive integer.")
            return

        print(f"Divisors of {num}: ", end="")
        
        # Loop from 1 to num to find divisors
        for i in range(1, num + 1):
            if num % i == 0:
                print(i, end=" ")
        
        print() # Newline at the end

    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    print_divisors()
