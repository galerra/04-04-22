#!/usr/bin/env python3
main_list = []
s = []
with open("17.txt") as f_o:
    for i in f_o:
        main_list.append(int(i.split()[0]))
double_count = 0
for i in range(1, len(main_list), 1):
    if i == 1:
        min_sum = main_list[i] + main_list[i - 1]
    if (main_list[i] % 3 == 0 or main_list[i - 1] % 3 == 0):
        double_count += 1
        if main_list[i] + main_list[i - 1] > min_sum:
            min_sum = main_list[i] + main_list[i - 1]
print(double_count, min_sum)