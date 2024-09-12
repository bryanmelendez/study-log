import yaml
from datetime import timedelta


class StudyStats:
    def __init__(self):
        self.log_file = "study_log.yaml"
        self.stats_file = "study_stats.yaml"
        self.total_time = None
        self.streak = None
        self.weekly_frequency = None
        self.description = None

        self.__time_entries = list()

        self.stats = {
            "Total time": None,
            "Consecutive days": None,
        }

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

    def get_total_time(self):
        with open(self.log_file, "r") as infile:
            log = yaml.safe_load(infile)

        # get the session length for each entry
        for entry in log:
            time_str = entry["Session length"]

            # Convert the time in string format to timedelta format
            hours, minutes, seconds = map(int, time_str.split(':'))
            td = timedelta(hours=hours, minutes=minutes, seconds=seconds)

            self.__time_entries.append(td)

        total = timedelta()
        for entry in self.__time_entries:
            total = total + entry

        self.total_time = str(total)

        print(self.total_time)

    def create_stats(self):
        self.get_total_time()
        self.stats["Total time"] = self.total_time

        with open(self.stats_file, "w") as outfile:
            yaml_list = list()
            yaml_list.append(self.stats)
            yaml_object = yaml.dump(yaml_list, sort_keys=False)
            outfile.write(yaml_object)


def main():
    stats = StudyStats()
    stats.create_stats()


if __name__ == "__main__":
    main()
