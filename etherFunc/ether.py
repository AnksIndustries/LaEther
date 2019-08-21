import re
import multiprocessing as MP
import json
import fileEdit as FE

class etherProcesses:
    def __init__(self,listOfWords,listOfFunctions):
        #self.etherQuesAns = {}
        #self.functionDictionary = {}
        #with open("etherQuesAns.json",'r') as file:
        #    self.etherQuesAns = json.load(file)
        
        #with open("functionsDef.json",'r') as file:
        #    self.functionDictionary = json.load(file)

        self.listOfWords=listOfWords
        self.listOfFunctions = listOfFunctions

    def etherReply(self):
        
        for word in self.listOfWords:
            if 'ASK' in self.listOfFunctions[word][0]:
                print(self.listOfFunctions[word][0])
              
