import math

# Function to calculate hypotenuse
def get_hypotenuse(leg1, leg2):
    return math.sqrt(leg1**2 + leg2**2)

def main():
    print("--- Triangle 1 ---")
    a1 = float(input("Enter leg 1: "))
    b1 = float(input("Enter leg 2: "))
    hyp1 = get_hypotenuse(a1, b1)

    print("\n--- Triangle 2 ---")
    a2 = float(input("Enter leg 1: "))
    b2 = float(input("Enter leg 2: "))
    hyp2 = get_hypotenuse(a2, b2)

    print(f"\nHypotenuse 1: {hyp1:.2f}")
    print(f"Hypotenuse 2: {hyp2:.2f}")
    print("-" * 20)

    # Compare hypotenuses
    if hyp1 > hyp2:
        print("The first triangle has the larger hypotenuse.")
    elif hyp2 > hyp1:
        print("The second triangle has the larger hypotenuse.")
    else:
        print("Both triangles have equal hypotenuses.")

if __name__ == "__main__":
    main()
