# guesses a english word of length more than three spelled with a given set of letters
given_letters = input().split()
length = int(input("length"))

def get_letter_id(letter):
    letters = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(letters)):
        if letters[i] == letter:
            return i 
    return -1
def get_new_words_list(layers:int):
    if layers == 1:
        return set()
    return [get_new_words_list(layers-1) for [] in range(26)]
def put_word_in_words_list(words_list, words_list_layers, word):
    if words_list_layers == 1:
        words_list_layers.add(word)
    put_word_in_words_list(words_list[get_letter_id(word[0])], words_list_layers-1, word[1:len(word)])
def search_word(words_list, words_list_layers, word):
    

all_english_words = get_new_words_list(3)
results = []

with open("./words.txt", "r") as f:
    for l in f.read().splitlines():
        for i in range(len(l)):
            letid = get_letter_id(l[i])
            if letid != -1:
                english_words[]
            