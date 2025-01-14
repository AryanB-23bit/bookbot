from pathlib import Path

def open_and_read(path: Path):
    with open(path) as f:
        return f.read()

def word_count(text: str):
    return len(text.split())

def character_count(text: str):
    char_count_dict: dict[str, int] = {}
    for char in text.lower():
        if char in char_count_dict:
            char_count_dict[char] += 1
        else:
            char_count_dict[char] = 1

    return char_count_dict

def gen_text_report(path, count: int, char_count_dict: dict[str, int]):
    print(f'--- Begin report of {path} ---')
    print(f'{count} words found in the document {"\n"}')
    for k, v in sorted(char_count_dict.items(), key=lambda item: item[1], reverse=True ):
        if k.isalpha():
            print(f'The {k} character was found {v} times')
    print('--- End report ---')


if __name__ == "__main__":
    book_path: Path = Path("books/frankenstein.txt")
    book_text = open_and_read(book_path)
    book_word_count = word_count(book_text)
    book_char_count = character_count(book_text)
    gen_text_report(book_path, book_word_count, book_char_count)