def to_octal_code():
    try:
        num = int(input("Enter a non-negative integer: "))
        
        if num < 0:
            print("Please enter a non-negative integer.")
            return

        # Use Python's format string syntax:
        # :010o
        # 0  -> Pad with zeros
        # 10 -> Width of 10 characters
        # o  -> Convert to octal
        octal_code = "{:010o}".format(num)
        
        print(f"Original Decimal: {num}")
        print(f"10-digit Octal:   {octal_code}")
        
    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    to_octal_code()
