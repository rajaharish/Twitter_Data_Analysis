from MRBiGramCount import MRBiGramCount
import sys
import json
import operator
from collections import OrderedDict
from collections import Counter


if __name__ == '__main__':
    # Creates an instance of our MRJob subclass
    job = MRBiGramCount(args=sys.argv[1:])
    with job.make_runner() as runner:
        # Run the job
        runner.run()
  
        # Process the output
        data=OrderedDict()
        for line in runner.stream_output():
            key, value = job.parse_output_line(line)
            data[str(tuple(key))]=value
         
        sorted_x= OrderedDict()
        ListItems=list(sorted_x)
        print Counter(data).most_common(10)