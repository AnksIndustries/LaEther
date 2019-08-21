import re
import lineWrite as LW

fileDict = dict()
fileDict['word'] = []
fileDict['function'] = []
fileDict['alt'] = []

def lineF(line):
    fileDict = dict()
    fileDict['word'] = []
    fileDict['function'] = []
    fileDict['alt'] = []
    fileDict['word'].append(re.findall('word=([A-Z]+)',line))
    fileDict['function'].append(re.findall('function=(.+ \ *)',line))
    fileDict['alt'].append(re.findall('alt=(.+)',line))
    for keys in fileDict:
        fileDict[keys]=fileDict[keys][0]

    for i in range(len(fileDict['function'])):
        fileDict['function'][i]=fileDict['function'][i].strip()

    return fileDict

def hasWord(word):
    words_in_dict1 = []
    with open('dict1.txt','r+') as dict1:
            for line in dict1:
                dict1_dict = lineF(line)
                words_in_dict1.append(dict1_dict['word'])

    for i in range(len(words_in_dict1)):
        words_in_dict1[i] = words_in_dict1[i][0]
    
    if word in words_in_dict1:
        return True
    else:
        return False
        

def getFunctions(list_of_words):
    Collects = {'words':[],'functions':[]}
    Collects['words'] = list_of_words
    for word in Collects['words']:
        if not hasWord(word):
            newDict = {'word':word,'function':'ASK','alt':''}
            LW.lineW(newDict)
        else:
            with open('dict1.txt','r+') as file:
                for line in file:
                    wordDict=lineF(line)
                    if word in wordDict['word'] or word in wordDict['alt']:
                        Collects['functions'].append(wordDict['function'])
                    else:
                        pass

    flag = 0
    new = {}
    for word in Collects['words']:
        if(flag<len(Collects['functions'])):
            new[word]= Collects['functions'][flag]
        flag += 1

    Collects['functions']=new
    return Collects
