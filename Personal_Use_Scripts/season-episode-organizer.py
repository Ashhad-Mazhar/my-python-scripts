import re
import shutil
from pathlib import Path


'''
This is a Python script that organizes my season episodes files
following a certain naming convention by extracting the season
name, season number, and episode number from the file names. It 
arranges them into structured folders in my computer's Videos
folder.
'''


def Create_Directory(directory_path):
    if not Path.is_dir(directory_path):
        Path.mkdir(directory_path)
        print(f'{directory_path.name} folder created')

videos_folder_path = Path.home() / 'Videos'

Create_Directory(videos_folder_path / 'Seasons')

seasons_folder_path = videos_folder_path / 'Seasons'

# Example file name matching this regex:
# Breaking.Bad.S01E01.720p.x264.Bluray.Hindi.English.Esubs.MoviesMod.org.mkv
# This file will organized into the folder:
# Seasons -> Breaking Bad -> Season 01 -> Episode 01
season_regex = re.compile(r'^(.+)\.(S\d{2})(E\d{2}).*$')

for file in Path.cwd().glob('*.mkv'):
    # Checking to see if the object is a file, not a directory
    print('File matched')
    if file.is_file():
        match = season_regex.match(file.name)

        season_name = match.group(1).replace('.', ' ')
        season_number = match.group(2).replace('S', 'Season ')
        episode_number = match.group(3).replace('E', 'Episode ')

        season_directory = seasons_folder_path / season_name
        season_number_directory = season_directory / season_number

        Create_Directory(seasons_folder_path / season_name)
        Create_Directory(seasons_folder_path / season_name / season_number)

        shutil.copy(file, str(season_number_directory / (episode_number + '.mkv')))

        print('File copied')