from datetime import datetime

# Example dates
date1 = datetime(2026, 2, 23, 12, 0, 0) # Feb 23, 2026, 12:00 PM
date2 = datetime(2026, 2, 24, 14, 30, 0) # Feb 24, 2026, 02:30 PM

# Calculate difference
difference = date2 - date1
seconds_diff = difference.total_seconds()

print(f"The difference is {seconds_diff} seconds.")