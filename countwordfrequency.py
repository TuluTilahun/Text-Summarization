from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 

#wordstring = 'it was the best of times it was the worst of times '
#wordstring += 'it was the age of wisdom it was the age of foolishness'

wordstring='A person who loves someone is surely loved in turn by the others. Researchers show that the more a person loves people around him/her the better healthy life he/she has. People who love others without any condition are mostly lead happy life. Contrary, there are people who are ignorant and get satisfaction by hurting others. Some of them develop this behavior from their childhood.  Adoring others will give you immense happiness and peace.'

wordlist = wordstring.split()

wordfreq = []
for w in wordlist:
    wordfreq.append(wordlist.count(w))

print("String\n" + wordstring +"\n")
print("List\n" + str(wordlist) + "\n")
print("Frequencies\n" + str(wordfreq) + "\n")
print("Pairs\n" + str(list(zip(wordlist, wordfreq))))

example_sent='A person who loves someone is surely loved in turn by the others'
stop_words = set(stopwords.words('english')) 
  
word_tokens = word_tokenize(example_sent) 
  
filtered_sentence = [w for w in word_tokens if not w in stop_words] 
  
filtered_sentence = [] 
  
for w in word_tokens: 
    if w not in stop_words: 
        filtered_sentence.append(w) 
  
print(word_tokens) 
print(filtered_sentence)