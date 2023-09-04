def main():
    book_path = "books/frankenstein.txt"
    text = get_book_content(book_path)
    number_of_words = get_number_of_words(text)
    characters = get_characters(text)
    character_list = list(characters)
    character_list.sort()
    create_report(book_path, number_of_words, characters, character_list)




def get_book_content(path):
    with open(path, "r") as f:
        return f.read()

def get_number_of_words(text):
    words = text.split()
    return len(words)    

def get_characters(text):
    characters = {}
    for letter in text:
        if letter.isalpha():
            if letter not in characters:
                characters[letter.lower()] = 1
            else:
                characters[letter.lower()] += 1
    return characters

def create_report(book_path, number_of_words, characters, character_list):
    print(f"--- Begin report of {book_path} ---")
    print(f"{number_of_words} words found in the document")
    for char in character_list:
        print(f"{char} was found {characters[char]} times")
    print(f"--- End report ---")




main()