one_list = [0, 100000, [], 0]
two_list = [0, 100000, [], 0]
four_list = [0, 100000, [], 0]


def not_blank(question, error_message, let_ok):
    valid = False
    error = error_message
    while not valid:
        letter = False
        response = input(question)
        if not let_ok:
            for letter in response:
                if letter.isalpha():
                    letter = True

        if not response or letter is True:  # Generate Error for bad name
            print(error)

        else:  # no error found
            return response


def input_times(list):
    time = 0
    while time != -1:

        time = not_blank("Please enter your time\n"
                         "If you are finished then please enter '-1': ", "Sorry please enter an integer", False)
        time = int(time)
        if time != -1:
            list[2].append(time)
    for time in list[2]:
        list[3] = list[3] + time
        if time < list[1]:
            list[1] = time
    list[0] = list[3] / len(list[2])
    list = [list[0], list[1], list[2], list[3]]
    return list


mode = int(input("Please enter what race type you would like to enter results in\n"
                 "Please enter '1','2' or '3' for 100m, 200m or 400m: "))
while mode != 1 and mode != 2 and mode != 3:
    mode = int(input("Sorry Please enter '1' '2' or '3': "))

if mode == 1:
    one_list = input_times(one_list)
if mode == 2:
    two_list = input_times(two_list)
if mode == 3:
    four_list = input_times(four_list)
mode = 0
while mode != 14:
    mode = int(input("Press '1' '2' or '3' to enter more race times\n"
                     "Press '4' '5' or '6' to see all results for the 100m, 200m or 400m respectively\n"
                     "Press '7' '8' or '9' to see the average times for the 100m 200m or 400m respectively\n"
                     "Press '10 '11' or '12' to see the best times for the 100m 200m or 400m respectively\n"
                     "Press '13' to wipe all results and '14' to end the program: "))
    while 1 > mode or mode > 14:
        mode = int(input("Sorry I didn't register that: "))
    if mode == 1:
        one_list = input_times(one_list)
    if mode == 2:
        two_list = input_times(two_list)
    if mode == 3:
        four_list = input_times(four_list)
    if mode == 4:
        print("The times for the 100m are {}".format(one_list[2]))
    if mode == 5:
        print("The times for the 200m are {}".format(two_list[2]))
    if mode == 6:
        print("The times for the 400m are {}".format(four_list[2]))
    if mode == 7:
        print("The average time for 100m is {}".format(one_list[0]))
    if mode == 8:
        print("The average time for 200m is {}".format(two_list[0]))
    if mode == 9:
        print("The average time for 400m is {}".format(four_list[0]))
    if mode == 10:
        print("The best time for 100m is {}".format(one_list[1]))
    if mode == 11:
        print("The best time for 200m is {}".format(two_list[1]))
    if mode == 12:
        print("The best time for 400m is {}".format(four_list[1]))
    if mode == 13:
        one_list = [0, 100000, [], 0]
        two_list = [0, 100000, [], 0]
        four_list = [0, 100000, [], 0]
