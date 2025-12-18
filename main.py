from stats import get_book_words, appearances, on_order
import sys 

def get_book_text(filepath):
    content = ""
    with open(filepath) as file:
        content = file.read()
    return content 

def main(): 
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    output = get_book_text(sys.argv[1])
    newVar = appearances(output)
    print(
    "============ BOOKBOT ============\n"
    "Analyzing book found at books/frankenstein.txt...\n"
    "----------- Word Count ----------")
    print(get_book_words(output))
    print(
    "--------- Character Count -------")
    print (on_order(newVar))
    print(
    "============= END ===============")



if __name__ == "__main__":
    main()