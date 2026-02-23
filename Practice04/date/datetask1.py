from datetime import date, timedelta

current_date = date.today()
five_days_ago = current_date - timedelta(days=5)

print("Current Date:", current_date)
print("Five days ago:", five_days_ago)