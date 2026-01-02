def analyze_arrays():
    # Define 3 lists of integers
    # Note: Python lists are dynamic, so we don't need to specify size limits manually
    arrays = [
        [5, 10, 15, 20, 25],                  # List 1
        [1, 2, 3, 4, 5, 6, 7, 8],             # List 2
        [100, 200, 300]                       # List 3
    ]

    for i, current_list in enumerate(arrays, 1):
        total_sum = sum(current_list)
        count = len(current_list)
        
        # Avoid division by zero if a list happens to be empty
        if count > 0:
            mean = total_sum / count
        else:
            mean = 0.0

        print(f"Array {i}:")
        print(f"  Sum: {total_sum}")
        print(f"  Arithmetic Mean: {mean:.2f}")
        print("-" * 23)

if __name__ == "__main__":
    analyze_arrays()
