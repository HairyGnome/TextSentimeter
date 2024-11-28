import csv
import math
import os
import sys
import time

from pyasn1_modules.rfc1902 import Integer

from Tokenizer import Tokenizer


class DatabaseParser:

    test_ratio = 10

    def __init__(self, ratio):
        test_ratio = ratio

    def sec_to_time(self, sec):
        days = math.floor(sec/86400)
        sec = sec % 86400
        hours = math.floor(sec/3600)
        sec = sec % 3600
        minutes = math.floor(sec/60)
        sec = sec % 60
        return days, hours, minutes, sec

    def parse_data(self, path):
        data = []
        labels = []
        eval_data = []
        eval_labels = []
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
                    estimated_time = self.sec_to_time(estimated_time)
                    output = f'Row number: {i}/1,600,000\tTime elapsed: {math.floor(time_elapsed)} s\tEstimated time left: {estimated_time[0]} days {estimated_time[1]} hours {estimated_time[2]} minutes {round(estimated_time[3])} seconds'
                    sys.stdout.write(f'\r{output}')
                    sys.stdout.flush()
                    if i % self.test_ratio == 0:
                        eval_data.append(tokenizer.tokenize(row[5]))
                        eval_labels.append(row[0])
                    else:
                        data.append(tokenizer.tokenize(row[5]))
                        labels.append(row[0])
                    i += 1

            return data, labels, eval_data, eval_labels

        except FileNotFoundError:
            print('Error: File not found')


if __name__ == '__main__':
    parser = DatabaseParser()
    data, label = parser.parse_data(os.curdir + '/data/dataset.csv')
    print(data[:5])