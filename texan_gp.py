import matplotlib
matplotlib.use('Agg')
## For use in WSL or where a GUI is not available
import numpy as np
import matplotlib.pyplot as plt
import re

def texan(x):
    f  = file(x + "_text.txt", 'r')
    l = 0
    w = 0
    c = 0
    for line in f:
        l+=1
        line=re.split(' +|\.+|,+|-+',line)
        for i in line:
            if len(i)==0:
                continue
            w+=1
            c+=len(i)
    return (l,w,c)



names = []
linecount = []
charcount = []
wordcount = []
wpl = []
emoj=[]

print "Enter contact names of chat members:"
while True:
    x=raw_input()
    if x=='':
        break
    names.append(x)

for i in names:
    x = texan(i)
    linecount.append(x[0])
    wordcount.append(x[1])
    charcount.append(x[2])
for i in range(len(names)):
    wpl.append(wordcount[i]*1.0/(linecount[i]*1.0))

print names
print linecount
print wordcount
print charcount
print wpl



objects =tuple(names)
y_pos = np.arange(len(objects))
plt.bar(y_pos, linecount, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.title('Number of lines')
plt.show()
plt.savefig('data_lines.png')
plt.clf()



plt.bar(y_pos, wordcount, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.title('Number of words')
plt.show()
plt.savefig('data_words.png')
plt.clf()

plt.bar(y_pos, charcount, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.title('Number of characters')
plt.show()
plt.savefig('data_characters.png')
plt.clf()

plt.bar(y_pos, wpl, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.title('Number of words per line(avg)')
plt.savefig('data_wpl.png')
plt.show()


