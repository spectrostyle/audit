import csv
import shutil
import os


def find_move(reports_file, found_files):
    for file in os.listdir(reports_file):

            found = False
            with open(f"{reports_file}/{file}", encoding="utf-8-sig") as csvfile:
                reader = csv.reader(csvfile)

                for row in reader:
                    if found:
                        break

                    for entry in row:
                        if entry == "Description (Transaction Code)":
                            found = True
                            found_file = "HotelStatistics"
                            break
                        if entry == "Business Date: 10/19/2025":
                            found = True
                            found_file = "FTC"
                            break
                    shutil.copy(f"{reports_file}/{file}", f"{found_files}/{found_file}.csv")


def clean(found_files):
    if os.listdir(found_files):
        print("Cleaning up files from yesterday's scan...\n")
        for file in os.listdir(found_files):
            os.remove(f"{found_files}/{file}")
