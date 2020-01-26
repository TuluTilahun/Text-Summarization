# load doc into memory
def load_doc(filename):
	# open the file as read only
	file = open(filename, mode='rt', encoding='utf-8', errors='ignore')
	# read all text
	text = file.readlines()
	# close the file
	file.close()
	return text

h="hypothesis.txt"
r="reference.txt"
syssummary=load_doc(h)
refsummary=load_doc(r)

#print(syssummary[1].split())
#print(refsummary[1].split())

#print(len(syssummary))
#print(len(refsummary))

RefsumlenAdju=open("ReferenceLengthAdjusted.txt","a", encoding='utf-8')
for i in range(len(refsummary)):
    splitrefsummary=refsummary[i].split()
    splitsyssummary=syssummary[i].split()
    
    RefsumlenAdju.write(str(splitrefsummary[0:len(splitsyssummary)]))
    RefsumlenAdju.write("\n")

RefsumlenAdju.close()

print("Done!!!")