
from mrjob.job import MRJob
from mrjob.step import MRStep
import re
import nltk


lastWord=None
lastWordTrigram=None

class WordFrequency(MRJob):

    
    def mapper(self, _, line):
        # yield each word in the line
        # for word in WORD_RE.findall(line):
        if len(line.strip()) != 0 :
            global lastWord
            global lastWordTrigram
            if lastWord is None and lastWordTrigram is None:
                lastWord = ""
                lastWordTrigram = ""
            from_prev_line_trigram=" ".join(lastWordTrigram)    
            updatedline_trigram=from_prev_line_trigram+" "+line
            updatedline_bigram=lastWord+" "+line
            newword_trigram=nltk.word_tokenize(updatedline_trigram)
            newword_bigram=nltk.word_tokenize(updatedline_bigram)
            yield "monograms",len(list(nltk.ngrams(nltk.word_tokenize(line),1)))
            #for bigram in nltk.bigrams(newword):
            yield "bigram", len(list(nltk.bigrams(newword_bigram)))
            #for word in nltk.ngrams(newword,3)
            yield "trigram", len(list(nltk.ngrams(newword_trigram,3)))
            lastWord = updatedline_bigram.split()[-1]
            lastWordTrigram=updatedline_trigram.split()[-2:]
        
    def combiner(self, key, values):
        yield key,sum(values)

if __name__ == '__main__':
    lastWord=None
    lastWordTrigram=None
    WordFrequency.run()