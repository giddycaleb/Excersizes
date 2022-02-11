times = []
time = 0
best_time = 100000000
total_time = 0
while time != -1:

    time = float(input("Please enter your time\n"
                       "If you are finished then please enter '-1': "))
    if time != -1:
        times.append(time)
for time in times:
    total_time = total_time + time
    print(time)
    if time < best_time:
        best_time = time
print("The best time was {}".format(best_time))
print("The average time was {}".format(total_time/len(times)))
