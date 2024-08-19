---
id: design
aliases: []
tags: []
---

# Possible languages
- python
- bash
- lua??

# Format
Session started at: {time} \ 
Session ended at: {time} \ 
Session length: {length} \

Log: (brief but detailed description of what I did during that time)

# Pomodoro support?
I think I'm just going to assume that pomodoro is being handled separately \
and any breaks during the session will just be ignored

# Core features 
- display a timer that updates in real time
- vim integration - when you end the session, it will open a vim session to \
let you enter the description of what you worked on
- store all the data in JSON (times, length, description)

The idea is that I would just have this open in an inactive tmux window \
which is different that I was planning on last time I tried this. 

# Notes
- Also might want to rebrand this to "study-log" to emphasize that \
this is primarily for my studies, not just random work

# Ideas for more features
- habit tracker - github commit diagram thing but for visually \
tracking sessions
