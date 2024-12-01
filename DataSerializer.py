import joblib
import threading
import time
import math
import sys
import os

from TimeCalculator import sec_to_time

class DataSerializer:

    def save(self, data):
        saving_completed = False
        def save_data():
            joblib.dump(data, f'{os.curdir}/data/dataset')
            callback()

        def callback():
            nonlocal saving_completed
            saving_completed = True

        start_time = time.time()
        thread = threading.Thread(target=save_data())
        thread.start()
        while not saving_completed:
            time_elapsed = time.time()-start_time
            time_elapsed = math.floor(time_elapsed)
            time_elapsed = sec_to_time(time_elapsed)
            output = f'Time elapsed: {time_elapsed[0]} days {time_elapsed[1]} hours {time_elapsed[2]} minutes {math.floor(time_elapsed[3])} seconds'
            sys.stdout.write(f'\r{output}')
            sys.stdout.flush()
        sys.stdout.write('\nData saved!\n')

    def load(self, path):
        loading_completed = False

        def load_data():
            joblib.load(path)
            callback()

        def callback():
            nonlocal loading_completed
            loading_completed = True

        start_time = time.time()
        thread = threading.Thread(target=load_data())
        thread.start()
        while not loading_completed:
            time_elapsed = time.time() - start_time
            time_elapsed = math.floor(time_elapsed)
            time_elapsed = sec_to_time(time_elapsed)
            output = f'Time elapsed: {time_elapsed[0]} days {time_elapsed[1]} hours {time_elapsed[2]} minutes {math.floor(time_elapsed[3])} seconds'
            sys.stdout.write(f'\r{output}')
            sys.stdout.flush()
        sys.stdout.write('\nData loaded!\n')