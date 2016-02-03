
#The MapReduce Job for calucalting ordered trigrams.

from mrjob.job import MRJob
from mrjob.step import MRStep
import re
import nltk


lastWord=None

class SortedTriGramCount(MRJob):

    
    def mapper(self, _, line):
        global lastWord
        global counter
        if len(line.strip()) != 0 :
            if lastWord is None:
                lastWord = ""
            from_prev_line=" ".join(lastWord)    
            updatedline=from_prev_line+" "+line
            newword=nltk.word_tokenize(updatedline)
            for word in nltk.ngrams(newword,3):
                sortedbigram= sorted(word)
                yield (sortedbigram, 1)
                lastWord = updatedline.split()[-2:]
        

   

    def reducer(self, word, counts):
        SORT_VALUES = True
        yield (word),sum(counts)

if __name__ == '__main__':
    lastWord=None
    SortedTriGramCount.run()