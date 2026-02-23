import datetime


dt = datetime.datetime.now()


dt_no_micro = dt.replace(microsecond=0)

print("With Microseconds:   ", dt)
print("Without Microseconds:", dt_no_micro)