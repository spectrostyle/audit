import os

import startup
import fileOperations


def main():
    found_files = f"{os.getcwd()}/FoundFiles"
    reports_file = f"{os.getcwd()}/AuditFiles"


    startup.startup()
    fileOperations.clean(found_files)

    fileOperations.find_move(reports_file, found_files)




main()
