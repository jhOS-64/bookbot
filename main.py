def main():
    bookpath = input("Give path like 'books/bookname.txt' no quotations: \n")
    text = get_book(bookpath)
    num_words =count_words(text)
    print(f"{bookpath[6:-4]} has {num_words} words in it!")
def count_words(text):
    words = text.split()
    return len(words)

def get_book(path):
    with open(path) as f:
        return f.read()
        
main()