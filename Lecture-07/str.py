def sor_words_in_sentence(sentence):
    words = sentence.split() #spleit การแยกเป็นlist
    print("Original sentence: ", words)
    words.sort(key = str.lower)
    print("Sort: , ",words)
    sort_sentence = ' '.join(words)
    return sort_sentence

sentence = "This is a man world"
sorted_sentence = sor_words_in_sentence(sentence)
print(sorted_sentence)