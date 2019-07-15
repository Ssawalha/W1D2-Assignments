def word_stats(file,numword):
    worddict = {}
    maxdict ={}
    with open(file,"r") as f:
        for line in f:
            for word in line.split():
                if word in worddict:
                    worddict[word] += 1
                else: 
                    worddict[word] = 1
    maxvalues = sorted(worddict.values(), reverse = True)
    indval = 0
    for key in worddict:
        if worddict[key] in maxvalues[0:numword]:
            maxdict[key] = maxvalues[indval]
            indval += 1
    print (maxdict)

word_stats("article.txt",3)