import joblib
import threading
import time
import math
import sys
import os

from DatabaseParser import DatabaseParser
from TimeCalculator import sec_to_time

class DataSerializer:
    def save(self, data, path):
        joblib.dump(data, f'{os.curdir}/{path}')
        sys.stdout.write('\nData saved!\n')

    def load(self, path):
        try:
            loaded_data = joblib.load(path)
            sys.stdout.write('\nData loaded!\n')
            return loaded_data
        except FileNotFoundError:
            sys.stdout.write('Error: File not found')
            return

if __name__ == '__main__':
    serializer = DataSerializer()
    db_parser = DatabaseParser(10, True)
    data, labels, eval_data, eval_labels = db_parser.parse_data(os.curdir + '/data/dataset.csv')
    serializer.save((data, labels), '/data/training')
    serializer.save((eval_data, eval_labels), '/data/evaluation')