import nltk
import os

def getStory():
    print(os.getcwd())
    os.chdir('../resources')

    listOfFiles = open('listOfFiles.txt', 'w')

    texts = nltk.corpus.gutenberg.fileids()

    for text in texts:
        listOfFiles.write('\n' + text)
        current_file = open(text, 'w')
        sent_list = nltk.corpus.gutenberg.sents(text)
        for s in sent_list:
            sentence_string = " ".join(s)
            current_file.write(sentence_string +'\n\n')
