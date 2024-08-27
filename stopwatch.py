import time
import datetime
import os


class Stopwatch:
    def __init__(self):
        self.start_time = 0.0
        self.end_time = None
        self.elapsed_time = 0.0
        self.format_elapsed_time = None
        self.format_start_time = None
        self.format_end_time = None

    def start(self):
        # Run stopwatch until user enters ctrl-c
        try:
            self.start_time = time.time()
            print("Time started, ctrl-c to end")
            while True:
                pass

        except KeyboardInterrupt:
            self.end_time = time.time()

        self.elapsed_time = self.end_time - self.start_time

        self.calc_stats()

    def calc_stats(self):
        self.format_start_time = datetime.datetime.fromtimestamp(int(self.start_time)).time()
        self.format_end_time = datetime.datetime.fromtimestamp(int(self.end_time)).time()
        self.format_elapsed_time = datetime.timedelta(seconds=int(self.elapsed_time))

    # move this to other module
    def print_stats(self):
        print("\nSession started at: ", self.format_start_time)
        print("Session ended at: ", self.format_end_time)
        print("Session length: ", self.format_elapsed_time)
        print()
