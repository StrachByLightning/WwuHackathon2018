from docFormatter import textProcess
from modelGenerator import modelGenerator
import os
import random

def processAllFiles():
    #go in to resources to grab the list of files
    os.chdir('..')
    os.chdir('resources')

    listOfFiles = open('listOfFiles.txt','r').readlines()

    os.chdir('..')
    os.chdir('bin')

    freqDist ={}
    for f in listOfFiles:
        print(f);
        textProcess(f.replace('\n',''))
        tempDict = modelGenerator()
        keyList = freqDist.keys()

        for t in tempDict.keys():
            if t not in keyList:
                freqDist[t] = tempDict[t]
            else:
                freqDist[t] += tempDict[t]

    generateStory(freqDist)


    ######TESTING#####TESTING######
    test = open('testF.txt','w')
    for e in freqDist:
        test.write(str(e) + '\n')
    ###############################


def generateStory(freqDist):
    allElements = []
    for e in freqDist:
        for i in range(freqDist[e]):
            allElements.append(e)


    storyFile = open('generated_story.txt','w')
    toWrite = ''
    candidate1 = ''
    candidate2 = ''
    candidate3 = ''

    maxParagraphs = 20
    maxWords = 100
    numberOfParagraphs = 0
    numberOfWords = 0

    for i in range(10):
        storyFile.write(str(i+1) + '. ')
        toWrite = random.choice(allElements)
        while(toWrite[0] != '<s>' or toWrite[1] != '<s>'):
            toWrite = random.choice(allElements)
        candidate1 = toWrite[1]
        candidate2 = toWrite[2]
        candidate3 = toWrite[3]
        storyFile.write(toWrite[0] + ' ' + toWrite[1] + ' ' + toWrite[2] + ' '+ toWrite[3] + ' ')
        #### CAN OPTIMIZE THIS, GET THE LIST FIRST THEN RANDOM
        while(toWrite[3] != '</s>' and numberOfWords < maxWords):
            count = 0
            while(toWrite[0] != candidate1 or toWrite[1] != candidate2 or toWrite[2] != candidate3 and count < len(allElements)):
                count+=1
                toWrite = random.choice(allElements)
            if(count >= len(allElements)):
                count = 0
                while(toWrite[1] != candidate2 or toWrite[2] != candidate3 and count < len(allElements)):
                    count+=1
                    toWrite = random.choice(allElements)
                if(count >= len(allElements)):
                    count = 0
                    while(toWrite[2] != candidate3 and count < len(allElements)):
                        count+=1
                        toWrite = random.choice(allElements)
            candidate1 = toWrite[1]
            candidate2 = toWrite[2]
            candidate3 = toWrite[3]
            storyFile.write(toWrite[3] + ' ')
            numberOfWords += 1
        if(candidate3 != '</s>'):
          storyFile.write('</s>\n')
        else:
          storyFile.write('\n')
        numberOfWords = 0




if __name__ == '__main__':
    processAllFiles()
