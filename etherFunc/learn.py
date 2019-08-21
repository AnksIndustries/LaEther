import json

class learning:

    def __init__(self,type_of_action):
        self.TOA = type_of_action

    def revert(self):
        type_of_action=None
    
    def learnit(self,question):
        if self.TOA == 0:
            text = None
            while(len(text)==0):
                text=input('Please tell me the answer >>> ')
                if len(text)!=0:
                    with open('QAether.json','a+') as QAetherFile:
                        QAether = json.load(QAetherFile)
                        QAether[question]=text
                        json.dump(QAether,QAetherFile)
                        print('Updated!')
                elif "Crevert" in text:
                    self.revert()
                    break
                else:
                    print('Please type "Crevert" to revert learning or type any answer')
        elif self.TOA == 1:
            
