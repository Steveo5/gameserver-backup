#!/usr/bin/python3

import yaml
import os
import subprocess
from datetime import datetime
import glob
import rconclient


def backupdir(directory_from, directory_to):
    today = datetime.now()
    today_formatted = today.strftime('%Y-%m-%d_%H:%M:%S')

    directory_to_with_time = directory_to + '_' + today_formatted + '.tar.gz'

    print('backing up to  ' + directory_to_with_time)

    subprocess.call(['tar', '-czf', directory_to_with_time, directory_from])

    return


def cleanupoldbackups(directory, amount_to_keep=5):
    print('Cleaning up old backups from ' + directory)

    files_in_directory = glob.glob(directory + os.path.sep + '*')
    files_in_directory.sort(key=os.path.getmtime)
    files_deleted_count = 0;

    files_in_directory_count = len(files_in_directory)

    while files_in_directory_count > amount_to_keep:
        files_in_directory_count -= 1

        os.remove(files_in_directory[files_deleted_count])

        files_deleted_count += 1

    if files_deleted_count > 0:
        print('Cleaned up ' + str(files_deleted_count) + ' files')

    return


print('Reading backups.yml')
with open(r'backups.yml') as file:
    # The FullLoader parameter handles the conversion from YAML
    # scalar values to Python the dictionary format
    backup_yml_file = yaml.load(file, Loader=yaml.FullLoader)

    for backup in backup_yml_file['backups']:
        name = backup['name']
        directory = backup['directory']
        output_directory = backup['output_directory']
        type = backup['type']
        rconHost = backup['rcon']['host']
        rconPort = backup['rcon']['port']
        rconPass = backup['rcon']['password']

        rcon_client = rconclient.RconClient(rconHost, rconPort, rconPass)

        if type == 'minecraft':
            rcon_client.execute('save-off')
            print('Turning off save for the minecraft server')

        backupdir(directory_from=directory, directory_to=output_directory + os.path.sep + name)
        cleanupoldbackups(directory=output_directory)

        if type == 'minecraft':
            rcon_client.execute('save-on')
            print('Turning on save for the minecraft server')
