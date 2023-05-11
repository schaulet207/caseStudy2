import pandas as pd

# Read the three csv files provided
booking = pd.read_csv('cleveland_booking_logs.csv')
cancel = pd.read_csv('cleveland_cancel_logs.csv')
shifts = pd.read_csv('cleveland_shifts.csv')

# SHIFT DATA CALCULATIONS
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

# CANCELLATION DATA CALCULATIONS
# Filter to determine the rows where an NCNS occurs
ncns = cancel[cancel['Action'] == 'NO_CALL_NO_SHOW']
# Filter to determine the rows where a call off occurs
call_off = cancel[cancel['Action'] == 'WORKER_CANCEL']

# Sum the total number of shifts
total_called_off_shifts = cancel.shape[0]
# Sum the number of NCNS shifts
total_ncns = len(ncns)
# Sum the number of call-off shifts
total_call_off = len(call_off)

# Select the rows where 'Action' = 'WORKER_CALL_OFF' and 'Lead Time' is between 0 and 1 hours
lead_time_filtered_0_1 = cancel[(cancel['Action'] == 'WORKER_CANCEL') & (cancel['Lead Time'] >= 0) & (cancel['Lead Time'] <= 1)]
# Select the rows where 'Action' = 'WORKER_CALL_OFF' and 'Lead Time' is between 1 and 2 hours
lead_time_filtered_1_2 = cancel[(cancel['Action'] == 'WORKER_CANCEL') & (cancel['Lead Time'] >= 1) & (cancel['Lead Time'] <= 2)]
# Select the rows where 'Action' = 'WORKER_CALL_OFF' and 'Lead Time' is between 2 and 3 hours
lead_time_filtered_2_3 = cancel[(cancel['Action'] == 'WORKER_CANCEL') & (cancel['Lead Time'] >= 2) & (cancel['Lead Time'] <= 3)]
# Select the rows where 'Action' = 'WORKER_CALL_OFF' and 'Lead Time' is between 3 and 4 hours
lead_time_filtered_3_4 = cancel[(cancel['Action'] == 'WORKER_CANCEL') & (cancel['Lead Time'] >= 3) & (cancel['Lead Time'] <= 4)]
# Select the rows where 'Action' = 'WORKER_CALL_OFF' and 'Lead Time' is between 4 and 24 hours
lead_time_filtered_4_12 = cancel[(cancel['Action'] == 'WORKER_CANCEL') & (cancel['Lead Time'] >= 4) & (cancel['Lead Time'] <= 12)]
# Select the rows where 'Action' = 'WORKER_CALL_OFF' and 'Lead Time' is between 4 and 24 hours
lead_time_filtered_12_24 = cancel[(cancel['Action'] == 'WORKER_CANCEL') & (cancel['Lead Time'] >= 12) & (cancel['Lead Time'] <= 24)]
# Select the rows where 'Action' = 'WORKER_CALL_OFF' and 'Lead Time' is greater than 24 hours
lead_time_filtered_24 = cancel[(cancel['Action'] == 'WORKER_CANCEL') & (cancel['Lead Time'] >= 24)]

# Sum the number of shifts called off between 0-1 hours prior
zero_one = lead_time_filtered_0_1.shape[0]
# Sum the number of shifts called off between 1-2 hours prior
one_two = lead_time_filtered_1_2.shape[0]
# Sum the number of shifts called off between 2-3 hours prior
two_three = lead_time_filtered_2_3.shape[0]
# Sum the number of shifts called off between 3-4 hours prior
three_four = lead_time_filtered_3_4.shape[0]
# Sum the number of shifts called off between 4-24 hours prior
four_twelve = lead_time_filtered_4_12.shape[0]
# Sum the number of shifts called off between 4-24 hours prior
twelve_twentyfour = lead_time_filtered_12_24.shape[0]
# Sum the number of shifts called off greater than 24 hours prior
twentyfour_plus = lead_time_filtered_24.shape[0]

# BOOKING DATA CALCULATIONS
# Select the total nunmber of shifts in cleveland_booking_logs.csv
booking_count = booking.shape[0]

# Select the rows where 'Action' = 'WORKER_CALL_OFF' and 'Lead Time' is after the shift start time
claim_lead_filtered_0_0 = booking[(booking['Action'] == 'SHIFT_CLAIM') & (booking['Lead Time'] <= 0)]
# Select the rows where 'Action' = 'WORKER_CALL_OFF' and 'Lead Time' is between 0 and 1 hours
claim_lead_filtered_0_1 = booking[(booking['Action'] == 'SHIFT_CLAIM') & (booking['Lead Time'] >= 0) & (booking['Lead Time'] <= 1)]
# Select the rows where 'Action' = 'WORKER_CALL_OFF' and 'Lead Time' is between 1 and 2 hours
claim_lead_filtered_1_2 = booking[(booking['Action'] == 'SHIFT_CLAIM') & (booking['Lead Time'] >= 1) & (booking['Lead Time'] <= 2)]
# Select the rows where 'Action' = 'WORKER_CALL_OFF' and 'Lead Time' is between 2 and 3 hours
claim_lead_filtered_2_3 = booking[(booking['Action'] == 'SHIFT_CLAIM') & (booking['Lead Time'] >= 2) & (booking['Lead Time'] <= 3)]
# Select the rows where 'Action' = 'WORKER_CALL_OFF' and 'Lead Time' is between 3 and 4 hours
claim_lead_filtered_3_4 = booking[(booking['Action'] == 'SHIFT_CLAIM') & (booking['Lead Time'] >= 3) & (booking['Lead Time'] <= 4)]
# Select the rows where 'Action' = 'WORKER_CALL_OFF' and 'Lead Time' is between 4 and 24 hours
claim_lead_filtered_4_12 = booking[(booking['Action'] == 'SHIFT_CLAIM') & (booking['Lead Time'] >= 4) & (booking['Lead Time'] <= 12)]
# Select the rows where 'Action' = 'WORKER_CALL_OFF' and 'Lead Time' is between 4 and 24 hours
claim_lead_filtered_12_24 = booking[(booking['Action'] == 'SHIFT_CLAIM') & (booking['Lead Time'] >= 12) & (booking['Lead Time'] <= 24)]
# Select the rows where 'Action' = 'WORKER_CALL_OFF' and 'Lead Time' is greater than 24 hours
claim_lead_filtered_24 = booking[(booking['Action'] == 'SHIFT_CLAIM') & (booking['Lead Time'] >= 24)]

