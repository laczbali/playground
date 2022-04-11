# Task
# - we have a safe, that has an N digit code
# - we know a number of rules about the code
# - we need to figure it out based on those rules

# how many digits in the "code"
    # DIGIT_COUNT = 3
DIGIT_COUNT = 4
# hinted combination, correct digits, correct placement
    # RULES = [
    #     ([6,8,2], 1, 1),
    #     ([6,1,4], 1, 0),
    #     ([2,0,6], 2, 0),
    #     ([7,3,8], 0, 0),
    #     ([7,8,0], 1, 0),
    # ]
RULES = [
    ([0, 5, 8, 2], 1, 1),
    ([5, 4, 7, 9], 2, 2),
    ([1, 5, 9, 6], 1, 1),
    ([3, 0, 6, 1], 2, 0),
    ([2, 7, 0, 3], 2, 0),
]

# -----------
LOWER_LIMIT = 0
UPPER_LIMIT = (10**DIGIT_COUNT)

possibilities = []
for num in range(LOWER_LIMIT, UPPER_LIMIT):
    numarray = [int(d) for d in str(num)]
    # left-pad with zeros
    numarray = [0] * (DIGIT_COUNT - len(numarray)) + numarray

    num_passed_flag = True

    for rule in RULES:
        # check that correctly placed digits are present
        same_digit_count = len([idx for idx in range(0, DIGIT_COUNT) if numarray[idx] == rule[0][idx]])
        if same_digit_count != rule[2]:
            num_passed_flag = False
            break

        # check that correct digits, with incorrect placement, are present
        similar_digit_count = len([digit for digit in numarray if digit in rule[0]])
        if similar_digit_count != rule[1]:
            num_passed_flag = False
            break

    if num_passed_flag:
        # num to string, with left-padding
        num_str = str(num).zfill(DIGIT_COUNT)
        possibilities.append(num_str)

print(possibilities)