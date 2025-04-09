import sys

# Initialize lists for 5 processes
n = 5
at = []
bt = []
pt = []
st = [-1] * n
et = [0] * n
wt = [0] * n
tt = [0] * n
done = [False] * n

# Input for 5 processes
print("Enter details for 5 processes:\n")
for i in range(n):
    print(f"Process {i + 1}:")
    at.append(int(input("Arrival Time: ")))
    bt.append(int(input("Burst Time: ")))
    pt.append(int(input("Priority (Lower = Higher Priority): ")))

original_bt = bt[:]

jtime = 0
counter = n

# Preemptive Priority Scheduling Logic
while counter > 0:
    index = -1
    highest_priority = sys.maxsize

    for i in range(n):
        if at[i] <= jtime and not done[i] and bt[i] > 0:
            if pt[i] < highest_priority:
                highest_priority = pt[i]
                index = i
            elif pt[i] == highest_priority:
                if at[i] < at[index]:  # FCFS tie breaker
                    index = i

    if index != -1:
        if st[index] == -1:
            st[index] = jtime
        bt[index] -= 1
        jtime += 1

        if bt[index] == 0:
            et[index] = jtime
            done[index] = True
            counter -= 1
    else:
        jtime += 1

# Calculate WT and TT
total_wt = 0
total_tt = 0
for i in range(n):
    tt[i] = et[i] - at[i]
    wt[i] = tt[i] - original_bt[i]
    total_wt += wt[i]
    total_tt += tt[i]

# Print result table
print("\nFinal Scheduling Table:")
print("P\tAT\tBT\tST\tET\tWT\tTT")
for i in range(n):
    print(f"P{i+1}\t{at[i]}\t{original_bt[i]}\t{st[i]}\t{et[i]}\t{wt[i]}\t{tt[i]}")

# Print averages
avg_wt = total_wt / n
avg_tt = total_tt / n

print(f"\nAverage Waiting Time: {avg_wt:.2f}")
print(f"Average Turnaround Time: {avg_tt:.2f}")
