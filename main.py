def main():
    with open("books/frankenstein.txt") as f:
            file_contents = f.read()

    count_words(file_contents)

def count_words(text):
    list = text.split()
    list_count = len(list)
    #wc = 0
    #for word in list:
    #     wc += 1
    #print(wc)
    print(list_count)
main()