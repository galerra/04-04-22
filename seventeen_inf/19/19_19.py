#!/usr/bin/env python3
main_list = []
with open("17.txt") as f_o:
    for i in f_o:
        main_list.append(int(i.split()[0]))
double_count = 0
min_sum = 0
for i in range(len(main_list) - 1):
    for j in range(i + 1,len(main_list)):
        if (main_list[i] + main_list[j]) % 80 == 0 and (main_list[i] % 50 == 0 or main_list[j] % 50 == 0):
            double_count += 1
            min_sum = max(min_sum,main_list[i] + main_list[j])
print(double_count, min_sum)