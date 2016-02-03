from SortedTriGramCount import SortedTriGramCount
import sys
import json
import operator
from collections import OrderedDict
from collections import Counter


if __name__ == '__main__':
    # Creates an instance of our MRJob subclass
    job=SortedTriGramCount(args=sys.argv[1:])
    with job.make_runner() as runner:
        # Run the job
        runner.run()

        
        

        #print json.dumps(data)    
        # Process the output
        data=OrderedDict()
        for line in runner.stream_output():
            key, value = job.parse_output_line(line)
            #print 'key:', key, 'value:', value
            data[str(tuple(key))]=value
        # print(json.dumps(data)) 

        #sorted_x = sorted(data.items(), key=data.get)
        sorted_x= OrderedDict()
        #sorted_x = sorted(data.items(), key=operator.itemgetter(1))
        #sorted_x=sorted(data.values())
        ListItems=list(sorted_x)
        #for words in ListItems[-5:]:
        #	print words
        print Counter(data).most_common(10)