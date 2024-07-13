# TO DO: Debug this script. It's still not error free

import re
import os
import shutil
import send2trash
from pathlib import Path

'''
This is a Python script that will detect the English subtitles
for each video in a course folder, change the filename to be the
same as the video and delete all other language subtitle files
'''

# Current working directory is assumed to be the course path
course_path = Path(r'C:\Users\Ashhad\Videos\Udemy - Data Warehouse Fundamentals for Beginners 2020-3')

for folderName, subfolders, files in os.walk(course_path):
    for file in files:
        match = re.search(r'^(.*) English.vtt$', file)
        if match:
            newFilename = match.group(1) + '.vtt'
            shutil.move(str(course_path / file), str(course_path / newFilename))
        if re.search(r'.*\.mp4$', file) or file == 'Readme.txt':
            continue
        else:
            send2trash.send2trash(str(course_path / file))