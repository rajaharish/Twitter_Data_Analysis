
#The MapReduce Job for calucalting ordered bigrams.

from mrjob.job import MRJob
from mrjob.step import MRStep
import re
import nltk

WORD_RE = re.compile(r"[\w']+")
lastWord=None
counter=0
class SortedBiGramCount(MRJob):

    
    def mapper(self, _, line):
        global lastWord
        global counter
        if lastWord is None:
            lastWord = ""
        updatedline=lastWord+" "+line
        newword=nltk.word_tokenize(updatedline)
        for word in nltk.bigrams(newword):
            sortedbigram= sorted(word)
            yield (sortedbigram, 1)
        if(len(line.split()) <= 0):
            counter=counter+1
        else:
             lastWord = updatedline.split()[-1]
        

   

    def reducer(self, word, counts):
        SORT_VALUES = True
        yield (word),sum(counts)

if __name__ == '__main__':
    lastWord=None
    counter=0
    SortedBiGramCount.run()