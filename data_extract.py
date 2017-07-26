import re
people={}
class msg:
    def __init__(self):
        self.d_d=0  #date
        self.d_m=0  #m
        self.d_y=0  #y
        self.d_t=0 #time
        self.text="" #text
        self.owner=""
    def show(self): #print all
        print self.d_d, self.d_m,self.d_y,self.d_t,self.text


        
def msg_strip(l,prev):
    a=msg()
    try :
        t,x=map(str,l.split(', ',1))
        date=t.split('/')
        a.d_d=date[0]
        a.d_m=date[1]
        a.d_y=date[2]
        #print x
        x=re.split(' - |:| ',x,3)    # not splitting to name + text because contact name might have a space
        #print x
        a.d_t=int(x[0])*3600+int(x[1])*60
        if (x[2]=="PM"):
            a.d_t+=12*3600
        m=x[3].split(':',1)         # careful, contact name shouldnt have a :
        a.text=m[1].strip()  
        n=m[0]
        a.owner=n
    except (ValueError,IndexError):
        a.d_d=prev.d_d
        a.d_m=prev.d_m
        a.d_y=prev.d_y
        a.d_t=prev.d_t
        a.text=l.strip()
        a.owner=prev.owner
        n=prev.owner
    if people.get(n)==None:
        people[n]=[]
    people[n].append(a)
    glob_file.write(a.text+'\n')
    return a
    
s=raw_input()
f=file(s,'r')
glob_file=file('convo.txt','w')

prev = msg()
i=f.readlines()
for x in i:
    prev = msg_strip(x,prev)
    #prev.show()
for i in people:
    f.close()
    f=file(i+"_text.txt",'w')
    print i
    for j in people[i]:
        j.show()
        f.write(j.text+'\n')
glob_file.close()
