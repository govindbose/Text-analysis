import re    
def msg_strip(l):
    x = re.sub(ur'[\U0001f600-\U0001f650]|[\U0001f300-\U0001f5ff]|[\U0001f680-\U0001f6ff]|\:p|\:\)|\:\(|\:\\|\:\/|xd|xp|_|\*|\.',' ',l.lower().decode('utf-8'),flags=re.UNICODE)
    print x
    glob_file.write(x.encode('utf-8'))
    return x
    
s=raw_input()
f=file(s,'r')
glob_file=file('_new_'+s,'w')
i = f.readlines()
for x in i:
    msg_strip(x)
glob_file.close()