# Sum the number of shifts claimed after shift start time
claim_post_start = claim_lead_filtered_0_0.shape[0]
# Sum the number of shifts claimed between 0-1 hours prior
claim_zero_one = claim_lead_filtered_0_1.shape[0]
# Sum the number of shifts claimed between 1-2 hours prior
claim_one_two = claim_lead_filtered_1_2.shape[0]
# Sum the number of shifts claimed between 2-3 hours prior
claim_two_three = claim_lead_filtered_2_3.shape[0]
# Sum the number of shifts claimed between 3-4 hours prior
claim_three_four = claim_lead_filtered_3_4.shape[0]
# Sum the number of shifts claimed between 4-24 hours prior
claim_four_twelve = claim_lead_filtered_4_12.shape[0]
# Sum the number of shifts claimed between 4-24 hours prior
claim_twelve_twentyfour = claim_lead_filtered_12_24.shape[0]
# Sum the number of shifts claimed greater than 24 hours prior
claim_twentyfour_plus = claim_lead_filtered_24.shape[0]

# Print shift calculation results
print("SHIFTS DATA")
print("Total Shifts:", total_shifts)
print("HCF Deleted Shifts:", deleted_shifts)
print("Percentage of HCF deleted shifts:", round((deleted_shifts / total_shifts) * 100, 2),"%")
print("Non-deleted Shifts:", non_deleted_count)
print("Fulfilled Shifts:", fulfilled_shifts)
print("Percentage of fulfilled shifts:", round((fulfilled_shifts / non_deleted_count) * 100, 2),"%")
print("Unfulfilled Shifts:", unfulfilled_shifts)
print("Percentage of unfulfilled shifts:", round((unfulfilled_shifts / non_deleted_count) * 100, 2),"%")

# Print cancellation calculation results
print("CANCEL LOGS DATA")
print("Total number of called off shifts:", total_called_off_shifts)
print("Total percentage of NCNS shifts:", round((total_ncns / total_called_off_shifts) * 100, 2),"%")
print("Total percentage of shifts called off by HCPs:", round((total_call_off / total_called_off_shifts) * 100, 2),"%")
print("Percentage of shifts called off where 'Lead Time' is between 0 and 1 hour:", round((zero_one / total_called_off_shifts) * 100, 2),"%")
print("Percentage of shifts called off where 'Lead Time' is between 1 and 2 hours:", round((one_two / total_called_off_shifts) * 100, 2),"%")
print("Percentage of shifts called off where 'Lead Time' is between 2 and 3 hours:", round((two_three / total_called_off_shifts) * 100, 2),"%")
print("Percentage of shifts called off where 'Lead Time' is between 3 and 4 hours:", round((three_four / total_called_off_shifts) * 100, 2),"%")
print("Percentage of shifts called off where 'Lead Time' is between 4 and 12 hours:", round((four_twelve / total_called_off_shifts) * 100, 2),"%")
print("Percentage of shifts called off where 'Lead Time' is between 12 and 24 hours:", round((twelve_twentyfour / total_called_off_shifts) * 100, 2),"%")
print("Percentage of shifts called off where 'Lead Time' is greater than 24 hours:", round((twentyfour_plus / total_called_off_shifts) * 100, 2),"%")

# Print booking calculation results
print("BOOKING LOGS DATA")
print("Number of shifts booked:", booking_count)
print("Percentage of shifts claimed after the shift start time:", round((claim_post_start / booking_count) * 100, 2),"%")
print("Percentage of shifts claimed where 'Lead Time' is between 0 and 1 hour:", round((claim_zero_one / booking_count) * 100, 2),"%")
print("Percentage of shifts claimed where 'Lead Time' is between 1 and 2 hours:", round((claim_one_two / booking_count) * 100, 2),"%")
print("Percentage of shifts claimed where 'Lead Time' is between 2 and 3 hours:", round((claim_two_three / booking_count) * 100, 2),"%")
print("Percentage of shifts claimed where 'Lead Time' is between 3 and 4 hours:", round((claim_three_four / booking_count) * 100, 2),"%")
print("Percentage of shifts claimed where 'Lead Time' is between 4 and 12 hours:", round((claim_four_twelve / booking_count) * 100, 2),"%")
print("Percentage of shifts claimed where 'Lead Time' is between 12 and 24 hours:", round((claim_twelve_twentyfour / booking_count) * 100, 2),"%")
print("Percentage of shifts claimed where 'Lead Time' is greater than 24 hours:", round((claim_twentyfour_plus / booking_count) * 100, 2),"%")