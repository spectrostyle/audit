import csv

# Scans hotel statistic for relevant pairs
# Returns a dictionary
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
                    "Room Charge (RM)",
                    "Total For CREDIT CARDS: "
                    ]
            key_total = len(keys)
            for row in reader:
                if key_total == -2: # -2 for ptd, ytd
                    break
                if any(row[0].startswith(key) for key in keys):
                    # if not row[4].startswith("(")) then negative?
                    hotel_stats.update({row[0]: float(row[4].strip("()").replace(",",""))})
                    key_total -= 1
                if row[0].startswith("Total For ROOM REVENUE"):
                    hotel_stats.update({"PTD": float(row[5].strip("()").replace(",",""))})
                    hotel_stats.update({"YTD": float(row[6].strip("()").replace(",",""))})
                    key_total -= 1
            return hotel_stats


        if report.endswith("FTC.csv"):
            ftc_dict = {}
            keys = [f"Occupancy Statistics_STR Occ% of Total Rooms",
                    "Occupancy Statistics_ADR for Total Revenue Rooms",
                    "Room Statistics_Out Of Order",
                    "Stay Over Rooms",
                    "Day Use Rooms"
                    ]
            key_total = len(keys)
            rows = list(reader)
            headers = rows[0]
            values = rows[1]

            for idx, header in enumerate(headers):
                if key_total == 0:
                    break
                if header in keys:
                    ftc_dict[header] = values[idx]
                    key_total -= 1
            return ftc_dict
