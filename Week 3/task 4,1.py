def gcd(a, b):
    """Euclid's algorithm to find Greatest Common Divisor"""
    while b:
        a, b = b, a % b
    return a

def divide_fractions():
    print("Enter Fraction 1 (A/B):")
    a = int(input("A: "))
    b = int(input("B: "))
    
    print("Enter Fraction 2 (C/D):")
    c = int(input("C: "))
    d = int(input("D: "))

    if b == 0 or d == 0 or c == 0:
        print("Error: Denominator (or divisor numerator) cannot be zero.")
        return

    # Division rule: (A/B) / (C/D) = (A*D) / (B*C)
    numerator = a * d
    denominator = b * c

    # Simplify fraction
    common_divisor = gcd(numerator, denominator)
    final_num = numerator // common_divisor
    final_den = denominator // common_divisor

    print(f"\nResult: {final_num}/{final_den}")

if __name__ == "__main__":
    divide_fractions()
