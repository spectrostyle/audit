import csv

# row[0] for the Key
# row[4] for value "Today's Net"
# row[5] for value "PTD Totals"
# row[6] for value "YTD Totals"

# Scans hotel statistic for relevant pairs
# Returns a dictionary
# TO DO:
# make sure proper indexes are grabbed
# will prob throw error with negative but for now fine
def one(hs):
    values = ["Cash (CA)",
    "Check (CK)",
    "American Express (AX)",
    "Discover (DS)",
    "Master Card (MC)",
    "Visa Payment (VI)",
    "Room Charge (RM)"
    ]

    hotel_stats = {}
    with open(hs, encoding="utf-8-sig") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if any(row[0].startswith(value) for value in values):
                # if not row[4].startswith("(")) then negative?
                hotel_stats.update({row[0]: float(row[4].strip("()").replace(",",""))})
            if row[0].startswith("Total For ROOM REVENUE"):
                hotel_stats.update({"PTD": row[5]})
                hotel_stats.update({"YTD": row[6]})

    return hotel_stats

# Guest refund?

