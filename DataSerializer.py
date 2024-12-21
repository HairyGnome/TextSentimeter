import os
import sys
import time

import joblib

from DatabaseParser import DatabaseParser
from TimeCalculator import sec_to_time


class DataSerializer:
    def save(self, data, path):
        start_time = time.time()
        joblib.dump(data, f'{os.curdir}/{path}')
        time_elapsed = sec_to_time(time.time() - start_time)
        sys.stdout.write(f'\nData saved in {time_elapsed[0]} days {time_elapsed[1]} hours {time_elapsed[2]} minutes {time_elapsed[3]} seconds\n')

    def load(self, path):
        try:
            start_time = time.time()
            loaded_data = joblib.load(path)
            time_elapsed = sec_to_time(time.time()-start_time)
            sys.stdout.write(f'\nData loaded in {time_elapsed[0]} days {time_elapsed[1]} hours {time_elapsed[2]} minutes {round(time_elapsed[3])} seconds\n')
            return loaded_data
        except FileNotFoundError:
            sys.stdout.write('Error: File not found')
            return ()

if __name__ == '__main__':
    serializer = DataSerializer()
    db_parser = DatabaseParser(10, True)
    data, labels, eval_data, eval_labels = db_parser.parse_data(os.curdir + '/data/dataset.csv')
    serializer.save((data, labels), '/data/training')
    serializer.save((eval_data, eval_labels), '/data/evaluation')