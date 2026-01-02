import math

def triangle_area(s1, s2, s3):
    """Calculates area of a triangle using Heron's Formula"""
    # Check if a valid triangle can be formed
    if (s1 + s2 > s3) and (s1 + s3 > s2) and (s2 + s3 > s1):
        # Semi-perimeter
        p = (s1 + s2 + s3) / 2
        # Area formula
        return math.sqrt(p * (p - s1) * (p - s2) * (p - s3))
    else:
        return 0  # Invalid triangle

def quadrilateral_area():
    print("Enter the lengths of the 4 sides and the diagonal.")
    print("Assumption: The diagonal connects the vertex between side1/side2 to the opposite vertex.")
    
    try:
        s1 = float(input("Side 1: "))
        s2 = float(input("Side 2: "))
        s3 = float(input("Side 3: "))
        s4 = float(input("Side 4: "))
        diag = float(input("Diagonal: "))

        if any(x <= 0 for x in [s1, s2, s3, s4, diag]):
            print("All lengths must be positive.")
            return

        # Area of first triangle (Side 1, Side 2, Diagonal)
        area1 = triangle_area(s1, s2, diag)
        
        # Area of second triangle (Side 3, Side 4, Diagonal)
        area2 = triangle_area(s3, s4, diag)

        if area1 == 0 or area2 == 0:
            print("Error: The given dimensions cannot form valid triangles.")
        else:
            total_area = area1 + area2
            print(f"\nArea of Triangle 1: {area1:.2f}")
            print(f"Area of Triangle 2: {area2:.2f}")
            print(f"Total Area of Quadrilateral: {total_area:.2f}")

    except ValueError:
        print("Invalid input. Please enter numbers.")

if __name__ == "__main__":
    quadrilateral_area()
