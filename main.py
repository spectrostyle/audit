import os

import startup
import fileOperations
import getValues


def main():
    if "main.py" not in os.listdir():
        print("wrong dir")
        os.chdir(f"{os.getcwd()}/python/final/project")

    reports_file = f"{os.getcwd()}/AuditFiles"
    found_files = f"{os.getcwd()}/FoundFiles"
    template = f"{os.getcwd()}/Template/SummaryTemplate.html"


    startup.startup()
    fileOperations.clean(found_files, os)
    fileOperations.find_move(reports_file, found_files, os)

    summary = {}
    for report in os.listdir(found_files):
        summary.update(getValues.get_values(f"{found_files}/{report}"))

    with open(template, 'r', encoding='utf-8-sig') as file:
        audit_summary = file.read()

        empty = 0
        new_summary = audit_summary.replace('Rooms Sold:', f'Rooms Sold: (int({summary["Stay Over Rooms"]}) + int({summary["Day Use Rooms"]}))'
                                  ).replace('Occupancy: %', f'Occupancy: {summary["Occupancy Statistics_STR Occ% of Total Rooms"]}'
                                  ).replace('Out of Order Rooms:', f'Out of Order Rooms: {summary["Room Statistics_Out Of Order"]}'
                                  ).replace('ADR: $', f'ADR: $ {summary["Occupancy Statistics_ADR for Total Revenue Rooms"]}'
                                  ).replace('Room Revenue: $', f'Room Revenue: $ {summary["Room Charge (RM)"]}'
                                  ).replace('Cash: $', f'Cash: $ {summary["Cash (CA)"]:.2f}'
                                  ).replace('AMEX: $', f'AMEX: $ {summary["American Express (AX)"]:.2f}'
                                  ).replace('Check: $', f'Check: $ {summary["Check (CK)"]:.2f}'
                                  ).replace('Discover(NS): $', f'Discover(NS): $ {summary["Discover (DS)"]:.2f}'
                                  ).replace('Guest Refund: $', f'Guest Refund: $ {empty}'
                                  ).replace('Mastercard: $', f'Mastercard: $ {summary["Master Card (MC)"]:.2f}'
                                  ).replace('Visa: $', f'Visa: $ {summary["Visa Payment (VI)"]:.2f}'
                                  ).replace('Credit Total: $', f'Credit Total: {summary["Total For CREDIT CARDS: "]:.2f}'
                                  ).replace('Month to Date: $', f'Month to Date: $ {summary["PTD"]:.2f}'
                                  ).replace('Year to Date: $', f'Year to Date: $ {summary["YTD"]:.2f}')


        with open(template, 'w', encoding='utf-8') as file:
            file.write(new_summary)
            print('Audit Complete.')


main()
