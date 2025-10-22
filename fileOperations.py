import csv
import shutil


# Searches specified file for certain csvs, labels csv accordingly,
# and moves csv to new seperate folder for processing.
# Should only search first row, files unchanging positions.
# TO DO:
# find transaction report and move (one if statement)
# setup os date time
def find_move(reports_file, found_files, os):
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
                        if entry == "Business Date: 10/20/2025":
                            found = True
                            found_file = "FTC"
                            break
                        break
                    print(f"Found {found_file}. Renaming and moving to {found_files}/{found_file}.csv")
                    shutil.copy(f"{reports_file}/{file}", f"{found_files}/{found_file}.csv")


# If files exist from previous Audit, delete those files with permission
# TO DO:
# input handling for yes/no?
def clean(found_files, os):
    if os.listdir(found_files):
        print(f"Found", ", ".join(os.listdir(found_files)), "from yesterday")

        print("Deleting...\n")
        for file in os.listdir(found_files):
            os.remove(f"{found_files}/{file}")
