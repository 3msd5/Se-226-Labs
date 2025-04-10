import string

def reverse_string(s):
    return s[::-1]

def capitalize_words(s):
    return s.title()

def remove_punctuation(s):
    return s.translate(str.maketrans("", "", string.punctuation))

if __name__ == "__main__":
    test_str = "muhammed!# sait Dokur#"
    print(reverse_string(test_str))
    print(capitalize_words(test_str))
    print(remove_punctuation(test_str))
