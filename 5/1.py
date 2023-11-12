def spin_words(sentence):
    # Your code goes here
    words = sentence.split()
    reword=[]
    i=0
    for word in words:
        if len(word) >= 5:
            for grapheme in word:
                reword.append(grapheme)
            reword.reverse()
            words[i]="".join(reword)
        reword=[]
        i+=1
    return " ".join(words)
    return None