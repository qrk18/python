import nltk
from nltk.util import ngrams
import re
from nltk.tokenize import sent_tokenize
from nltk import load
import codecs


def getAdvAdjFourgrams(terms,nouns,posLex,negLex):

    result=[]

    fourgrams = ngrams(terms,4) #compute 4-grams
    
    #for each 4gram
    for tg in fourgrams:  
        if tg[0] == 'not' and tg[3] in nouns and tg[2] in posLex or tg[2] in negLex : # if the 2gram is a an adverb followed by an adjective
             result.append(tg)
   
    return result


# return all the terms that belong to a specific POS type
def getPOSterms(terms,POStags,tagger):
	
    tagged_terms=tagger.tag(terms)#do POS tagging on the tokenized sentence

    POSterms={}
    for tag in POStags:POSterms[tag]=set()

    #for each tagged term
    for pair in tagged_terms:
        for tag in POStags: # for each POS tag 
            if pair[1].startswith(tag): POSterms[tag].add(pair[0])

    return POSterms

    
def getTop3(D):
    t = sorted(D.items(), key=lambda x:-x[1])[:3]
    for x in t:
        print ("{0}".format(*x))
    
def loadLexicon(fname):
    newLex=set()
    lex_conn=codecs.open(fname,'r',encoding='utf-8')
    #add every word in the file to the set
    for line in lex_conn:
        newLex.add(line.strip())# remember to strip to remove the lin-change character
    lex_conn.close()

    return newLex   

D ={'ka':22,'buoy':7,'egg':89,'frog':56}
sentence ="not a good girl"
_POS_TAGGER = 'taggers/maxent_treebank_pos_tagger/english.pickle'
tagger = load(_POS_TAGGER)

posLex = loadLexicon('positive-words.txt')
negLex = loadLexicon('negative-words.txt')

     

def processSentence(sentence,posLex,negLex,tagger):
    #sentence=sentence.read().strip()
    #sentences=sent_tokenize(sentence)
    adjAfterAdv=[]
    #for sentence1 in sentences:

    sentence=re.sub('[^a-zA-Z\d]',' ',sentence)#replace chars that are not letters or numbers with a spac
    sentence=re.sub(' +',' ',sentence).strip()#remove duplicate spaces

        #tokenize the sentence
    terms = nltk.word_tokenize(sentence.lower()) 
        

    POStags=['NN'] # POS tags of interest 		
    POSterms=getPOSterms(terms,POStags,tagger)

    nouns=POSterms['NN']
        
        

        #get the results for this sentence 
    adjAfterAdv+=getAdvAdjFourgrams(terms,nouns,posLex,negLex)
        
    print (adjAfterAdv)
    
    
processSentence(sentence,posLex,negLex,tagger) 