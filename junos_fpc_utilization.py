import os
import paramiko
import re
import sys
import time
from pprint import pprint
import argparse
from ssh_connectivity import Device
from junos_sys_chassis import get_chassis_fpc
from junos_sys_chassis import parse_chassis_fpc_output
from junos_sys_chassis import sweep_status
from backend_functions import determine_list_average
from backend_functions import determine_list_highest_value



'''The following code can be used to execute this script file on 1 device under test.'''
cli_args = sys.argv[1:]
dut_ip = cli_args[0]
dut_user = cli_args[1]
dut_pass = cli_args[2]
route_table = cli_args[3]


'''DUT Login parameters'''
host_ip = dut_ip
user = dut_user
passwd = dut_pass
timeout = 30


def main():
    dut_host = Device(host_ip, user, passwd)
    try:
        # obtain list of FPCs currently online and parse associated values
        fpc_values = get_chassis_fpc(dut_host)
        fpc_func_output = parse_chassis_fpc_output(fpc_values)
        fpc_count = len(fpc_func_output)
        print(f"There are {fpc_count} FPC(s) online in {host_ip}")
        fpc_slots = []
        fpc_states = []
        fpc_cpu_util = []
        fpc_mem_util = []
        fpc_mem_heap = []
        fpc_mem_buffer = []
        for fpc in fpc_func_output:
            fpc_dict = fpc
            # append dict key values to pre-defined lists
            fpc_slots.append(fpc_dict['fpc_slot'])
            fpc_states.append(fpc_dict['fpc_status'])
            fpc_cpu_util.append(fpc_dict['fpc_cpu_util_pct'])
            fpc_mem_util.append(fpc_dict['fpc_cpu_mem_dram_mb'])
            fpc_mem_heap.append(fpc_dict['fpc_cpu_mem_util_heap'])
            fpc_mem_buffer.append(fpc_dict['fpc_cpu_mem_util_buf'])
            print(f"FPC {fpc_slots[0]} state is {fpc_states[0]}. Current CPU utilization is {fpc_cpu_util[0]}. Current memory utilization is {fpc_mem_util[0]}MB, buffer use % is {fpc_mem_buffer[0]}, and heap use % is {fpc_mem_heap[0]}.")
    except:
        print(f'An error occurred.')
    try:
        fpc_values = get_chassis_fpc(dut_host)
        fpc_online_list = sweep_status(fpc_values)
        fpc_count = len(fpc_online_list)
        # Get FPC utilization over a specified interval period
        interval_current = 0
        interval_end = 20
        fpc_cpu_util = []
        fpc_mem_util = []
        fpc_mem_heap = []
        fpc_mem_buffer = []
        while interval_current <= interval_end:
            print(f"Interval {interval_current}")
            for fpc in range(fpc_count):
                fpc_values = get_chassis_fpc(dut_host)
                fpc_func_output = parse_chassis_fpc_output(fpc_values)
                fpc_count = len(fpc_func_output)
                #print(f"There are {fpc_count} FPC(s) online in {host_ip}")
                for fpc in fpc_func_output:
                    fpc_dict = fpc
                    # append dict key values to pre-defined lists
                    slot = fpc_dict['fpc_slot']
                    cpu_util_pct = fpc_dict['fpc_cpu_util_pct']
                    cpu_total_mem = fpc_dict['fpc_cpu_mem_dram_mb']
                    cpu_mem_util_heap = fpc_dict['fpc_cpu_mem_util_heap']
                    cpu_mem_util_buf = fpc_dict['fpc_cpu_mem_util_buf']
                    # display current values from device
                    print(f'FPC {slot} CPU Utilization: {cpu_util_pct}%')
                    print(f'FPC {slot} CPU Utilization - Total Memory: {cpu_total_mem}MB')
                    print(f'FPC {slot} CPU Utilization - Memory Heap: {cpu_mem_util_heap}%')
                    print(f'FPC {slot} CPU Utilization - Memory Buffer: {cpu_mem_util_buf}%')
                    # append values to lists to get averages later
                    fpc_cpu_util.append(int(cpu_util_pct))
                    fpc_mem_util.append(int(cpu_total_mem))
                    fpc_mem_heap.append(int(cpu_mem_util_heap))
                    fpc_mem_buffer.append(int(cpu_mem_util_buf))
                    # fpc_cpu_util.append(fpc_dict['fpc_cpu_util_pct'])
                    # fpc_mem_util.append(fpc_dict['fpc_cpu_mem_dram_mb'])
                    # fpc_mem_heap.append(fpc_dict['fpc_cpu_mem_util_heap'])
                    # fpc_mem_buffer.append(fpc_dict['fpc_cpu_mem_util_buf'])
                    # print(fpc_cpu_util)
                    # print(fpc_mem_util)
                    # print(fpc_mem_heap)
                    # print(fpc_mem_buffer)
            interval_current += 1
        print(f'########################################################')
        print(f'######################## SUMMARY #######################')
        print(f'########################################################')
        fpc_cpu_util_avg = round(determine_list_average(fpc_cpu_util), 2)
        fpc_mem_util_avg = int(determine_list_average(fpc_mem_util))
        fpc_mem_heap_avg = round(determine_list_average(fpc_mem_heap), 2)
        fpc_mem_buffer_avg = round(determine_list_average(fpc_mem_buffer), 2)
        fpc_cpu_util_max = round(determine_list_highest_value(fpc_cpu_util), 2)
        print(f'FPC CPU utilizations after {interval_end}x 1 second iterations:')
        print(f'########################################################')
        print(f'FPC {slot} CPU Utilization (Maximum): {fpc_cpu_util_max}%')
        print(f'FPC {slot} CPU Utilization (Average): {fpc_cpu_util_avg}%')
        print(f'FPC {slot} CPU Utilization - Total Memory (Average): {fpc_mem_util_avg}MB')
        print(f'FPC {slot} CPU Utilization - Memory Heap (Average): {fpc_mem_heap_avg}%')
        print(f'FPC {slot} CPU Utilization - Memory Buffer (Average): {fpc_mem_buffer_avg}%')
        print(f'########################################################')
        print(f'########################################################')
        print(f'########################################################')
    except:
        print(f'An error occurred.')




if __name__ == '__main__':
    main()
