import csv

# TO DO:
# make sure proper indexes are grabbed
def one(hs):
    values = ["Cash (CA)",
    "Check (CK)",
    "American Express (AX)",
    "Discover (DS)",
    "Master Card (MC)",
    "Visa (VS)"
    ]

    hotel_stats = {}
    with open(hs, encoding="utf-8-sig") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if any(row[0].startswith(value) for value in values):
                hotel_stats.update({row[0]: row[4]})

    return hotel_stats



# Credit total? 15
# Guest refund?
# Room Revenue?

