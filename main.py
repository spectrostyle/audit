import os

import startup
import fileOperations
import getValues


def main():
    if "main.py" not in os.listdir():
        print("wrong dir")
        os.chdir(f"{os.getcwd()}/python/final/project")

    reports_file = f"{os.getcwd()}/AuditFiles"
    found_files = f"{os.getcwd()}/FoundFiles"
    template = f"{os.getcwd()}/Template/SummaryTemplate.HTML"
    #

    startup.startup()
    fileOperations.clean(found_files, os)
    fileOperations.find_move(reports_file, found_files, os)

    summary = {}
    for report in os.listdir(found_files):
        summary.update(getValues.get_values(f"{found_files}/{report}"))

    print(summary)


main()
