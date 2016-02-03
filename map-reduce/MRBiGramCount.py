
#The MapReduce Job for calucalting bigrams.

from mrjob.job import MRJob
from mrjob.step import MRStep
import re
import nltk


lastWord=None

class MRBiGramCount(MRJob):

    
    def mapper(self, _, line):
        if len(line.strip()) != 0 :
            global lastWord
            if lastWord is None:
                lastWord = ""
            updatedline=lastWord+" "+line
            newword=nltk.word_tokenize(updatedline)
            for word in nltk.bigrams(newword):
                yield (word, 1)
            lastWord = updatedline.split()[-1]

    def reducer(self, word, counts):
        SORT_VALUES = True
        yield (word),sum(counts)

if __name__ == '__main__':
    lastWord=None
    counter=0
    MRBiGramCount.run()