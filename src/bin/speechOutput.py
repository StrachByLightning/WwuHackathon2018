import os

def speechOutput():
    if(os.getcwd()[-3:] != 'bin'):
        os.chdir('bin')

    story = open('generated_story.txt','r')
    final = open('finalOutput.txt','w')

    for line in story:
        wordList = line.split(' ')
        final.write(wordList[4])
        for i in range(5, len(wordList) -2):
            final.write(' ' + wordList[i])
        final.write('\n')

speechOutput()
