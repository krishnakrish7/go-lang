def rev_sentence(sentence):
    words=sentence.split(' ')
    reverse_sentence=' '.join(reversed(words))
    return reverse_sentence
sentence=input("Enter a string ")
print(rev_sentence(sentence))