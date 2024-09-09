import json


class StudyStats:
    def __init__(self):
        self.total_time = None
        self.streak = None
        self.weekly_frequency = None
        self.description = None

    def getDescription(self, log_array, session_id):
        if len(log_array) <= 0:
            print("length error!\n")
            return "ERROR 1"

        for entry in log_array:
            # print(entry)
            # print(entry["Session"])
            # print(session_id)
            # print("\n")
            if entry["Session"] == session_id:
                return entry["Log"]

        return "ERROR2"

    # parse the log file and calculate all stats
