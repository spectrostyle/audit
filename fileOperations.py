import csv
import shutil


# Searches AuditFiles folder for certain csvs, labels csv accordingly
# moves csv to FoundFiles folder for processing.
# Should only search first row, files unchanging positions.
# TO DO:
# 
def find_move(reports_file, found_files, os):
    for file in os.listdir(reports_file):
        found_file = None

        if file.startswith("Export-"):
            found_file = "Transaction Report"

        else:
            with open(f"{reports_file}/{file}", encoding="utf-8-sig") as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:         
                    for entry in row:

                        if entry == "Description (Transaction Code)":
                            found_file = "Hotel Statistics"
                        if entry.startswith("Business Date: "):
                            found_file = "Final Transaction Closeout"
                            
                        break
                    break

        if found_file:
            print(f"Found {found_file}. Renaming and moving to {found_files}/{found_file.replace(' ', '')}.csv")
            shutil.copy(f"{reports_file}/{file}", f"{found_files}/{found_file.replace(' ', '')}.csv")
        else:
            print(f"No name found for {file}")         


# If files exist from previous Audit, delete those files with permission
# TO DO:
# 
def clean(found_files, os):
    if os.listdir(found_files):
        print(f"Found", ", ".join(os.listdir(found_files)), "from yesterday.")

        permission = input("\nDelete these files before continuing? (y/n): ").lower()
        if permission == 'y': 
            for file in os.listdir(found_files):
                print(f"\nDeleting {file}...")
                os.remove(f"{found_files}/{file}")    
        else:
            print("Files not deleted. Exiting program to prevent errors.")
            exit()
