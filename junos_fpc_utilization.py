import os
import paramiko
import re
import sys
import time
from pprint import pprint
import argparse
from lib_ssh_connectivity import Device
from lib_junos_sys_chassis import get_chassis_fpc
from lib_junos_sys_chassis import parse_chassis_fpc_output
from lib_junos_sys_chassis import sweep_status
from lib_backend_functions import determine_list_average
from lib_backend_functions import determine_list_highest_value



'''The following code can be used to execute this script file on 1 device under test.'''
cli_args = sys.argv[1:]
dut_ip = cli_args[0]
dut_user = cli_args[1]
dut_pass = cli_args[2]
interval_end = int(cli_args[3])


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
        #print(fpc_values)
        fpc_func_output = parse_chassis_fpc_output(fpc_values)
        #print(fpc_func_output)
        fpc_count = len(fpc_func_output)
        print(f"There are {fpc_count} FPC(s) online in {host_ip}")
        fpc_slots = []
        fpc_states = []
        fpc_cpu_util = []
        fpc_mem_util = []
        fpc_mem_heap = []
        fpc_mem_buffer = []
        #print(f'{fpc_func_output}')
        for fpc in fpc_func_output:
            #print(f'{fpc}')
            fpc_dict = fpc
            # append dict key values to pre-defined lists
            fpc_slot = fpc_dict['fpc_slot']
            fpc_state = fpc_dict['fpc_status']
            fpc_cpu_utilization = fpc_dict['fpc_cpu_util_pct']
            fpc_mem_utililization = fpc_dict['fpc_cpu_mem_dram_mb']
            fpc_mem_heap_utililization = fpc_dict['fpc_cpu_mem_util_heap']
            fpc_mem_buffer_utililization = fpc_dict['fpc_cpu_mem_util_buf']
            fpc_slots.append(fpc_slot)
            fpc_states.append(fpc_state)
            fpc_cpu_util.append(fpc_cpu_utilization)
            fpc_mem_util.append(fpc_mem_utililization)
            fpc_mem_heap.append(fpc_mem_heap_utililization)
            fpc_mem_buffer.append(fpc_mem_buffer_utililization)
            print(f"FPC {fpc_slot} state is {fpc_state}. Current CPU utilization is {fpc_cpu_utilization}. Current memory utilization is {fpc_mem_utililization}MB, buffer use % is {fpc_mem_buffer_utililization}, and heap use % is {fpc_mem_heap_utililization}.")
    except:
        print(f'An error occurred.')
    try:
        fpc_values = get_chassis_fpc(dut_host)
        fpc_online_list = sweep_status(fpc_values)
        fpc_count = len(fpc_online_list)
        # Get FPC utilization over a specified interval period
        interval_current = 0
        fpcs = []
        fpc_slot_0 = [0]
        fpc_slot_1 = [1]
        fpc_slot_2 = [2]
        fpc_slot_3 = [3]
        fpc_slot_4 = [4]
        fpc_slot_5 = [5]
        fpc_slot_6 = [6]
        fpc_slot_7 = [7]
        fpc_cpu_util = []
        fpc_mem_util = []
        fpc_mem_heap = []
        fpc_mem_buffer = []
        cpu_util_pct_slot0 = []
        cpu_util_pct_slot1 = []
        cpu_util_pct_slot2 = []
        cpu_util_pct_slot3 = []
        cpu_util_pct_slot4 = []
        cpu_util_pct_slot5 = []
        cpu_util_pct_slot6 = []
        cpu_util_pct_slot7 = []
        cpu_total_mem_slot0 = []
        cpu_total_mem_slot1 = []
        cpu_total_mem_slot2 = []
        cpu_total_mem_slot3 = []
        cpu_total_mem_slot4 = []
        cpu_total_mem_slot5 = []
        cpu_total_mem_slot6 = []
        cpu_total_mem_slot7 = []
        cpu_mem_util_heap_slot0 = []
        cpu_mem_util_heap_slot1 = []
        cpu_mem_util_heap_slot2 = []
        cpu_mem_util_heap_slot3 = []
        cpu_mem_util_heap_slot4 = []
        cpu_mem_util_heap_slot5 = []
        cpu_mem_util_heap_slot6 = []
        cpu_mem_util_heap_slot7 = []
        cpu_mem_util_buf_slot0 = []
        cpu_mem_util_buf_slot1 = []
        cpu_mem_util_buf_slot2 = []
        cpu_mem_util_buf_slot3 = []
        cpu_mem_util_buf_slot4 = []
        cpu_mem_util_buf_slot5 = []
        cpu_mem_util_buf_slot6 = []
        cpu_mem_util_buf_slot7 = []
        while interval_current <= interval_end:
            print(f"Interval {interval_current}")
            fpc_values = get_chassis_fpc(dut_host)
            for fpc in range(fpc_count):
                fpc_func_output = parse_chassis_fpc_output(fpc_values)
                fpc_count = len(fpc_func_output)
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
                if slot == '0':
                    cpu_util_pct_slot0.append(int(cpu_util_pct))
                    cpu_total_mem_slot0.append(int(cpu_total_mem))
                    cpu_mem_util_heap_slot0.append(int(cpu_mem_util_heap))
                    cpu_mem_util_buf_slot0.append(int(cpu_mem_util_buf))
                if slot == '1':
                    cpu_util_pct_slot1.append(int(cpu_util_pct))
                    cpu_total_mem_slot1.append(int(cpu_total_mem))
                    cpu_mem_util_heap_slot1.append(int(cpu_mem_util_heap))
                    cpu_mem_util_buf_slot1.append(int(cpu_mem_util_buf))
                if slot == '2':
                    cpu_util_pct_slot2.append(int(cpu_util_pct))
                    cpu_total_mem_slot2.append(int(cpu_total_mem))
                    cpu_mem_util_heap_slot2.append(int(cpu_mem_util_heap))
                    cpu_mem_util_buf_slot2.append(int(cpu_mem_util_buf))
                if slot == '3':
                    cpu_util_pct_slot3.append(int(cpu_util_pct))
                    cpu_total_mem_slot3.append(int(cpu_total_mem))
                    cpu_mem_util_heap_slot3.append(int(cpu_mem_util_heap))
                    cpu_mem_util_buf_slot3.append(int(cpu_mem_util_buf))
                if slot == '4':
                    cpu_util_pct_slot4.append(int(cpu_util_pct))
                    cpu_total_mem_slot4.append(int(cpu_total_mem))
                    cpu_mem_util_heap_slot4.append(int(cpu_mem_util_heap))
                    cpu_mem_util_buf_slot4.append(int(cpu_mem_util_buf))
                if slot == '5':
                    cpu_util_pct_slot5.append(int(cpu_util_pct))
                    cpu_total_mem_slot5.append(int(cpu_total_mem))
                    cpu_mem_util_heap_slot5.append(int(cpu_mem_util_heap))
                    cpu_mem_util_buf_slot5.append(int(cpu_mem_util_buf))
                if slot == '6':
                    cpu_util_pct_slot6.append(int(cpu_util_pct))
                    cpu_total_mem_slot6.append(int(cpu_total_mem))
                    cpu_mem_util_heap_slot6.append(int(cpu_mem_util_heap))
                    cpu_mem_util_buf_slot6.append(int(cpu_mem_util_buf))
                if slot == '7':
                    cpu_util_pct_slot7.append(int(cpu_util_pct))
                    cpu_total_mem_slot7.append(int(cpu_total_mem))
                    cpu_mem_util_heap_slot7.append(int(cpu_mem_util_heap))
                    cpu_mem_util_buf_slot7.append(int(cpu_mem_util_buf))
            interval_current += 1
        if len(cpu_util_pct_slot0) > 0:
            fpc_slot_0.append(cpu_util_pct_slot0)
            fpc_slot_0.append(cpu_total_mem_slot0)
            fpc_slot_0.append(cpu_mem_util_heap_slot0)
            fpc_slot_0.append(cpu_mem_util_buf_slot0)
        if len(cpu_util_pct_slot1) > 0:
            fpc_slot_1.append(cpu_util_pct_slot1)
            fpc_slot_1.append(cpu_total_mem_slot1)
            fpc_slot_1.append(cpu_mem_util_heap_slot1)
            fpc_slot_1.append(cpu_mem_util_buf_slot1)
        if len(cpu_util_pct_slot2) > 0:
            fpc_slot_2.append(cpu_util_pct_slot2)
            fpc_slot_2.append(cpu_total_mem_slot2)
            fpc_slot_2.append(cpu_mem_util_heap_slot2)
            fpc_slot_2.append(cpu_mem_util_buf_slot2)
        if len(cpu_util_pct_slot3) > 0:
            fpc_slot_3.append(cpu_util_pct_slot3)
            fpc_slot_3.append(cpu_total_mem_slot3)
            fpc_slot_3.append(cpu_mem_util_heap_slot3)
            fpc_slot_3.append(cpu_mem_util_buf_slot3)
        if len(cpu_util_pct_slot4) > 0:
            fpc_slot_4.append(cpu_util_pct_slot4)
            fpc_slot_4.append(cpu_total_mem_slot4)
            fpc_slot_4.append(cpu_mem_util_heap_slot4)
            fpc_slot_4.append(cpu_mem_util_buf_slot4)
        if len(cpu_util_pct_slot5) > 0:
            fpc_slot_5.append(cpu_util_pct_slot5)
            fpc_slot_5.append(cpu_total_mem_slot5)
            fpc_slot_5.append(cpu_mem_util_heap_slot5)
            fpc_slot_5.append(cpu_mem_util_buf_slot5)
        if len(cpu_util_pct_slot6) > 0:
            fpc_slot_6.append(cpu_util_pct_slot6)
            fpc_slot_6.append(cpu_total_mem_slot6)
            fpc_slot_6.append(cpu_mem_util_heap_slot6)
            fpc_slot_6.append(cpu_mem_util_buf_slot6)
        if len(cpu_util_pct_slot7) > 0:
            fpc_slot_7.append(cpu_util_pct_slot7)
            fpc_slot_7.append(cpu_total_mem_slot7)
            fpc_slot_7.append(cpu_mem_util_heap_slot7)
            fpc_slot_7.append(cpu_mem_util_buf_slot7)
        if len(fpc_slot_0) > 1:
            fpcs.append(fpc_slot_0)
        if len(fpc_slot_1) > 1:
            fpcs.append(fpc_slot_1)
        if len(fpc_slot_2) > 1:
            fpcs.append(fpc_slot_2)
        if len(fpc_slot_3) > 1:
            fpcs.append(fpc_slot_3)
        if len(fpc_slot_4) > 1:
            fpcs.append(fpc_slot_4)
        if len(fpc_slot_5) > 1:
            fpcs.append(fpc_slot_5)
        if len(fpc_slot_6) > 1:
            fpcs.append(fpc_slot_6)
        if len(fpc_slot_7) > 1:
            fpcs.append(fpc_slot_7)
    except:
        print('An error occurred.')
    try:
        print(f'########################################################')
        print(f'FPCs online in slots: {fpc_slots}')
        for s in fpcs:
            #print(s)
            fpc_id = s[0]
            fpc_cpu_util = s[1]
            fpc_mem_util = s[2]
            fpc_mem_heap = s[3]
            fpc_mem_buffer = s[4]
            print(f'########################################################')
            print(f'################# FPC SLOT {fpc_id} SUMMARY ###################')
            print(f'########################################################')
            fpc_cpu_util_avg = round(determine_list_average(fpc_cpu_util), 2)
            fpc_mem_util_avg = int(determine_list_average(fpc_mem_util))
            fpc_mem_heap_avg = round(determine_list_average(fpc_mem_heap), 2)
            fpc_mem_buffer_avg = round(determine_list_average(fpc_mem_buffer), 2)
            fpc_cpu_util_max = round(determine_list_highest_value(fpc_cpu_util), 2)
            print(f'FPC CPU utilizations after {interval_end}x 1 second iterations:')
            print(f'########################################################')
            print(f'FPC {fpc_id} CPU Utilization (Maximum): {fpc_cpu_util_max}%')
            print(f'FPC {fpc_id} CPU Utilization (Average): {fpc_cpu_util_avg}%')
            print(f'FPC {fpc_id} CPU Utilization - Total Memory (Average): {fpc_mem_util_avg}MB')
            print(f'FPC {fpc_id} CPU Utilization - Memory Heap (Average): {fpc_mem_heap_avg}%')
            print(f'FPC {fpc_id} CPU Utilization - Memory Buffer (Average): {fpc_mem_buffer_avg}%')
            print(f'########################################################')
            print(f'########################################################')
            print(f'########################################################')

    except:
        print(f'An error occurred.')


if __name__ == '__main__':
    main()
