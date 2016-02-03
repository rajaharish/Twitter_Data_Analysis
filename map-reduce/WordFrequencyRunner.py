from WordFrequency import WordFrequency
import sys
import json
import operator
from collections import OrderedDict
from collections import Counter


if __name__ == '__main__':
    # Creates an instance of our MRJob subclass
    job=WordFrequency(args=sys.argv[1:])
    with job.make_runner() as runner:
        # Run the job
        runner.run()

        
        

        #print json.dumps(data)    
        # Process the output
        f = open("result.txt", "w")
        data=OrderedDict()
        for line in runner.stream_output():
            key, value = job.parse_output_line(line)
            print 'key:', key, 'value:', value
            f.write(str(str(key)+" "+str(value)))
            f.write("\n")
        f.close()