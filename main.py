def main():
    file_path = "books/frankenstein.txt"
    text = get_book_text(file_path)
    num_words = get_num_words(text)
    num_letters_dict = get_letter_count(text)
    print(f"total word count: {num_words}")
    
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
    # counts the number of letters
    letters_dict = {}
    lowered_string = text.lower()
    words = lowered_string.split()
main()

