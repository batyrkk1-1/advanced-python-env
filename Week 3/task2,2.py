def calculate_rectangles():
    # Loop 3 times for 3 rectangles
    for i in range(1, 4):
        print(f"\n--- Rectangle {i} ---")
        try:
            width = float(input(f"Enter side 1 for rectangle {i}: "))
            height = float(input(f"Enter side 2 for rectangle {i}: "))
            
            if width >= 0 and height >= 0:
                area = width * height
                print(f"Area of rectangle {i}: {area:.2f}")
            else:
                print("Sides cannot be negative.")
                
        except ValueError:
            print("Invalid input. Please enter valid numbers.")

if __name__ == "__main__":
    calculate_rectangles()
