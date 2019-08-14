#!/usr/local/bin/python3
at = [0, 1, 2, 3, 4]
bt = [10, 1, 2, 1, 5]
priority = [7, 10, 5, 5, 9]
ct, tat, wt = [], [], []

n = len(priority)

# Sorting the jobs according to the priority
for i in range(n):
        for j in range(1, n-i-1):
            if priority[j] > priority[j+1] :
                priority[j], priority[j+1] = priority[j+1], priority[j]
                bt[j], bt[j+1] = bt[j+1], bt[j]
                at[j], at[j+1] = at[j+1], at[j]

# Calculating Completion Time, CT
ct.insert(0, bt[0])
tat.append(ct[0] - at[0])
wt.append(tat[0] - bt[0])
for i in range(1, n):
    ct.append(ct[i-1] + bt[i])
    tat.append(ct[i] - at[i])
    wt.append(tat[i] - bt[i])
# Sorting the jobs according to the arrival time, AT
for i in range(n):
        for j in range(1, n-i-1):
            if at[j] > at[j+1] :
                priority[j], priority[j+1] = priority[j+1], priority[j]
                bt[j], bt[j+1] = bt[j+1], bt[j]
                at[j], at[j+1] = at[j+1], at[j]
                tat[j], tat[j+1] = tat[j+1], tat[j]
                wt[j], wt[j+1] = wt[j+1], wt[j]
print(tat)