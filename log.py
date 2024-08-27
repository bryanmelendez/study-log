import json
import os
from stopwatch import Stopwatch

log_file = "study_log.json"
backup_file = "backup_study_log.json"
backup = None

# Driver code
sw = Stopwatch()

sw.start()
sw.print_stats()

log = {
        "start time": sw.format_start_time,
        "end time": sw.format_end_time,
        "elapsed time": sw.format_elapsed_time,
        "description": "",
}

if os.path.exists(log_file):
    os.rename(log_file, backup_file)
    with open(backup_file, "r") as infile:
        backup = infile.read()

json_object = json.dumps(log, indent=4)

with open(log_file, "a") as outfile:
    outfile.write(json_object)
    if backup:
        outfile.write("\n")
        outfile.write(backup)

os.system("nvim study_log.json")
