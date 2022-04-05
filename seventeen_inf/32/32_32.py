#!/usr/bin/env python3
main_list = []
with open("17.txt") as f_o:
    for i in f_o:
        main_list.append(int(i.split()[0]))
double_count = 0
max_sum = 0
s = 0
n = 0
for i in range(len(main_list)):
    if (main_list[i] % 2 == 1):
        s += main_list[i]
        n += 1
x = s / n
for i in range(len(main_list) - 1):
    if ((main_list[i] % 5 == 0) or (main_list[i + 1] % 5 == 0)) and ((main_list[i] < x) or (main_list[i + 1] < x)):
        double_count += 1
        max_sum = max(max_sum, main_list[i] + main_list[i + 1])
print(double_count, max_sum)