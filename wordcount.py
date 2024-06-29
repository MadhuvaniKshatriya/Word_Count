def count_words(text):
    
    words = text.split()
    
    return len(words)

def main():
    user_input = input("Enter a sentence or paragraph: ")
    word_count = count_words(user_input)
    print(f"The number of words are: {word_count}")

if __name__ == "__main__":
    main()
