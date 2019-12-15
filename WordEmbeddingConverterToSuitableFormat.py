import gensim

#filename='GoogleNews-vectors-negative300.bin'  # downloaded from : https://code.google.com/archive/p/word2vec/  
filename = 'glove.840B.300d.txt'  				# downloaded from : https://nlp.stanford.edu/projects/glove/ 
#filename = 'cc.en.300.vec.txt'                 # downloaded from : https://fasttext.cc/docs/en/crawl-vectors.html 

# Keep this script with the downloaded embedding and run to get equivalent Word2Vec file fromat.
model = gensim.models.KeyedVectors.load_word2vec_format(filename, binary=False) 
model.save_word2vec_format(filename+".bin", binary=True) 
model = gensim.models.KeyedVectors.load_word2vec_format(filename+".bin", binary=True)   #Equivalent Word2Vec for cc.en.300.vec.txt embedding is saved as cc.en.300.vec.txt.bin


 


