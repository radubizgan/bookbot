def get_book_words(books):
    count = 0
    word = []
    word = books.split()
    for words in word:
        count += 1
    return f"Found {count} total words"

def appearances(books):
    count = 0
    word = ""
    word = books.split()
    result = {}
    for words in word:
        words = words.lower()
        for letter in words:
            if letter not in result:
                result[letter] = 1
            else:
                result[letter] += 1
    return result 

def on_order(dics):
    result = []
    new_res = {}
    for dic in dics:
        new_res["char"] = dic 
        new_res["num"] = dics[dic]
        result.append(new_res) 
        new_res = {}
    def sort_on(items):
        return items["num"]
    result.sort(reverse=True, key=sort_on)
    for results in result:
        if results != "None":
            print(f"{results['char']}: {results['num']}")
    
  

