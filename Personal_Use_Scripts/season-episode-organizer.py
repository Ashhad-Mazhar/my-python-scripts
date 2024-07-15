import re
import os
import shutil
import zipfile
from pathlib import Path


'''
This is a Python script that organizes my season episodes files
following a certain naming convention by extracting the season
name, season number, and episode number from the file names. It 
arranges them into structured folders in my computer's Videos
folder.
'''
def main():
    destination_path = Path.home() / 'Videos'
    seasons_folder_path = destination_path / 'Seasons'
    mkv_files_source_path = Path.home() / 'Downloads' / 'Video'
    zip_files_source_path = Path.home() / 'Downloads' / 'Compressed'

    Create_Directory(destination_path / 'Seasons')
    Create_Directory(destination_path / 'Movies')

    Move_Season_Files(mkv_files_source_path, seasons_folder_path)
    Move_Season_Files_Zip(zip_files_source_path, seasons_folder_path)




def Create_Directory(directory_path: Path):
    if not Path.is_dir(directory_path):
        Path.mkdir(directory_path)
        print(f'{directory_path.name} folder created')

def Move_Season_Files_Zip(source_path: Path, seasons_folder_path: Path):
    for file in source_path.glob('*.zip'):
        if file.is_file():
            extract_path = source_path / file.stem
            if not extract_path.is_dir():
                episodes_zip = zipfile.ZipFile(file)
                episodes_zip.extractall(extract_path)
                episodes_zip.close()

            extracted_folders = [folder for folder in extract_path.iterdir() if folder.is_dir()]

            if extracted_folders:
                extracted_folder_path = extracted_folders[0]
                Move_Season_Files(extracted_folder_path, seasons_folder_path)

def Move_Season_Files(source_path: Path, seasons_folder_path: Path):
    # Example file name matching this regex:
    # Breaking.Bad.S01E01.720p.x264.Bluray.Hindi.English.Esubs.MoviesMod.org.mkv
    # This file will be organized like this:
    # Seasons -> Breaking Bad -> Season 01 -> Episode 01.mkv
    season_regex_string = r'^(.+)\.(S\d{2})(E\d{2}).*$'
    season_regex = re.compile(season_regex_string)

    for file in source_path.glob('*.mkv'):
    # Checking to see if the object is a file, not a directory
        if file.is_file():
            season_filename_match = season_regex.match(file.name)

            if season_filename_match:
                season_name = season_filename_match.group(1).replace('.', ' ')
                season_number = season_filename_match.group(2).replace('S', 'Season ')
                episode_number = season_filename_match.group(3).replace('E', 'Episode ')

                season_directory = seasons_folder_path / season_name
                season_number_directory = season_directory / season_number

                Create_Directory(seasons_folder_path / season_name)
                Create_Directory(seasons_folder_path / season_name / season_number)

                if not (season_number_directory / (episode_number + '.mkv')).is_file():
                    shutil.copy(file, str(season_number_directory / (episode_number + '.mkv')))
                    print(f'{os.path.join(season_directory.name, season_number_directory.name, (episode_number + '.mkv'))} copied')

            else:
                print(f'Unsupported .mkv file found: {file.name}')


# Calling the main function
if __name__ == "__main__":
    main()