import shutil


# If files exist from previous Audit, delete those files with permission
def clean(FoundFiles, os):
    print(f"\nChecking for yesterday's Audit in {FoundFiles}...")

    if os.listdir(FoundFiles):
        print(f"\nFound the following:\n[", ", ".join(os.listdir(FoundFiles)), "]")

        permission = input("\nDelete these files before continuing? (y/n): ").lower()
        print("")

        if permission == 'y': 
            for file in os.listdir(FoundFiles):
                print(f"Deleting {file}...")
                os.remove(f"{FoundFiles}/{file}")    
        else:
            print("Files not deleted. Exiting program to prevent errors.")
            exit()
            
    input(f"\n{FoundFiles} is clean. Press <enter> to continue.\n")


# Searches AuditFiles first row, copies matching files to FoundFiles.
def find_move(AuditFiles, FoundFiles, os, csv):
    print(f"\nScanning {AuditFiles}...\n")
    for file in os.listdir(AuditFiles):
        print(f"Scanning {file}...")
        found_file = None

        if file.startswith("Export-"):
            found_file = "Transaction Report"

        else:
            with open(f"{AuditFiles}/{file}", encoding="utf-8-sig") as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:         
                    for entry in row:

                        if entry == "Description (Transaction Code)":
                            found_file = "Hotel Statistics"
                        if entry.startswith("Business Date: "):
                            found_file = "Final Transaction Closeout"
                        if entry.startswith("Transaction Code"):
                            found_file = "Hotel Journal Summary"
                        break
                    break

        if found_file:
            print(f"Found: [{found_file}]. \nMoving to: {FoundFiles}/{found_file.replace(' ', '')}.csv\n")
            shutil.move(f"{AuditFiles}/{file}", f"{FoundFiles}/{found_file.replace(' ', '')}.csv")
        else:
            print(f"No name found for {file}!\n")
    
    input("Moving files complete. Press <enter> to continue.\n")
