def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
        return print("working!")
def letter_count(str):
    words = str.split()
    word_number = 0
    for word in words:
        word_number += 1
    return word_number
def count_characters(book):
    lower_book = book.lower()
    char_set = {}
    for i in range(0, len(book)):
        char = lower_book[i]
        if char not in char_set :
            char_set[char] = 1
        if char in char_set: 
            char_set[char] = 1 + char_set[char]
    return char_set
def report(prev_book_chars,book):
    book_chars = count_characters(prev_book_chars)
    new_list = list(book_chars.items())
    count = letter_count(book)
    print("--- Begin report of book ---")
    print(f"{count} words found in the document")
    for char in new_list:
        if char[0].isalpha() == True:
            letter = char[0]
            number = char[1]
            print(f"The {letter} character was found {number} times")
    print("--- End report ---")
count_characters("Hello World")         
letter_count("Hello World")
report("Hello World","Hello World")
main()