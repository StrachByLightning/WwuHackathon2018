from sys import argv
from re import search
import os

def textProcess(fileName):
    ## DOING 4-GRAMS => 3 <s>

    ## ADD <s> and </s> TO EACH LINE

    newParaGraph = 0
    previousLine = ''
    start = 0
    os.chdir('..')
    os.chdir('resources')
    story = open(fileName,'r')
    os.chdir('..')
    os.chdir('bin')
    temp = open('temp.txt','w')

    lines = story.readlines()

    for line in lines:
        # first loop, initialize previousLine for second iteration
        if start == 0:
            start = 1
            if len(line.split(' ')) == 0: # if empty line
                continue
            else:
                previousLine += '<s> <s> <s> '
                previousLine += line.replace('\n', '')
                newParaGraph = 0
                continue
        ## write line if end of paragraph
        if(line.split(' ')[0] == '\n'):
            newParaGraph = 1
            if(previousLine != ''):
                temp.write(previousLine + ' </s>\n')
                previousLine = ''
        ## start of paragraph
        else:
            if(newParaGraph == 1):
                #remove lines with no alpha numeric character
                if(search('[a-zA-Z0-9_]',line) == None):
                    continue
                previousLine = ''
                previousLine += '<s> <s> <s> '
                previousLine += line.replace('\n','')
                newParaGraph = 0
            else:
                previousLine += ' '
                previousLine += line.replace('\n','')
    temp.write(previousLine + '</s>\n')

    story.close()
    temp.close()



if __name__ == '__main__':
    textProcess(argv[1])
