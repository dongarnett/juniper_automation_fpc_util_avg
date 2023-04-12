# juniper_automation_fpc_util_avg
This tool obtains a list of FPCs currently online and returns the following over a user supplied interval period:

-CPU Utilization
1. Maximum CPU Utilization %
2. Average CPU Utilization %
3. Average Total Memory (in MB)
4. Average Memory Heap %
5. Average Memory Buffer %



Usage:
you@your_computer# python3 junos_fpc_utilization.py <ip-address> <username> <password> <interval-count>


Example Run:
me@my_computer# python3 junos_fpc_utilization.py 10.0.0.21 user123 passwd123 20
Sending command: show chassis fpc

There are 1 FPC(s) online in 10.0.0.21
FPC 0 state is Online. Current CPU utilization is 26. Current memory utilization is 511MB, buffer use % is 0, and heap use % is 32.
Sending command: show chassis fpc

Interval 0
Sending command: show chassis fpc

FPC 0 CPU Utilization: 26%
FPC 0 CPU Utilization - Total Memory: 511MB
FPC 0 CPU Utilization - Memory Heap: 32%
FPC 0 CPU Utilization - Memory Buffer: 0%
Interval 1
Sending command: show chassis fpc

FPC 0 CPU Utilization: 26%
FPC 0 CPU Utilization - Total Memory: 511MB
FPC 0 CPU Utilization - Memory Heap: 32%
FPC 0 CPU Utilization - Memory Buffer: 0%
Interval 2
Sending command: show chassis fpc

FPC 0 CPU Utilization: 26%
FPC 0 CPU Utilization - Total Memory: 511MB
FPC 0 CPU Utilization - Memory Heap: 32%
FPC 0 CPU Utilization - Memory Buffer: 0%
Interval 3
Sending command: show chassis fpc

FPC 0 CPU Utilization: 27%
FPC 0 CPU Utilization - Total Memory: 511MB
FPC 0 CPU Utilization - Memory Heap: 32%
FPC 0 CPU Utilization - Memory Buffer: 0%
Interval 4
Sending command: show chassis fpc

FPC 0 CPU Utilization: 27%
FPC 0 CPU Utilization - Total Memory: 511MB
FPC 0 CPU Utilization - Memory Heap: 32%
FPC 0 CPU Utilization - Memory Buffer: 0%
Interval 5
Sending command: show chassis fpc

FPC 0 CPU Utilization: 27%
FPC 0 CPU Utilization - Total Memory: 511MB
FPC 0 CPU Utilization - Memory Heap: 32%
FPC 0 CPU Utilization - Memory Buffer: 0%
Interval 6
Sending command: show chassis fpc

FPC 0 CPU Utilization: 27%
FPC 0 CPU Utilization - Total Memory: 511MB
FPC 0 CPU Utilization - Memory Heap: 32%
FPC 0 CPU Utilization - Memory Buffer: 0%
Interval 7
Sending command: show chassis fpc

FPC 0 CPU Utilization: 27%
FPC 0 CPU Utilization - Total Memory: 511MB
FPC 0 CPU Utilization - Memory Heap: 32%
FPC 0 CPU Utilization - Memory Buffer: 0%
Interval 8
Sending command: show chassis fpc

FPC 0 CPU Utilization: 27%
FPC 0 CPU Utilization - Total Memory: 511MB
FPC 0 CPU Utilization - Memory Heap: 32%
FPC 0 CPU Utilization - Memory Buffer: 0%
Interval 9
Sending command: show chassis fpc

FPC 0 CPU Utilization: 33%
FPC 0 CPU Utilization - Total Memory: 511MB
FPC 0 CPU Utilization - Memory Heap: 32%
FPC 0 CPU Utilization - Memory Buffer: 0%
Interval 10
Sending command: show chassis fpc

FPC 0 CPU Utilization: 33%
FPC 0 CPU Utilization - Total Memory: 511MB
FPC 0 CPU Utilization - Memory Heap: 32%
FPC 0 CPU Utilization - Memory Buffer: 0%
Interval 11
Sending command: show chassis fpc

FPC 0 CPU Utilization: 33%
FPC 0 CPU Utilization - Total Memory: 511MB
FPC 0 CPU Utilization - Memory Heap: 32%
FPC 0 CPU Utilization - Memory Buffer: 0%
Interval 12
Sending command: show chassis fpc

FPC 0 CPU Utilization: 33%
FPC 0 CPU Utilization - Total Memory: 511MB
FPC 0 CPU Utilization - Memory Heap: 32%
FPC 0 CPU Utilization - Memory Buffer: 0%
Interval 13
Sending command: show chassis fpc

FPC 0 CPU Utilization: 33%
FPC 0 CPU Utilization - Total Memory: 511MB
FPC 0 CPU Utilization - Memory Heap: 32%
FPC 0 CPU Utilization - Memory Buffer: 0%
Interval 14
Sending command: show chassis fpc

FPC 0 CPU Utilization: 33%
FPC 0 CPU Utilization - Total Memory: 511MB
FPC 0 CPU Utilization - Memory Heap: 32%
FPC 0 CPU Utilization - Memory Buffer: 0%
Interval 15
Sending command: show chassis fpc

FPC 0 CPU Utilization: 31%
FPC 0 CPU Utilization - Total Memory: 511MB
FPC 0 CPU Utilization - Memory Heap: 32%
FPC 0 CPU Utilization - Memory Buffer: 0%
Interval 16
Sending command: show chassis fpc

FPC 0 CPU Utilization: 31%
FPC 0 CPU Utilization - Total Memory: 511MB
FPC 0 CPU Utilization - Memory Heap: 32%
FPC 0 CPU Utilization - Memory Buffer: 0%
Interval 17
Sending command: show chassis fpc

FPC 0 CPU Utilization: 31%
FPC 0 CPU Utilization - Total Memory: 511MB
FPC 0 CPU Utilization - Memory Heap: 32%
FPC 0 CPU Utilization - Memory Buffer: 0%
Interval 18
Sending command: show chassis fpc

FPC 0 CPU Utilization: 31%
FPC 0 CPU Utilization - Total Memory: 511MB
FPC 0 CPU Utilization - Memory Heap: 32%
FPC 0 CPU Utilization - Memory Buffer: 0%
Interval 19
Sending command: show chassis fpc

FPC 0 CPU Utilization: 31%
FPC 0 CPU Utilization - Total Memory: 511MB
FPC 0 CPU Utilization - Memory Heap: 32%
FPC 0 CPU Utilization - Memory Buffer: 0%
Interval 20
Sending command: show chassis fpc

FPC 0 CPU Utilization: 31%
FPC 0 CPU Utilization - Total Memory: 511MB
FPC 0 CPU Utilization - Memory Heap: 32%
FPC 0 CPU Utilization - Memory Buffer: 0%
########################################################
######################## SUMMARY #######################
########################################################
FPC CPU utilizations after 20x 1 second iterations:
########################################################
FPC 0 CPU Utilization (Maximum): 33%
FPC 0 CPU Utilization (Average): 29.71%
FPC 0 CPU Utilization - Total Memory (Average): 511MB
FPC 0 CPU Utilization - Memory Heap (Average): 32.0%
FPC 0 CPU Utilization - Memory Buffer (Average): 0.0%
########################################################
########################################################
########################################################
![image](https://user-images.githubusercontent.com/103336677/231333916-23dd98d6-e421-4a24-a947-3564a3796f49.png)
