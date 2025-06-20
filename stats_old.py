#Count word function
def count_words(text):
    words = text.split()
    return len(words)

#Converion of characters

def count_characters(text):
    text = text.lower()
    char_counts = {}
    
    for char in text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    return char_counts

def sort_characters(char_counts):
    sorted_list = [{"char": char, "num": count} for char, count in char_counts.items()]
    sorted_list.sort(key=lambda x: x["num"], reverse=True)
    return sorted_list

def print_stats(text):
    print(f"Found {count_words(text)} total words")
    char_counts = count_characters(text)
    print(f"e: {char_counts.get('e','0')}")
    print(f"t: {char_counts.get('t','0')}")
