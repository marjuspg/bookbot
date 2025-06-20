#Developed by Marius Sava
#still_learning :)
from stats import count_words
from stats import count_characters
from stats import sort_characters
from stats import print_stats

from stats import print_stats

def get_book_text(filepath):
    with open(filepath, encoding="utf-8") as f:
        return f.read()

def main():
    filepath = "books/frankenstein.txt"
    book_text = get_book_text(filepath)
    print_stats(book_text)

main()

