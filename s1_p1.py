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
