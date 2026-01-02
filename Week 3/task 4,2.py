# Procedure to check if a single point is inside the circle
def is_inside(px, py, cx, cy, radius_sq):
    # Calculate squared distance from center
    dist_sq = (px - cx)**2 + (py - cy)**2
    return dist_sq < radius_sq

def main():
    print("Enter Circle parameters:")
    xa = float(input("Center X (xa): "))
    yb = float(input("Center Y (yb): "))
    r = float(input("Radius (R): "))
    r_squared = r**2

    # List of points to check: P, F, L
    points = []
    
    print("\nEnter Point P coordinates:")
    points.append(('P', float(input("p1: ")), float(input("p2: "))))
    
    print("Enter Point F coordinates:")
    points.append(('F', float(input("f1: ")), float(input("f2: "))))
    
    print("Enter Point L coordinates:")
    points.append(('L', float(input("l1: ")), float(input("l2: "))))

    count = 0
    print("\nResults:")
    for name, x, y in points:
        if is_inside(x, y, xa, yb, r_squared):
            print(f"Point {name}({x}, {y}) is INSIDE.")
            count += 1
        else:
            print(f"Point {name}({x}, {y}) is NOT inside.")

    print(f"\nTotal points inside the circle: {count}")

if __name__ == "__main__":
    main()
