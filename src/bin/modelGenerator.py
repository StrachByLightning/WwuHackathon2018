from nltk import word_tokenize, FreqDist, ngrams

def modelGenerator():
    inputFile = open('temp.txt','r').read().replace('\n', ' ')

    tempListOfTokens = word_tokenize(inputFile, language = 'english')

    listOfTokens = []
    i = 0
    # reconstruct <s> and </s>
    while i < (len(tempListOfTokens)-3):

        # only need to check the 1st 2 the 3rd one must be '>'
        if((tempListOfTokens[i] == '<') and (tempListOfTokens[i+1] == 's')):
            listOfTokens += ['<s>']
            i+=3
        # only need to check the 1st 3 the 4th one must be '>'
        elif((tempListOfTokens[i] == '<') and (tempListOfTokens[i+1] == '/s')):
            listOfTokens += ['</s>']
            i+=3
        else:
            listOfTokens += [tempListOfTokens[i].lower()]
            i+=1

    quadriGram = list(ngrams(listOfTokens, 4))
    quadriGram = [e for e in quadriGram if not ((e[0] == '</s>') or (e[1] == '</s>') or (e[2] == '</s>'))]

    freqDist = FreqDist(quadriGram)

    return freqDist

if __name__ == '__main__':
    modelGenerator()
