def gcd(a, b):
    """Euclid's algorithm to find Greatest Common Divisor"""
    while b:
        a, b = b, a % b
    return a

def subtract_fractions():
    print("Subtraction: Fraction 1 - Fraction 2")
    
    # Input for Fraction 1
    try:
        print("Enter Fraction 1 (A/B):")
        a = int(input("A: "))
        b = int(input("B: "))
        
        print("Enter Fraction 2 (C/D):")
        c = int(input("C: "))
        d = int(input("D: "))

        if b == 0 or d == 0:
            print("Error: Denominator cannot be zero.")
            return

        # Calculate numerator and denominator
        # Formula: (A*D - C*B) / (B*D)
        numerator = (a * d) - (c * b)
        denominator = b * d

        # Handle negative denominators (keep sign in numerator)
        if denominator < 0:
            numerator = -numerator
            denominator = -denominator

        # Simplify fraction using GCD
        # We use absolute value for GCD calculation
        common_divisor = gcd(abs(numerator), denominator)
        
        final_num = numerator // common_divisor
        final_den = denominator // common_divisor

        print(f"\nResult: {final_num}/{final_den}")

    except ValueError:
        print("Invalid input. Please enter integers.")

if __name__ == "__main__":
    subtract_fractions()
