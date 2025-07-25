from pathlib import Path
from utils import naming_func
from compressor import generate_backup

SOURCE = Path(input("Please enter the Source Path- \n"))
DESTINATION = "/your/path/to/backup_folder"
FILE_TYPE = input("Please enter the FILE_TYPE (ZIP(1), TAR.ZIP(2) OR TAR.BZ2(3)): ")
naming_option = input("Please enter the name of the new backup file else write '0': ").strip().lower()

backup_name = naming_func(naming_option)
generate_backup(SOURCE, DESTINATION, FILE_TYPE, backup_name)
