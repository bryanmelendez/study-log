#!/bin/bash

SAVE_PATH="$notes/1-personal/study-log"

if [ -f "$SAVE_PATH/study_log.md" ]; then
    echo "Creating a backup"
    cp $SAVE_PATH/study_log.md $SAVE_PATH/backup.md
fi
echo "Saving file to $SAVE_PATH"
cp -v study_log.yaml $SAVE_PATH
mv -v $SAVE_PATH/study_log.yaml $SAVE_PATH/study_log.md
