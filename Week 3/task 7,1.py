import math

def area_rectangle(length, width):
    """Routine to calculate area of a rectangle"""
    return length * width

def area_right_triangle(leg1, leg2):
    """Routine to calculate area of a right triangle"""
    # A right triangle is exactly half of a rectangle
    return 0.5 * area_rectangle(leg1, leg2)

def area_heron(s1, s2, s3):
    """Calculates area of a general triangle using Heron's Formula"""
    # Semi-perimeter
    p = (s1 + s2 + s3) / 2
    val = p * (p - s1) * (p - s2) * (p - s3)
    
    if val < 0:
        return 0 # Invalid triangle
    return math.sqrt(val)

def main():
    print("Enter the lengths of the 4 sides (X, Y, Z, T).")
    print("Assumption: Angle between X and Y is 90 degrees.")
    
    try:
        x = float(input("X: "))
        y = float(input("Y: "))
        z = float(input("Z: "))
        t = float(input("T: "))

        if any(side <= 0 for side in [x, y, z, t]):
            print("Side lengths must be positive.")
            return

        # 1. Area of the Right Triangle (sides X, Y)
        area1 = area_right_triangle(x, y)

        # 2. Calculate the Diagonal (Hypotenuse of X, Y)
        diagonal = math.sqrt(x**2 + y**2)

        # 3. Area of the second triangle (sides Z, T, Diagonal)
        area2 = area_heron(z, t, diagonal)

        if area2 == 0:
            print("Error: Sides Z, T and the Diagonal cannot form a valid triangle.")
        else:
            total_area = area1 + area2
            print(f"\nDiagonal Length: {diagonal:.2f}")
            print(f"Area of Right Triangle part: {area1:.2f}")
            print(f"Area of General Triangle part: {area2:.2f}")
            print(f"Total Area: {total_area:.2f}")

    except ValueError:
        print("Invalid input. Please enter numbers.")

if __name__ == "__main__":
    main()
