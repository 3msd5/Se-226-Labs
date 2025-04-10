from string_package import (
    reverse_string,
    capitalize_words,
    remove_punctuation,
    count_characters,
    count_words,
    average_word_length
)

if __name__ == "__main__":
    user_input = input("Enter a sentence: ")

    reversed_str = reverse_string(user_input)
    capitalized_str = capitalize_words(user_input)
    no_punct_str = remove_punctuation(user_input)

    char_count = count_characters(no_punct_str)
    word_count = count_words(no_punct_str)
    avg_word_len = average_word_length(no_punct_str)

    print("\nString Analysis Results:")
    print(f"Reversed: {reversed_str}")
    print(f"Capitalized: {capitalized_str}")
    print(f"Without Punctuation: {no_punct_str}")
    print(f"Character Count: {char_count}")
    print(f"Word Count: {word_count}")
    print(f"Average Word Length: {avg_word_len:.2f}")
