def count_words(text):
    words = text.split()
    return len(words)


def main():
    user_input = input("Enter your text: ")
    total_words = count_words(user_input)

    if total_words == 0:
        print("No words entered.")
    else:
        print(f"Total words: {total_words}")


if __name__ == "__main__":
    main()