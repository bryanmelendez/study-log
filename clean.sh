#!/bin/bash

mkdir save

mv -v backup_study_log.yaml save/
mv -v study_log.yaml save/

rm -v backup_study_log.yaml
rm -v study_log.yaml

