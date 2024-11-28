import csv
import math
import os
import sys
import time

from pyasn1_modules.rfc1902 import Integer

from Tokenizer import Tokenizer


class DatabaseParser:

    def secToTime(self, sec):
        days = math.floor(sec/86400)
        sec = sec % 86400
        hours = math.floor(sec/3600)
        sec = sec % 3600
        minutes = math.floor(sec/60)
        sec = sec % 60
        return days, hours, minutes, sec

    def parseData(self, path):
        data = []
        labels = []
        test_data = []
        test_labels = []
        tokenizer = Tokenizer()
        try:
            with open(path, 'r') as csvfile:
                csvreader = csv.reader(csvfile)
                next(csvreader)
                i = 0
                start_time = time.time()
                for row in csvreader:
                    line_num = csvreader
                    curr_time = time.time()
                    time_elapsed = curr_time-start_time
                    if i != 0:
                        estimated_time = time_elapsed/i * (1600000-i)
                    else:
                        estimated_time = 99999999999
                    estimated_time = self.secToTime(estimated_time)
                    output = f'Row number: {i}/1,600,000\tTime elapsed: {math.floor(time_elapsed)} s\tEstimated time left: {estimated_time[0]} days {estimated_time[1]} hours {estimated_time[2]} minutes {round(estimated_time[3])} seconds'
                    sys.stdout.write(f'\r{output}')
                    sys.stdout.flush()
                    if i % 10 == 0:
                        test_data.append(tokenizer.tokenize(row[5]))
                        test_labels.append(row[0])
                    else:
                        data.append(tokenizer.tokenize(row[5]))
                        labels.append(row[0])
                    i += 1

            return data, labels

        except FileNotFoundError:
            print('Error: File not found')


if __name__ == '__main__':
    parser = DatabaseParser()
    data, label = parser.parseData(os.curdir+'/data/dataset.csv')
    print(data[:5])