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
#Adding the vocab by laoding the doc
def add_vocab_load_data(filename,vocab):
  data=loading_data(filename)
  vocab_words=clearning_doc(data)
  vocab.update(vocab_words)

#Adding all docs in directory
def going_process(directory,vocab):
    for filename in listdir(directory):
        if not filename.endswith('.txt'):
            next
        path=directory+'/'+filename
        add_vocab_load_data(path,vocab)
#save the vocab list to the file
def save_list(lines,filename):
    data='\n'.join(lines)
    with open(filename,'w') as f:
        f.write(data)

#define vocab
vocab=Counter()
#add all docs to vocab
going_process('txt_sentoken/neg',vocab)
going_process('txt_sentoken/pos',vocab)

#print the size of the vocab
print(len(vocab))
#print the top words in the vocab
print(vocab.most_common(50))
#keep tokens with >5 occurrence
min_occurrence=5
tokens=[k for k,c in vocab.items() if c>=min_occurrence]
print(len(tokens))
#save tokens to a vocabulary file
save_list(tokens,'vocab.txt')




