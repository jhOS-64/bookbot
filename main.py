def main():
    bookpath = input("Give path like 'books/frankenstein.txt' no quotations: \n")
    text = get_book(bookpath)
    num_words = count_words(text)
    c_count = character_count(text)
    print(f"--- Begin report of {bookpath[6:-4]} ---")
    print(f"{num_words} words found in the document \n")
    for c in dict(sorted(c_count.items(), key=lambda item: item[1], reverse=True)):
        if c.isalpha():
            print(f"The '{c}' was found {c_count[c]} times.")

    print("--- End report ---")

def count_words(text):
    words = text.split()
    return len(words)

def get_book(path):
    with open(path) as f:
        return f.read()

def character_count(text):

    lower_text = text.lower()
    c_count = {}
    for c in lower_text:
        if c in c_count:
            c_count[c] += 1
        else:
            c_count[c] = 1
        
    return c_count

        
main()