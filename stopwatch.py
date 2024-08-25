import time
import datetime
import os


class Stopwatch:
    def __init__(self):
        self.start_time = 0.0
        self.end_time = None
        self.elapsed_time = 0.0
        self.output_elapsed_time = None
        self.output_start_time = None
        self.output_end_time = None

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
        self.output_start_time = datetime.datetime.fromtimestamp(int(self.start_time)).time()
        self.output_end_time = datetime.datetime.fromtimestamp(int(self.end_time)).time()
        self.output_elapsed_time = datetime.timedelta(seconds=int(self.elapsed_time))

    def print_stats(self):
        print("\nSession started at: ", self.output_start_time)
        print("Session ended at: ", self.output_end_time)
        print("Session length: ", self.output_elapsed_time)
        print()


# Driver code
stopwatch = Stopwatch()

stopwatch.start()
stopwatch.print_stats()
