# Initial
Total = 0
Count = 0
Average = 0
Max_num = -99999999
Min_num = +99999999

# Main structure
while True:
    current_num = input('Enter a number: ')

    if current_num == 'done':
        print('You entered ', Count, ' numbers, the total is: ', Total, ', the average is: ', Average)
        print('The maximum is: ', Max_num, ', the minimum is: ', Min_num)
        break
    else:
        try:
            Total = Total + float(current_num)
            Count = Count + 1
            Average = Total / Count
            Max_num = max(Max_num, float(current_num))
            Min_num = min(Min_num, float(current_num))
        except ValueError as invalid:
            print('Error type: ', invalid)

