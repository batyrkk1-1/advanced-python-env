import math

# Subroutine to calculate the area of an equilateral triangle
def triangle_area(side):
    # Area = (sqrt(3) / 4) * side^2
    return (math.sqrt(3) / 4) * (side ** 2)

def main():
    try:
        a = float(input("Enter the side length of the regular hexagon (a): "))
        
        if a >= 0:
            # A hexagon is made of 6 equilateral triangles
            one_triangle = triangle_area(a)
            hexagon_area = 6 * one_triangle
            
            print(f"Area of one triangle: {one_triangle:.2f}")
            print(f"Total area of the hexagon: {hexagon_area:.2f}")
        else:
            print("Side length cannot be negative.")
            
    except ValueError:
        print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
