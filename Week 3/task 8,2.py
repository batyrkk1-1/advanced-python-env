def swap_ends(arr):
    """
    Procedure to swap the first and last elements of a list.
    Modifies the list in-place.
    """
    if len(arr) < 2:
        return # Nothing to swap if array has 0 or 1 element
    
    # Standard swap logic using a temporary variable conceptualization
    # (Python allows this in one line: a, b = b, a)
    arr[0], arr[-1] = arr[-1], arr[0]

def main():
    try:
        # 1. Enter length of array
        m = int(input("Enter the length of the array (m): "))
        
        if m <= 0:
            print("Array length must be positive.")
            return

        # 2. Enter elements
        print(f"Enter {m} integer elements:")
        A = []
        for i in range(m):
            val = int(input(f"Element {i+1}: "))
            A.append(val)

        # 3. Output original
        print(f"\nOriginal Array:  {A}")

        # 4. Call procedure to swap
        swap_ends(A)

        # 5. Output resulting array
        print(f"Resulting Array: {A}")

    except ValueError:
        print("Invalid input. Please enter integers.")

if __name__ == "__main__":
    main()
