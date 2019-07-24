import re    
def msg_strip(l):
    l=  l.decode('utf-8').encode('ascii', 'ignore').decode('ascii') 
    #Removes non ascii characters viz emojis
    x = re.sub(ur'\:p|\:\)|\:\(|\:\\|\:\/|xd|xp|_|\*|\.',' ',l.lower().decode('utf-8'),flags=re.UNICODE)
    #Removes text smileys
    print x
    glob_file.write(x.encode('utf-8'))
    return x
    
s=raw_input("Enter name of chat file:")
f=file(s,'r')
glob_file=file('new_'+s,'w')
i = f.readlines()
for x in i:
    msg_strip(x)
glob_file.close()
