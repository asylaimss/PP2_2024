#1
import re
f = open('row.txt', 'r', encoding = "utf8")     # исправить ошибку r
def text_match(txt):
    pat = 'ab*?'
    if re.search(pat, txt): 
        return True
    else:
        return False    
     
x = True
while x:
    f_line = f.readline()
    if text_match(f_line):
        print(f_line)
    if not f_line:
        print("not such file or end file")
        x = False
f.close()

#2
import re
f = open('row.txt', 'r', encoding = "utf8") 
def text_match(txt):
    pat = 'аб*?'
    if re.search(pat, txt):
        return True
    else:
        return False 
    
x = True
while x:
    f_line = f.readline()
    if text_match(f_line):
        print(f_line)
    if not f_line:
        print("Not matched!")
        x = False
f.close()

#3
import re
f = open('row.txt', encoding = "utf8") 
def text_match(txt):
    pat = '^[а-я]+_[а-я]+$'
    if re.search(pat, txt):
        return True
    else:
        return False 
    
x = True
while x:
    f_line = f.readline()
    if text_match(f_line):
        print(f_line)
    if not f_line:
        print("Not matched!")
        x = False
f.close()
    
#4
import re
f = open('row.txt', encoding = "utf8") 
def text_match(txt):
    pat = '[А-Я]+[а-я]+$'
    if re.search(pat, txt):
        return True
    else:
        return False 
    
x = True
while x:
    f_line = f.readline()
    if text_match(f_line):
        print(f_line)
    if not f_line:
        print("Not matched!")
        x = False
f.close()

#5
import re
f = open('row.txt','r', encoding = "utf8") 
def text_match(txt):
    pat = 'а.*?б$'
    if re.search(pat, txt):
        return True
    else:
        return False 
    
x = True
while x:
    f_line = f.readline()
    if text_match(f_line):
        print(f_line)
    if not f_line:
        print("Not matched!")
        x = False
f.close()
    
#6
import re
f = open('row.txt','r', encoding = "utf8") 

x = True
while x:
    f_line = f.readline()
    if f_line:
        print(re.sub("[ ,.]", ":", f))
    if not f_line:
        print("Not matched!")
        x = False
f.close()
    
#7
import re
f = open('row.txt', 'r', encoding = "utf8") 
def tmt(txt):
    pat = ''.join(x.capitalize() or '_' for x in txt.split('_'))
    if re.search(pat, txt):
        return True
    else:
        return False 
    
x = True
while x:
    f_line = f.readline()
    if tmt(f_line):
        print(f_line)
    if not f_line:
        print("not such file or end file")
        x = False
f.close()

#8
import re
f = open('row.txt', encoding = "utf8") 

x = True
while x:
    f_line = f.readline()
    if f_line:
        print(re.findall('[А-Я][^А-Я]*', f_line))
    if not f_line:
        print("Not matched!")
        x = False
f.close()

#9
import re
f = open('row.txt', encoding = "utf8") 

x = True
while x:
    f_line = f.readline() 
    if f_line:
        print(re.sub(r"(\w)([A-Z])" or "(\w)([А-Я])", r"\1 \2", f_line))
    if not f_line:
        print("Not matched!")
        x = False
f.close()

#10
def camel_to_snake(camel_string):
    snake_list = []
    for i, c in enumerate(camel_string):
        if c.isupper() and i > 0:
            snake_list.append('_')
        snake_list.append(c.lower())
    return ''.join(snake_list)

f = open('row.txt', encoding="utf8")

x = True
while x:
    f_line = f.readline()
    f_line = "".join(f_line.split())
    print(camel_to_snake(f_line))
    if not f_line:
        print("End Of File")
        x = False
f.close()