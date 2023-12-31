import datetime
import statistics



message_fmt =  '''
# Statistic from: {date}
# Count:        {count}
# Sum:          {sum}
# Mean:         {mean}
# Median:       {median}
'''

with open('data\example6.txt', 'r+') as data:
    numbers = [float(line) for line in data
               if line != '\n' and not line.startswith('#')]
    message = message_fmt.format(
           date = datetime.datetime.now(),
           count = len(numbers),
           sum = sum(numbers),
           mean = statistics.mean(numbers),
           median = statistics.median(numbers) )



    print(message, file = data)
    #print(message)