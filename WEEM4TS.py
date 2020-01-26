from gensim.models import KeyedVectors
import datetime
import numpy as np

start = datetime.datetime.now()
print(start)
# Load reference summary and system system
def load_doc(filepath): # open the file as read only
    file = open(filepath, mode='rt', encoding='utf-8')
    text=list()
    # read all text
    lines = file.readlines()
    for i in lines:
        data=i.split()
        text.append(data)
    file.close()
    return text

refsummary=load_doc("reference.txt")
syssummary=load_doc("hypothesis.txt")
#print(len(refsummary))

print("System summary before preprocessing:")
print(syssummary[0])
print("Number of words = ", len(syssummary[0]))
print("Reference summary before preprocessing:")
print(refsummary[0])
print("Number of words = ", len(refsummary[0]))

#filename = 'GoogleNews-vectors-negative300.bin'    # Word2Vec based WEEM4TS
filename = 'glove.840B.300d.txt.word2vec.bin'    # GloVe based WEEM4TS
#filename = 'cc.en.300.vec.bin'    # FastText based WEEM4TS

model = KeyedVectors.load_word2vec_format(filename, binary=True)
embwords = list(model.wv.vocab)

add=0.0
for i in range(len(refsummary)):

    notmatchwordREF=np.setdiff1d(refsummary[i],syssummary[i])
    notmatchwordSYS=np.setdiff1d(syssummary[i],refsummary[i])
    notmatchwordREFemb=[]
    for m in range(len(notmatchwordREF)):
        if notmatchwordREF[m] in embwords:
            notmatchwordREFemb.append(notmatchwordREF[m])
            
    sentweight=0.0
    unigramrecall=0.0
    weight=0.0
    countbigram=0.0
        
    for n in range(len(syssummary[i])):
        
        if syssummary[i][n] in refsummary[i]:
            weight=1.0
            sentweight=sentweight+weight
            if syssummary[i][n] in syssummary[i] and syssummary[i][n] in refsummary[i]:
                if n<(len(syssummary[i])-1) and syssummary[i].index(syssummary[i][n])+1<len(syssummary[i]) and refsummary[i].index(syssummary[i][n])+1<len(refsummary[i]):
                    if syssummary[i][syssummary[i].index(syssummary[i][n])+1].lower() == (refsummary[i][refsummary[i].index(syssummary[i][n])+1]).lower():
                        countbigram=countbigram+1
                
        elif len(notmatchwordREFemb)>0 and syssummary[i][n] in embwords:
            result=[model.wv.similarity(syssummary[i][n],word) for word in notmatchwordREFemb]
            weight=max(result)
            sentweight=sentweight+weight
            if syssummary[i][n] in syssummary[i] and notmatchwordREFemb[result.index(max(result))] in refsummary[i]:
                if n<(len(syssummary[i])-1) and syssummary[i].index(syssummary[i][n])+1<len(syssummary[i]) and refsummary[i].index(notmatchwordREFemb[result.index(max(result))])+1<len(refsummary[i]):
                    if (syssummary[i][syssummary[i].index(syssummary[i][n])+1]).lower() == (refsummary[i][refsummary[i].index(notmatchwordREFemb[result.index(max(result))])+1]).lower():
                        countbigram=countbigram+1
        else:
           weight=0.0
           sentweight=sentweight+weight 
    
 
    if len(refsummary[i])>0 or len(syssummary[i])>0:
        unigramrecall=sentweight/max(len(refsummary[i]),len((syssummary[i])))  # this is for fair evaluation for system summaries that is too less or too high than reference summary
    else:
        unigramrecall=0
        
    bigramprecision=(countbigram/(len(syssummary[i])-1))*100
    unigramrecall=unigramrecall*100

    WEEM4TSscore=(0.8*unigramrecall)+(0.2*bigramprecision)   # alpha = 0/8, betta=0.2

   
    #Segment level summary score
    f=open("WEEM4TS.seg.score","a+")
    f.write("SystemName\t" + str(i+1) + "\t" + str(WEEM4TSscore) + "\n")
    f.close()
    
    add=add+WEEM4TSscore

#System level summary score   
f=open("WEEM4TS.sys.score","a+")
WEEM4CB=add/len(refsummary)
f.write("SystemName\t" + str(WEEM4CB)+"\n")
f.close()
print("Done!!!")
 