import subprocess
import os
from rich.console import Console
from rich.table import Table

menu_options = {
    '1': 'Start All Torrents',
    '2': 'Status of Incomplete Torrents',
    '3': 'Status of All Torrents',
    '4': 'Clean Torrent Directories',
    '5': 'Locate Duplicate Movies',
    '6': 'Reload ZSH',
    '7': 'Show All DNS Records',
    '8': 'Restart VM',
    '9': 'Backup VM',
    '10': 'Start VM',
    '11': 'Backup Prom Config',
    '12': 'Show Recent Spotify Tracks',
    '13': 'Update All RPis',
    '14': 'Recent PiHole Blocks',
    '15': 'Tail Ansible',
    '16': 'Tail Jellyfin',
    '17': 'Tail Untangle',
    '18': 'Wireless Status',
    '19': 'Switch Status',
    '20': 'Mount NAS Drives',
    '21': 'Exit',
}

table = Table(title="Alias Launch Menu")
table.add_column("Alias", justify="center", style="cyan")
table.add_column("Description", justify="left", style="green")
print('\n')


def print_menu():
    for key in menu_options.keys():
        table.add_row(key, menu_options[key])


def option1():
    print('\n')
    os.system('/Users/$USER/scripts/sh/start_all_torrents.sh')
    print('\n')


def option2():
    print('\n')
    os.system('/Users/$USER/scripts/sh/status_of_incomplete_torrents.sh')
    print('\n')


def option3():
    print('\n')
    os.system('/Users/$USER/scripts/sh/status_of_all_torrents.sh')
    print('\n')


def option4():
    print('\n')
    os.system('/Users/$USER/scripts/sh/clean_torrent_directories.sh')
    print('\n')


def option5():
    print('\n')
    os.system('/Users/$USER/scripts/sh/locate_duplicate_movies.sh')
    print('\n')


def option6():
    print('\n')
    os.system('/Users/$USER/scripts/sh/reload_zsh.sh')
    print('\n')


def option7():
    print('\n')
    os.system('/Users/$USER/scripts/sh/show_all_dns_records.sh')
    print('\n')


def option8():
    print('\n')
    os.system('/Users/$USER/scripts/sh/restart_vm.sh')
    print('\n')


def option9():
    print('\n')
    os.system('/Users/$USER/scripts/sh/backup_vm.sh')
    print('\n')


def option10():
    print('\n')
    os.system('/Users/$USER/scripts/sh/start_vm.sh')
    print('\n')


def option11():
    print('\n')
    os.system('/Users/$USER/scripts/sh/backup_prom_config.sh')
    print('\n')


def option12():
    print('\n')
    subprocess.run(['python', f"/Users/{os.environ['USER']}/scripts/python/recent_tracks.py"])
    print('\n')


def option13():
    print('\n')
    os.system('/Users/$USER/scripts/sh/update_all_rpis.sh')
    print('\n')


def option14():
    print('\n')
    os.system('/Users/$USER/scripts/sh/pihole_blocks.sh')
    print('\n')


def option15():
    print('\n')
    os.system('/Users/$USER/scripts/sh/tail_ansible.sh')
    print('\n')


def option16():
    print('\n')
    os.system('/Users/$USER/scripts/sh/jellyfin.sh')
    print('\n')


def option17():
    print('\n')
    os.system('/Users/$USER/scripts/sh/untangle_query.sh')
    print('\n')


def option18():
    print('\n')
    subprocess.run(['python', f"/Users/{os.environ['USER']}/scripts/python/wireless.py"])
    print('\n')


def option19():
    print('\n')
    subprocess.run(['python', f"/Users/{os.environ['USER']}/scripts/python/switches.py"])
    print('\n')


def option20():
    print('\n')
    os.system('/Users/$USER/scripts/sh/nas.sh')
    print('\n')


if __name__ == '__main__':
    print_menu()
    console = Console()
    console.print(table)
    option = ''
    try:
        option = str(input('Select an alias ' + '[1 - ' + str(len(menu_options)) + ']: '))
    except:
        print('Wrong input. Please enter a number ...')
    if option == '1':
        option1()
    elif option == '2':
        option2()
    elif option == '3':
        option3()
    elif option == '4':
        option4()
    elif option == '5':
        option5()
    elif option == '6':
        option6()
    elif option == '7':
        option7()
    elif option == '8':
        option8()
    elif option == '9':
        option9()
    elif option == '10':
        option10()
    elif option == '11':
        option11()
    elif option == '12':
        option12()
    elif option == '13':
        option13()
    elif option == '14':
        option14()
    elif option == '15':
        option15()
    elif option == '16':
        option16()
    elif option == '17':
        option17()
    elif option == '18':
        option18()
    elif option == '19':
        option19()
    elif option == '20':
        option20()
    elif option == '21':
        print('Bye!')
        exit()
    else:
        print('Invalid option!')
