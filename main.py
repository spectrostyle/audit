import os

import startup
import fileOperations
import hotelStatistics


def main():
    if "main.py" not in os.listdir():
        print("wrong dir")
        os.chdir(f"{os.getcwd()}/python/final/project")


    found_files = f"{os.getcwd()}/FoundFiles"
    reports_file = f"{os.getcwd()}/AuditFiles"


    startup.startup()
    fileOperations.clean(found_files)
    fileOperations.find_move(reports_file, found_files)

    hotel_Stats = hotelStatistics.one(f"{found_files}/HotelStatistics.csv")




main()
