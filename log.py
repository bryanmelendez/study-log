import json
import os
from stopwatch import Stopwatch


class Log:
    def __init__(self):
        self.log_file = "study_log.json"
        self.backup_file = "backup_study_log.json"
        self.backup = None
        self.subject = None
        self.session = 0

    def menu(self):
        # example
        subjects = ['programming', 'math']

        print("Subjects:")
        for i in range(0, len(subjects)):
            print("{}. {}".format(i+1, subjects[i]))
        choice = int(input("Which subject are you studying?\t"))
        if choice > 0 and choice <= len(subjects):
            self.subject = subjects[choice-1]

    def start_session(self):
        sw = Stopwatch()

        sw.start()

        if os.path.exists(self.log_file):
            os.rename(self.log_file, self.backup_file)
            with open(self.backup_file, "r") as infile:
                self.backup = json.load(infile)

            # get the previous session number
            self.session = self.backup[0]["session"]

        # creates new list to be written to file
        log = list()

        self.session = self.session+1
        log_entry = {
                "session": self.session,
                "date": sw.date_string,
                "start time": sw.format_start_time,
                "end time": sw.format_end_time,
                "elapsed time": sw.format_elapsed_time,
                "subject": self.subject,
                "description": "",
        }

        log.append(log_entry)
        # append old list to new list
        if self.backup:
            log = log + self.backup

        json_object = json.dumps(log, indent=4)

        with open(self.log_file, "a") as outfile:
            outfile.write(json_object)

        self.print_stats(sw)

        input("\nPress enter to fill in log...")
        os.system("nvim study_log.json")

    def print_stats(self, sw):
        print("\n\nSession: ", self.session)
        print("Date: ", sw.date_string)
        print("Session started at: ", sw.format_start_time)
        print("Session ended at: ", sw.format_end_time)
        print("Session length: ", sw.format_elapsed_time)
        print()


def main():
    log = Log()
    log.menu()
    log.start_session()


if __name__ == "__main__":
    main()
