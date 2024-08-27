import json
import os
from stopwatch import Stopwatch

log_file = "study_log.json"
backup_file = "backup_study_log.json"
backup = None
session = 0

# Driver code
sw = Stopwatch()

sw.start()
sw.print_stats()

if os.path.exists(log_file):
    os.rename(log_file, backup_file)
    with open(backup_file, "r") as infile:
        backup = json.load(infile)

    session = backup[0]["session"]
    print("Session: ", session)

# creates new list to be written to file
log = list()

log_entry = {
        "session": session+1,
        "date": sw.date_string,
        "start time": sw.format_start_time,
        "end time": sw.format_end_time,
        "elapsed time": sw.format_elapsed_time,
        "description": "",
}

log.append(log_entry)
# append old list to new list
if backup:
    log = log + backup
print(log)

json_object = json.dumps(log, indent=4)

with open(log_file, "a") as outfile:
    outfile.write(json_object)

os.system("nvim study_log.json")
