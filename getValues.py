import csv



# Scans hotel statistic for relevant pairs
# Returns a dictionary
# row[0] for the Key
# row[4] for values "Today's Net" for Keys
# row[5] for value "PTD Totals"
# row[6] for value "YTD Totals"
# TO DO:
# make sure proper indexes are grabbed
# will prob throw error with negative but for now fine
# Guest refund?
def get_values(report):
    with open(report, encoding="utf-8-sig") as csvfile:
        reader = csv.reader(csvfile)

        if report.endswith("HotelStatistics.csv"):
            hotel_stats = {}
            keys = ["Cash (CA)",
                    "Check (CK)",
                    "American Express (AX)",
                    "Discover (DS)",
                    "Master Card (MC)",
                    "Visa Payment (VI)",
                    "Room Charge (RM)"
                    ]
            for row in reader:
                if any(row[0].startswith(key) for key in keys):
                    # if not row[4].startswith("(")) then negative?
                    hotel_stats.update({row[0]: float(row[4].strip("()").replace(",",""))})
                if row[0].startswith("Total For ROOM REVENUE"):
                    hotel_stats.update({"PTD": float(row[5].strip("()").replace(",",""))})
                    hotel_stats.update({"YTD": float(row[6].strip("()").replace(",",""))})

            return hotel_stats

        if report.endswith("FTC.csv"):
            for row in reader:
                for x in row:
                    print(x)

# occupancy
# rooms sold
# adr
# ooo


