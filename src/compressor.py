import os
import shutil

def generate_backup(SOURCE, DESTINATION, FILE_TYPE, backup_name):
    if not SOURCE.exists():
        print("INVALID SOURCE PATH, PROGRAM TERMINATED")
        exit()

    backup_path = os.path.join(DESTINATION, backup_name)

    if FILE_TYPE == "1":
        shutil.make_archive(backup_path, 'zip', root_dir=str(SOURCE))
    elif FILE_TYPE == "2":
        shutil.make_archive(backup_path, 'gztar', root_dir=str(SOURCE))
    elif FILE_TYPE == "3":
        shutil.make_archive(backup_path, 'bztar', root_dir=str(SOURCE))
    else:
        print("Invalid file type. Using ZIP by default.")
        shutil.make_archive(backup_path, 'zip', root_dir=str(SOURCE))

    print(f"✅ Backup done: {backup_path}.{FILE_TYPE}")
