# Introduction:
# This program is a salary calculator.
# It automatically calculate one's salary via inputting working hours and pay rate.
# Basic rules:
# Within 40 hours, one gets his pay at a standard rate.
# For overtime beyond 40 hours, there would be a 50% overtime pay.

# Initial
Pay = None
Overtime = None

# Main structure
while True:
    work_hrs = input('Input work hours: ')
    pay_rate = input('Input pay rate: ')

    try:
        Overtime = max(float(work_hrs) - 40, 0)
        Pay = float(work_hrs) * float(pay_rate) + Overtime * float(pay_rate) * 0.5
    except:
        Pay = -1

    if Pay == -1:
        print('Invalid, pls enter numeric input')
    else:
        break
print('Total pay is: ', Pay)
