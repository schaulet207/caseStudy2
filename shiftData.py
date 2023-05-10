import pandas as pd

# Read the three csv files provided
booking = pd.read_csv('cleveland_booking_logs.csv')
cancel = pd.read_csv('cleveland_cancel_logs.csv')
shifts = pd.read_csv('cleveland_shifts.csv')

# Determine the shift and cancel logs lowest and highest start date
lowest_start_date = shifts['Start'].min()
cancel_lowest_start_date = cancel['Shift Start Logs'].min()
highest_start_date = shifts['Start'].max()
cancel_highest_start_date = cancel['Shift Start Logs'].max()

# Print data ranges
print("Shift logs lowest start date:", lowest_start_date)
print("Shift logs highest start date:", highest_start_date)
print("Cancel logs lowest start date:", cancel_lowest_start_date)
print("Cancel logs highest start date:", cancel_highest_start_date)

# Filter to determine the rows where the "Verified" column is True or False
verified_shifts = shifts[shifts['Verified'] == True]
unverified_shifts = shifts[shifts['Verified'] == False]
# Filter to determine only the rows where the "Deleted" column is True
deleted_shifts = shifts[shifts['Deleted'] == True]

# Sum the number of verified & unverified shifts
total_verified_shifts = len(verified_shifts)
total_unverified_shifts = len(unverified_shifts)
# Total number of shifts created by HCF
total_shifts = shifts.shape[0]
# Number of shifts deleted by the HCF
deleted_shifts_count = deleted_shifts.shape[0]
# The total number of shifts MINUS the number of shifts deleted
total_booked_shifts = total_shifts - deleted_shifts_count
# The total number of shifts booked by HCPs MINUS the number of shifts worked
total_unfulfilled = total_booked_shifts - total_verified_shifts

# Print the results
print("Total number of shifts created by HCF:", total_shifts)
print("Total percentage of shifts cancelled by HCF:", round((deleted_shifts_count / total_shifts) * 100, 2),"%")
print("Total percentage of shifts booked by HCPs:", round((total_booked_shifts / total_shifts) * 100, 2),"%")
print("Total percentage of fulfilled shifts:", round((total_verified_shifts / total_shifts) * 100, 2),"%")
print("Total percentage of unfulfilled shifts:", round((total_unfulfilled / total_shifts) * 100, 2),"%")
print(shifts.head(3))