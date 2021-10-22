# Original purpose of this program:
# To find all the pairs of numbers within 99 which could fulfill AB / BC = A/C.

# Main process:
num_ful_1 = 0
for A in range(1, 10):
    for B in range(1, 10):
        AB = A * 10 + B
        for C in range(1, 10):
            BC = B * 10 + C
            if AB == BC:
                continue
            else:
                if AB / BC == A / C:
                    print(AB, '/', BC, '=', A, '/', C)
                    num_ful_1 += 1
print('There are', num_ful_1, 'pairs in total.')

# Findings:
# 1. Reminds me that range() has a closed-open neighborhood.
# 2. If we build up a list with range(), the initials are not necessary.

# Try LMNO and NOPQ patterns:
num_ful_2 = 0
for LM in range(10, 100):
    for NO in range(10, 100):
        LMNO = LM * 100 + NO
        for PQ in range(10, 100):
            NOPQ = NO * 100 + PQ
            if LMNO == NOPQ:
                continue
            else:
                if LMNO / NOPQ == LM / PQ:
                    print(LMNO, '/', NOPQ, '=', LM, '/', PQ)
                    num_ful_2 += 1
print('There are', num_ful_2, 'pairs in total.')

# Findings:
# 1. NO = 66 or 99 ?
# 2. Maybe there is an easier algorithm?

# Version 2.0:
num_ful_3 = 0
for numerator_1 in range(10, 100):
    for denominator_1 in range(10, 100):
        if numerator_1 == denominator_1:
            continue
        else:
            if (denominator_1 % 10) / int(numerator_1 / 10) == denominator_1 / numerator_1:
                if numerator_1 % 10 == int(denominator_1 / 10):
                    print(numerator_1, '/', denominator_1, '=', int(numerator_1 / 10), '/', denominator_1 % 10)
                    num_ful_3 += 1
print('There are', num_ful_3, 'pairs in total.')

num_ful_4 = 0
for numerator_2 in range(1000, 10000):
    for denominator_2 in range(1000, 10000):
        if numerator_2 == denominator_2:
            continue
        else:
            if (denominator_2 % 100) / int(numerator_2 / 100) == denominator_2 / numerator_2:
                if numerator_2 % 100 == int(denominator_2 / 100):
                    print(numerator_2, '/', denominator_2, '=', int(numerator_2 / 100), '/', denominator_2 % 100)
                    num_ful_4 += 1
print('There are', num_ful_4, 'pairs in total.')

# Findings:
# 1. Why does the later algorithm contain less statements but turn out to cost more time?
