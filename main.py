def main():
    file_path = "books/frankenstein.txt"
    text = get_book_text(file_path)
    num_words = get_num_words(text)
    num_letters_dict = get_letter_count(text)
    print(f"--- Begin report of {file_path} ---")
    print(f"{num_words} words found in the document")
    sorted_lst = get_output_string(num_letters_dict)
    for s in sorted_lst:
        print(f"The '{s[0]}' character was found {s[1]}")
    print("--- End report ---")

def get_num_words(text):
    # count of the number of words
    words_list = []
    words_list= text.split()
    return len(words_list)

def get_book_text(file_path):
    # with block to open frankenstein file
    with open(file_path) as f:
        return f.read()

def get_letter_count(text):
    # counts the number of unique characters
    num_letters_dict = {}
    lowered_string = text.lower()
    words = lowered_string.split()
    for word in words:
        for i in word:
            if i.isalpha():
                if i in num_letters_dict:
                    num_letters_dict[i] += 1
                else:
                    num_letters_dict[i] = 1
            else:
                pass
    return num_letters_dict

def sort_on(sorted_lst):
    return sorted_lst[1]

def get_output_string(num_letters_dict):
    #returns the report to be printed for the program
    sorted_lst = list(num_letters_dict.items())
    sorted_lst.sort(reverse=True, key=sort_on)
    return sorted_lst

main()

