import pandas as pd

# Read the three csv files provided
booking = pd.read_csv('cleveland_booking_logs.csv')
cancel = pd.read_csv('cleveland_cancel_logs.csv')
shifts = pd.read_csv('cleveland_shifts.csv')

# Total shifts
total_shifts = shifts.shape[0]
# Total number of shifts deleted by the healthcare facility (HCF Deleted)
deleted_shifts = shifts[shifts['Deleted'] == True].shape[0]
# Total non-deleted shifts (Number of shifts not deleted by the healthcare facility)
non_deleted_shifts = shifts[shifts['Deleted'] != True]
non_deleted_count = non_deleted_shifts.shape[0]
# Total worked/fulfilled shifts (Verified shifts)
fulfilled_shifts = non_deleted_shifts[(non_deleted_shifts['Agent ID'].notnull())].shape[0]
# Total booked and unfulfilled shifts (Booked but not verified shifts)
unfulfilled_shifts = non_deleted_count - fulfilled_shifts

# Print the results
print("Total Shifts:", total_shifts)
print("HCF Deleted Shifts:", deleted_shifts)
print("Percentage of HCF deleted shifts:", round((deleted_shifts / total_shifts) * 100, 2),"%")
print("Non-deleted Shifts:", non_deleted_count)
print("Fulfilled Shifts:", fulfilled_shifts)
print("Percentage of fulfilled shifts:", round((fulfilled_shifts / non_deleted_count) * 100, 2),"%")
print("Unfulfilled Shifts:", unfulfilled_shifts)
print("Percentage of unfulfilled shifts:", round((unfulfilled_shifts / non_deleted_count) * 100, 2),"%")
