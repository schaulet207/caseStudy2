import pandas as pd

# Read the three csv files provided
booking = pd.read_csv('cleveland_booking_logs.csv')
cancel = pd.read_csv('cleveland_cancel_logs.csv')
shifts = pd.read_csv('cleveland_shifts.csv')

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

# Print the results
print("Percentage of shifts claimed after the shift start time:", round((claim_post_start / booking_count) * 100, 2),"%")
print("Percentage of shifts claimed where 'Lead Time' is between 0 and 1 hour:", round((claim_zero_one / booking_count) * 100, 2),"%")
print("Percentage of shifts claimed where 'Lead Time' is between 1 and 2 hours:", round((claim_one_two / booking_count) * 100, 2),"%")
print("Percentage of shifts claimed where 'Lead Time' is between 2 and 3 hours:", round((claim_two_three / booking_count) * 100, 2),"%")
print("Percentage of shifts claimed where 'Lead Time' is between 3 and 4 hours:", round((claim_three_four / booking_count) * 100, 2),"%")
print("Percentage of shifts claimed where 'Lead Time' is between 4 and 12 hours:", round((claim_four_twelve / booking_count) * 100, 2),"%")
print("Percentage of shifts claimed where 'Lead Time' is between 12 and 24 hours:", round((claim_twelve_twentyfour / booking_count) * 100, 2),"%")
print("Percentage of shifts claimed where 'Lead Time' is greater than 24 hours:", round((claim_twentyfour_plus / booking_count) * 100, 2),"%")
