def FCFS(arrival_time, burst_time):
    n = len(arrival_time)
    completion_time = [0] * n
    waiting_time = [0] * n
    turnaround_time = [0] * n

    # Completion time for first process is its burst time
    completion_time[0] = burst_time[0]

    # Calculate completion time for each process
    for i in range(1, n):
        completion_time[i] = completion_time[i - 1] + burst_time[i]

    # Calculate turnaround time and waiting time for each process
    for i in range(n):
        turnaround_time[i] = completion_time[i] - arrival_time[i]
        waiting_time[i] = turnaround_time[i] - burst_time[i]

    return completion_time, turnaround_time, waiting_time

# Example usage:
arrival_time = [0, 1, 2, 3]
burst_time = [5, 3, 8, 6]
completion_time, turnaround_time, waiting_time = FCFS(arrival_time, burst_time)

print("Process\t Arrival Time\t Burst Time\t Completion Time\t Turnaround Time\t Waiting Time")
for i in range(len(arrival_time)):
    print(f"P{i+1}\t\t {arrival_time[i]}\t\t {burst_time[i]}\t\t {completion_time[i]}\t\t\t {turnaround_time[i]}\t\t\t {waiting_time[i]}")

