import csv
import math
import os
import sys
import time



from Tokenizer import Tokenizer
from TimeCalculator import sec_to_time


class DatabaseParser:

    test_ratio = 10
    generate_train_data = False
    num_classes = 5

    def __init__(self, ratio = 10, generate_train_data = True, num_classes = 5):
        self.test_ratio = ratio
        self.generate_train_data = generate_train_data
        self.num_classes = num_classes

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
                    curr_time = time.time()
                    time_elapsed = curr_time-start_time
                    if i != 0:
                        estimated_time = time_elapsed/i * (1600000-i)
                    else:
                        estimated_time = 99999999999
                    time_elapsed = sec_to_time(time_elapsed)
                    estimated_time = sec_to_time(estimated_time)
                    output = f'Row number: {i}/1,600,000\tTime elapsed: {time_elapsed[0]} days {time_elapsed[1]} hours {time_elapsed[2]} minutes {math.floor(time_elapsed[3])} seconds\tEstimated time left: {estimated_time[0]} days {estimated_time[1]} hours {estimated_time[2]} minutes {round(estimated_time[3])} seconds'
                    sys.stdout.write(f'\r{output}')
                    sys.stdout.flush()
                    if self.generate_train_data and i % self.test_ratio == 0:
                        eval_data.append(tokenizer.tokenize(row[5].strip()))
                        eval_labels.append(self.get_label_vector(int(row[0])))
                    else:
                        data.append(tokenizer.tokenize(row[5]))
                        labels.append(self.get_label_vector(int(row[0])))
                    i += 1

            sys.stdout.write('\n')
            return data, labels, eval_data, eval_labels

        except FileNotFoundError:
            print('Error: File not found')

    def get_label_vector(self, label):
        label_vector = []
        for i in range(self.num_classes):
            if i == label:
                label_vector.append(1)
            else:
                label_vector.append(0)
        return label_vector

if __name__ == '__main__':
    parser = DatabaseParser(10)
    data, label = parser.parse_data(os.curdir + '/data/dataset.csv')
    print(data[:5])