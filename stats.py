import json


class Stats:
    def __init__(self):
        self.total_time = None
        self.streak = None
        self.weekly_frequency = None

    # parse the log file and calculate all stats
