a = 3
b = 4
tem = 0
i = 0
text = ''
while(i < b): 
    tem +=a
    text += str(a)
    if(i < b):
        text += '+'
    i += 1
print(text + ' = ' + str(tem))
