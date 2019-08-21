# lines -> the pattern we want to change
# editline -> the line which we want to replace with

import re

def f_Edit(lines,editline):
    f = open('dict.txt','r+')
    f_content = f.read()
    f_content = re.sub(lines,editline,f_content)
    f.seek(0)
    f.write(f_content)
    f.close()
    
