# Text-analysis


This is a basic Text analyser for WhatsApp. It uses the format obtained in the default whatsapp chat file obtained from sending a chat over email.

Has functions to plot individual word/line count in groups. Can be modified to whatever you think of.

###Sequence of operation
1. _make_convo.py_		: Makes everything lowercase, removes non-ascii characters, and text smileys.
2. _data_extract.py		: Splits the data into text/time sent etc. 
3. _count_data.py_		: Analyzes the processed data