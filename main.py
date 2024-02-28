import osimport shutil
from datetime import datetime
from plyer import notification


username = os.getlogin()


def nowtime():
    time = datetime.now()
    now = time.date()
    return nowclass BackUp:
    with open(f'C:\\Users\\{username}\\BACKUP\\config.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
        source_dir = lines[0]        
        sources = source_dir.split('=')
        source = sources[1].strip()

        backup_dir = lines[1]
        backups = backup_dir.split('=')
        backup = backups[1].strip()

    try:
        shutil.copytree(f'{source}', f'{backup}/Backup/{nowtime()}')
        notification.notify(title="백업 관리자", message="백업이 완료되었습니다", timeout=5)
        pass
    except FileExistsError:
        notification.notify(title="백업 관리자", message=f"오늘은 이미 백업이 되어있습니다\n마지막 백업일자 {nowtime()}", timeout=5)
