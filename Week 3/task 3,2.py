def sort_letters_in_words():
    text = input("Enter a string: ")
    
    # Split the sentence into a list of words
    words = text.split()
    
    sorted_words = []
    
    for word in words:
        # sorted(word) returns a list of characters, e.g., ['a', 'b', 'c']
        # "".join(...) combines them back into a string
        sorted_word = "".join(sorted(word))
        sorted_words.append(sorted_word)
    
    # Join the processed words back into a single string
    result = " ".join(sorted_words)
    
    print(f"Original: {text}")
    print(f"Modified: {result}")

if __name__ == "__main__":
    sort_letters_in_words()
