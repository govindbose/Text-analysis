from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

ch = ChatBot("gss")
ch.set_trainer(ChatterBotCorpusTrainer)
ch.train("chatterbot.corpus.english")

f=file('data.txt','r')
x=[]
y=f.readlines()
for i in y:
    try:
        z= i.decode('ascii')
        x.append(z)
    except:
        pass

ch.set_trainer(ListTrainer)
ch.train(x)
print "all set"
while True:
    s=raw_input()
    print ch.get_response(s)

