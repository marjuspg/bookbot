#Developed by Marius Sava
#still_learning :)

['main.py', 'books/frankenstein.txt']
print("Usage: python3 main.py <path_to_book>")
import sys
from stats import count_words
from stats import count_characters
from stats import sort_characters
from stats import print_stats

def get_book_text(filepath):
    with open(filepath, encoding="utf-8") as f:
        return f.read()

def main():
    book_text = get_book_text(sys.argv[1])
    print_stats(book_text)

main()

