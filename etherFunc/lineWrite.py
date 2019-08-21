
def lineW(lineDiction):
    with open('dict1.txt','a+') as file:
        file.write("word=%s function=%s alt=%s\n"%(lineDiction['word'],lineDiction['function'],lineDiction['alt']))
    
