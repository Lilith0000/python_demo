# Introduction:
# Inputting series of numbers, this program automatically help to count and record things.
# If input 'done', the program will stop and show results as bellows:
# 1. total; 2. average; 3. count of numbers; 4. maximum number; 5. minimum number.

# Initial
total = 0
count = 0
average = None
max_num = None
min_num = None

# Main structure
while True:
    current_num = input('Enter a number: ')
    if current_num == 'done':
        print('You entered ', count, ' numbers, the total is: ', total, ', the average is: ', average)
        print('The maximum is: ', max_num, ', the minimum is: ', min_num)
        break
    else:
        try:
            current_num = float(current_num)
        except ValueError as invalid:
            print('Error type: ', invalid)
            continue
        if max_num is None:
            max_num = current_num
        else:
            max_num = max(max_num, current_num)
        if min_num is None:
            min_num = current_num
        else:
            min_num = min(min_num, current_num)
        total += current_num
        count += 1
        average = total / count




