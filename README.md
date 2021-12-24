# Gameserver backup
This script will backup the configured directories (in tar.gz format) and place them into another configured directory. There is options for how many backups to keep.

## The backups.yml file   
This file configures the backups. The format is below.   
```
max_backups_to_keep: 3 # max number of each backup to keep

backups:
  - name: 'survival01' # name of the backup (will have date appended)
    directory: '/Users/steven/minecraft/survival01'
    output_directory: '/Users/steven/backup/minecraft'
    type: 'minecraft' # minecraft | other
    rcon: # rcon is used to run commands during the process. E.g. for minecraft it will turn off save and turn save back on after.
      host: '127.0.0.1'
      port: 25575
      password: 'minecraft'
```

## Running the backup script.
The easiest way is to put the script in crontab and execute it as often as you'd like the backups to be created. E.g. for Ubuntu:  
```
0 0,12 * * * cd ~/.minecraft-scripts && screen -dmS backup python3 backup.py
```
Which creates a Minecraft server backup every 12 hours.
