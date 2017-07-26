import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import re

emo={}

def texan(x):
    f  = file(x + ".txt", 'r')
    fnu = file(x + "_new.txt",'w')
    l = 0
    w = 0
    c = 0
    e = 0
    for line in f:
        l+=1
        line=line.strip().lower()
        x = re.sub(ur'[\U0001f600-\U0001f650]|[\U0001f300-\U0001f5ff]|[\U0001f680-\U0001f6ff]|\:p|\:\)|\:\(|\:\\|\:\/|xd|xp|_|\*',' ',line.decode('utf-8'),flags=re.UNICODE)
        if x:
            #print x.encode('utf-8')
            fnu.write(x.encode('utf-8')+'\n')
        line=re.split(' +|\.+|,+|-+',line)
        for i in line:
            if len(i)==0:
                continue
            w+=1
            c+=len(i)
    return (l,w,c,e)





print "enter names of ppl"
a = []
linecount = []
charcount = []
wordcount = []
wpl = []
emoj=[]
while True:
    x=raw_input()
    if x=='':
        break
    a.append(x)

for i in a:
    x = texan(i)
    linecount.append(x[0])
    wordcount.append(x[1])
    charcount.append(x[2])
    emoj.append(x[3])
for i in range(len(a)):
    wpl.append(wordcount[i]*1.0/(linecount[i]*1.0))

print a
#print linecount
#print wordcount
print charcount
#print wpl
print emoj



tot_emoj=[]
tot_emoj_no=[]
for i in emo:
    if emo[i]>10:
        tot_emoj.append(i)
        tot_emoj_no.append(emo[i])
        #print i.encode('utf-8') , emo[i]


plt.clf()

objects =tuple(a)
y_pos = np.arange(len(objects))
plt.bar(y_pos, linecount, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.title('Number of lines')
plt.show()

plt.bar(y_pos, wordcount, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.title('Number of words')
plt.show()

plt.bar(y_pos, charcount, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.title('Number of characters')
plt.show()

plt.bar(y_pos, wpl, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.title('Number of words per line(avg)')
plt.show()


plt.bar(y_pos, emoj, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.title('emojis')
plt.show()


emo_ypos=np.arange(len(tot_emoj))
plt.bar(emo_ypos, tot_emoj_no , align='center', alpha=0.5)
plt.xticks(emo_ypos, tuple(tot_emoj))
plt.title('total emojis')
plt.show()
