import nltk
import re
import io


def plot(s):
    x=[]
 #   f=file(s+".txt",'r')
    f= io.open(s+".txt", "r", encoding="utf-8")
    for i in f:
        z=re.split(r'\:p|\:\)|\:\(|\:\\|\:\/|xd|xp| +|\.+|\_+|\:+|\,+|\?+|\;+|\-+|',i.strip().lower())   #ignore emoticons, punctuation
        z=filter(None,z)  #remove empty lists
        #print z
        x+=z
    f1= nltk.FreqDist(x)
    #print x.nltk.collocations()
    f1.plot(100)
    nu=nltk.Text(x)
    print nu.collocations()

while True:
    s=raw_input()
    if s=='':
        break
    plot(s)
    
