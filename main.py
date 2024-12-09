def main():
    bookpath = input("Give path like 'books/frankenstein.txt' no quotations: \n")
    text = get_book(bookpath)
    num_words = count_words(text)
    c_count = character_count(text)
    print(f"{bookpath[6:-4]} has {num_words} words in it!")
    print(c_count)

def count_words(text):
    words = text.split()
    return len(words)

def get_book(path):
    with open(path) as f:
        return f.read()

def character_count(text):

    characters = text.lower()
    c_count = {}
    for c in characters:
        if c in c_count:
            c_count[c] = c_count[c] + 1
        else:
            c_count[c] = 1
        
    return c_count

        
main()