with open("books/frankenstein.txt") as f:
    file_contents = f.read()
def count_letters(book_text):
    letters = {}
    text_lower = book_text.lower()
    for letter in text_lower:
        if letter in letters:
            letters[letter] += 1
        elif letter.isalpha():
            letters[letter] = 1
    return letters

def sort_on(dict):
    return dict[list(dict.keys())[0]]

if __name__ == '__main__':
    print("--- Begin report of books/frankenstein.txt ---")
    print(f'{len(file_contents.split())} words found in the document\n')

    letters = count_letters(file_contents)
    split_letters = [{letter:letters[letter]} for letter in letters]
    print("splitting letters")
    print(split_letters)
    print("sorting letters")
    split_letters.sort(reverse=True,key=sort_on )
    for letter_count in split_letters:
        for letter in letter_count:
            print(f'The \'{letter}\' character was found {letter_count[letter]} times.')
    print("--- End report ---")
    # print(letters)