import pandas as pd

# Read the three csv files provided
booking = pd.read_csv('cleveland_booking_logs.csv')
cancel = pd.read_csv('cleveland_cancel_logs.csv')
shifts = pd.read_csv('cleveland_shifts.csv')

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

# Print the results
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