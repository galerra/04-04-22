#!/usr/bin/env python3
main_list = []
with open("17.txt") as f_o:
    for i in f_o:
        main_list.append(int(i.split()[0]))
double_count = 0
min_sum = 0
for i in range(len(main_list) - 2):
    sort_l = sorted([main_list[i], main_list[i + 1], main_list[i + 2]])
    if sort_l[2]**2 < (sort_l[1]**2 + sort_l[0]**2):
        double_count += 1
        m = max(m, sum(sort_l))
print(double_count, min_sum)