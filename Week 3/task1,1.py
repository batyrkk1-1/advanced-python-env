import math

def calculate_area():
    print("Choose a shape to calculate area:")
    print("1. Circle")
    print("2. Rectangle")
    print("3. Triangle")
    
    choice = input("Enter your choice (1-3): ")

    if choice == '1':
        radius = float(input("Enter the radius of the circle: "))
        if radius >= 0:
            area = math.pi * radius ** 2
            print(f"Area of the circle: {area:.2f}")
        else:
            print("Radius cannot be negative.")

    elif choice == '2':
        length = float(input("Enter length of the rectangle: "))
        width = float(input("Enter width of the rectangle: "))
        if length >= 0 and width >= 0:
            area = length * width
            print(f"Area of the rectangle: {area:.2f}")
        else:
            print("Dimensions cannot be negative.")

    elif choice == '3':
        base = float(input("Enter base of the triangle: "))
        height = float(input("Enter height of the triangle: "))
        if base >= 0 and height >= 0:
            area = 0.5 * base * height
            print(f"Area of the triangle: {area:.2f}")
        else:
            print("Dimensions cannot be negative.")

    else:
        print("Invalid choice.")

if __name__ == "__main__":
    calculate_area()
