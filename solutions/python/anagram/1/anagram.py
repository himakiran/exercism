def find_anagrams(word, candidates):
    word=word.lower()
    word_list=list(word)
    anagrams=[]
    brk=False
    for each in candidates:
        each1=each.lower()
        if each1==word:
            continue
        each_list=list(each1)
        for chr in each_list:
            try:
                index = word_list.index(chr)
                word_list.pop(index)
            except:
                brk=True
                break

        if brk:
            brk=False
            word_list=list(word)
            continue
        if word_list==[]:
            anagrams.append(each)
            word_list=list(word)
    return anagrams
