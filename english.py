# this is a speech engine based bot which learns and executes all the functions
# present in its library and it is also able to create new functions with the
# unit functions
#
#       (c) Copyrights are reserved, AnksIndustries Pvt. Ltd.


import re                           # for regular expression
import lineFilter as LF             # Filtering Line in file
import lineWrite as LW              # Write in the File
import ether as e
import multiprocessing as MP       # Handle multiple processes



sentance = None
while sentance!='EXIT':
    ExitFlag = False                                        
    sentance = input('Ether 2.0.1 >>> ')         # input from the user
    sentance = sentance.upper()

    if ExitFlag == True:
        #Exit all the processes and send the main process in sleep mode until it
        #is asked to start again
        break
        
    Collect = LF.getFunctions(re.findall("[A-Z]+",sentance))        # tokenizing the sentance and preparing list of functions
    Words = Collect['words']
    Functions = Collect['functions']
    print(Collect)
    
    #etherProc = e.etherProcesses(Words,Functions)
    #etherProc.etherReply()
