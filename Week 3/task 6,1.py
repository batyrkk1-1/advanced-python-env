def gcd(a, b):
    """Euclid's algorithm to find Greatest Common Divisor"""
    while b:
        a, b = b, a % b
    return a

def calculate_gcd_lcm():
    print("Enter two natural numbers:")
    try:
        num1 = int(input("Number 1: "))
        num2 = int(input("Number 2: "))
        
        if num1 <= 0 or num2 <= 0:
            print("Please enter natural numbers (integers > 0).")
            return

        # Calculate GCD
        greatest_divisor = gcd(num1, num2)
        
        # Calculate LCM: (A * B) // GCD
        # We use integer division // because LCM of integers is always an integer
        least_multiple = (num1 * num2) // greatest_divisor
        
        print(f"GCD of {num1} and {num2} is: {greatest_divisor}")
        print(f"LCM of {num1} and {num2} is: {least_multiple}")

    except ValueError:
        print("Invalid input. Please enter integers.")

if __name__ == "__main__":
    calculate_gcd_lcm()
