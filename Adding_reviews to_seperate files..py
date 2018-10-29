from collections import Counter
from nltk.corpus import stopwords
from os import listdir
import re
import string

#The first step is importing the document into the memory
#the function name would be loading data

def loading_data(filename):
    with open(filename,'r+',encoding='utf-8') as f:
        data=f.read()
    return data

#The next include turn the data into clearn docs
'''1) Spilt the tokens
   2) Removing the punctuation from words
   3) Removing token that contain the numbers
   4) Removing the that have one charactor or stop words
'''
def clearning_doc(doc_text):
    #spilting the text into the tokens
    tokens=doc_text.split()
    #now regular expression is use to remove the punctuations
    #re_exp_punc contain all the punctuations
    re_exp_punc=re.compile('[%s]'% re.escape(string.punctuation))
    #print(re_exp_punc)
    #removing the puncations from the tokens
    tokens=[re_exp_punc.sub('',w) for w in tokens]
    #NOw the tokens become puncations free
    #We use alph function to remove the digits
    tokens=[word for word in tokens if word.isalpha()]
    #filter out the stop words
    stop_words=set(stopwords.words('english'))
    tokens=[w for w in tokens if not w in stop_words]
    #filter out the short tokens
    tokens=[word for word in tokens if len(word)>2]
    return tokens

# save list to file
def save_list(lines,filename):
    data='\n'.join(lines)
    with open (filename, 'w') as f:
        f.write(data)
#load the doc, clean the doc and save the doc
def doc_to_line(filename,vocab):
    #load
   doc=loading_data(filename)
   tokens=clearning_doc(doc)
   tokens=[word for word in tokens if word in vocab]
   return ' '.join(tokens)


#Adding all docs in directory
def going_process(directory,vocab):
    lines=list()
    for filename in listdir(directory):
        if not filename.endswith('.txt'):
            next
        path=directory+'/'+filename
        line=doc_to_line(path,vocab)
        lines.append(line)
    return lines
#save the vocab list to the file
def save_list(lines,filename):
    data='\n'.join(lines)
    with open(filename,'w') as f:
        f.write(data)

#loading vocab
vocab_name='vocab.txt'
vocab=loading_data(vocab_name)
vocab=vocab.split()
vocab=set(vocab)

#prepaing the postive file
postive_lines=going_process('txt_sentoken/pos',vocab)
save_list(postive_lines,'postive.txt')
negative_lines=going_process('txt_sentoken/neg',vocab)
save_list(negative_lines,'negative.txt')