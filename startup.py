def startup(os):
    if "main.py" not in os.listdir():
        print("'main.py' not found. \n wrong dir")
        os.chdir(f"{os.getcwd()}/python/final/project")

    print("\n", "*" * 15, "Auto Audit", "*" * 15) 
    input("Press <enter> when ready to scan the Audit Files folder for needed files.")
