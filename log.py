import yaml
import os
from study_stats import StudyStats
from stopwatch import Stopwatch
from settings import Settings


class Log:
    def __init__(self):
        self.log_file = "study_log.yaml"
        self.backup_file = "backup_study_log.yaml"
        self.backup = None
        self.backup_text = None
        self.subject = None
        self.session = 0
        self.log = None
        self.yaml_object = None

    def menu(self):
        # example
        settings = Settings()
        settings.get_settings()

        print("Subjects:")
        for i in range(0, len(settings.subjects)):
            print("{}. {}".format(i+1, settings.subjects[i]))

        quit_num = len(settings.subjects)+1
        print("{}. Quit".format(quit_num))

        choice = int(input("Which subject are you studying?\t"))
        if choice == quit_num:
            exit()
        elif choice > 0 and choice <= len(settings.subjects):
            self.subject = settings.subjects[choice-1]

    def start_session(self):
        sw = Stopwatch()

        sw.start()

        # rename the log file to backup file
        # then read from the backup
        if os.path.exists(self.log_file):
            os.rename(self.log_file, self.backup_file)
            # this file read is for the yaml load
            with open(self.backup_file, "r") as infile:
                self.backup = yaml.safe_load(infile)

            # this file read is for the utf-8 string load
            with open(self.backup_file, "r", encoding='utf-8') as text_file:
                self.backup_text = text_file.read()

            # get the previous session number
            self.session = self.backup[0]["Session"]

        # creates new list to be written to file
        self.log = list()

        self.session = self.session+1
        log_entry = {
                "Session": self.session,
                "Date": sw.date_string,
                "Session started at": sw.format_start_time,
                "Session ended at": sw.format_end_time,
                "Session length": sw.format_elapsed_time,
                "Subject": self.subject,
                "Log": ' ',
        }

        self.log.append(log_entry)

        self.yaml_object = yaml.dump(self.log, sort_keys=False)

        with open(self.log_file, "a") as outfile:
            outfile.write(self.yaml_object)
            outfile.write('\n')
            if self.backup_text:
                outfile.write(self.backup_text)

        self.print_stats(sw)

        input("\nPress enter to fill in log...")
        os.system("nvim study_log.yaml")

    def print_stats(self, sw):
        print("\n\nSession: ", self.session)
        print("Date: ", sw.date_string)
        print("Session started at: ", sw.format_start_time)
        print("Session ended at: ", sw.format_end_time)
        print("Session length: ", sw.format_elapsed_time)
        print()


def main():
    debug = False

    log = Log()
    log.menu()
    log.start_session()

    if (debug):
        stats = StudyStats()
        description = stats.getDescription(log_array=log.log, session_id=1)
        print(description)


if __name__ == "__main__":
    main()
