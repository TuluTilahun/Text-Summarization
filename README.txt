# WETS

=== WETS stands for Word Embedding based Text Summarization.
=== It is intended for selecting top-n salient sentences from original text, which can be used as a reference summary.
=== WETS is proposed to address lack of ideal and complete ground truth (human generated reference summary).

# WEEM4TS

=== WEEM4TS represents Word Embedding based Evaluation Metric for Text Summarization.

# Requirements:

=== Install python 3.0, gensim, numpy, nltk, and textwrap  
=== Load any word embedding model you need from the following links:
	== https://code.google.com/archive/p/word2vec/                           (Word2Vec based embedding)
	== https://nlp.stanford.edu/projects/glove/     (glove.840B.300d.zip)    (GloVe based embedding)
	== https://fasttext.cc/docs/en/crawl-vectors.html                        (FastText based embedding)
=== Word2Vec based word embedding models are compatible with gensim. However, GloVe and FastText based file formats need to be converted to equivalent Word2Vec version.
=== For conversion, use: WordEmbeddingConverterToSuitableFormat.py   (Assign the loaded word embedding model to a variable name "filename", then the equivalent file will be created in the same folder)

# Procedure for generating reference summary using WETS

	1. Copy the original text and paste in "OriginalToBesummarized.txt"
	2. Open "WETS.py" and do the following:
		== Go to line code: "m=len(wordfreq)-5", and set the number of top m frequent words. In our case we determined top m=len(wordfreq)-5. You can comment this line and assign acceptable top frequent number to m. 
		== Assign the appropriate word embedding to the variable "filename".
		== Go to line code:"my_wrap = textwrap.TextWrapper(width = 800)" and you can change width. In our case 800 words of top-n sentences, which can be adjusted manually, later, by picking the required number of words from generated top sentences.
		== After running "WETS.py", top-n sentences, in our case top sentences of 800 words will be written to the file: "ReferenceSummary.txt".
		== You can also use "WETSsummaryLengthAdjustment.py" to adjust length of reference summary according to the length of system generated summary.
			== The reference summary that length adjusted according to system summary should be written to "ReferenceLengthAdjusted.txt"

# Procedure for evaluating system generated summary using WEEM4TS

	1. Copy ground truth (human generated summary or WETS generated reference summary) and paste in "reference.txt"
	2. Copy system generated summary and paste in "hypothesis.txt"
	3. Open "WEEM4TS.py" and assign the appropriate word embedding to the variable "filename".
	4. Run, "WEEM4TS.py", segment level WEEM4TS score and system level WEEM4TS score should be written in "WEEM4TS.seg.score" and "WEEM4TS.sys.score" respectively.   

# Authors

=== [Tulu Tilahun Hailu] (tutilacs@yahoo.com)
=== [Junqing Yu] (yjqing@hust.edu.cn)
=== [Tessfu Geteye Fantaye] (tessfug@hust.edu.cn) 

# Reference

=== If you use WETS and/or WEEM4TS, please cite the following reference. 
