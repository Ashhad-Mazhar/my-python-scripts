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

course_path = Path.home() / 'Videos' / 'Data_Warehouse_Fundamentals_for_Beginners'

for folderName, subfolders, files in os.walk(course_path):
    for file in files:
        match = re.search(r'^(.*) English.vtt$', file)
        if match:
            newFilename = match.group(1) + '.vtt'
            shutil.move(os.path.join(folderName, file), os.path.join(folderName, newFilename))
            print(f'{file} renamed to {newFilename}')
        elif re.search(r'.*\.vtt', file):
            send2trash.send2trash(os.path.join(folderName, file))
            print(f'{file} sent to recycle bin')
        print()