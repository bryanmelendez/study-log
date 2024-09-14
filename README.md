This is a CLI interface for tracking study/work sessions. This includes a basic \
stopwatch and will automatically log start/end times as well as total time. \
The data is stored as a .yaml file to maintain organization and accessibility of \
the data, as well as for readability. Seperate from this program, I save a copy \
of the outputted .yaml log as a .md file to keep in my personal notes system. \

# Dependencies
- PyYaml

# Usage (as of right now)
- Edit the SAVE_PATH var in save.sh script 
- Run ```python log.py``` in your python environment
- Run ```python study_stats.py``` to calculate your study stats (not finished)

# TODO
- [x] basic yaml file log
- [x] display the elasped time in terminal
- [ ] implement stats to track total time, weekly sessions, etc
- [ ] implement a settings file to let you specify study topics and other options

# Ideas
- calculate the stats starting from a certain date (to see how many hours were \
    spent studying during a school term or for an exam)
