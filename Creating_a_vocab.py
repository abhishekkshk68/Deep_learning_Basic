from collection import Counter
from nltk.corpus import stopwords

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
    token=doc_text.split()
    #now regular expression is use to remove the punctuations
    #re_exp_punc contain all the punctuations
    re_exp_punc=re.compile('[%s]'% re.escape(string.punctuation))
    print(re_exp_punc)
    #removing the puncations from the tokens
    token=[re_exp_punc.sub('',w) for w in tokens]
    #NOw the tokens become puncations free
    #We use alph function to remove the digits
    tokens=[word for word in tokens if word.isalpha()]
    #filter out the stope words

