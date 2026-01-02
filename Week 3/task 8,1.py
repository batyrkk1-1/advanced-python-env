def check_digits(number):
    """
    Checks if 'number' is divisible by all of its digits.
    Returns True if it is, False otherwise.
    """
    temp = number
    while temp > 0:
        digit = temp % 10
        
        # If digit is 0, we cannot divide by it (undefined), so fail.
        if digit == 0:
            return False
            
        # If number is not divisible by the digit, fail.
        if number % digit != 0:
            return False
            
        temp //= 10 # Move to the next digit
        
    return True

def find_divisible_numbers():
    try:
        n = int(input("Enter natural number n: "))
        
        print(f"Numbers <= {n} divisible by each of their digits:")
        
        results = []
        for i in range(1, n + 1):
            if check_digits(i):
                results.append(i)
        
        # Print results neatly
        print(results)
        
    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    find_divisible_numbers()
