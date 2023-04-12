import paramiko
from lib_ssh_connectivity import Device
from lib_ssh_connectivity import create_handle_quiet
import os
import re
import sys
import time
from pprint import pprint
import argparse
from collections import defaultdict



'''Get FPC values from device'''
def get_chassis_fpc(dut_host):
    '''Command sets for device configuration'''
    command_set_1 = [f'show chassis fpc']
    '''Create handle'''
    dut_host_session = create_handle_quiet(dut_host)
    dut_host_terminal = dut_host_session.invoke_shell()
    '''Start execution'''
    for command in command_set_1:
        print(f'Sending command: {command}\n')
        try:
            dut_host_terminal.send(f'{command}\n')
            time.sleep(1)
        except:
            print(f"An error occurred.")
        output = dut_host_terminal.recv(1000).decode('utf-8')
    output_recv = output.split('\n')
    dut_host_terminal.send('exit\n')
    return output
    time.sleep(10)






'''
for line in f.split('\n'):
    slot,status,temp,fpc_cpu_util_pct,fpc_cpu_intr_pct,fpc_cpu_1min_avg,fpc_cpu_5min_avg,fpc_cpu_15min_avg,fpc_cpu_mem_dram_mb,fpc_cpu_mem_util_heap,fpc_cpu_mem_util_buf = line.split()

    out[typ][name] = price

dict(out)

out = defaultdict(dict)

for line in f.split('\n'):
    typ,name,price = line.split(';')
    out[typ][name] = price

dict(out)
'''
['Last login: Wed Apr 12 16:17:12 2023 from 10.10.196.20\r\r',
'--- JUNOS 20.3X75-D43.10 Kernel 64-bit  JNPR-11.0-20230201.7537bf2_buil\r',
'show chassis fpc\r',
'{master}\r',
'csim@bentwaters-vc-car-r1> show chassis fpc \r',
'                     Temp  CPU Utilization (%)   CPU Utilization (%)  Memory    Utilization (%)\r',
'Slot State            (C)  Total  Interrupt      1min   5min   15min  DRAM (MB) Heap     Buffer\r',
'  0  Empty           \r',
'  1  Online            44     28          3       28     28     28    2048       66         28\r',
'  2  Online            45     31          5       31     31     31    2048       65         28\r',
'  3  Online            52     29          0       28     29     29    2048       71         20\r',
'  4  Online            60     16          0       15     15     15    3168       35         26\r',
'  5  Empty           \r',
'\r',
'{master}\r',
'csim@bentwaters-vc-car-r1> ']

'''Parse output from routing table data retrieved'''
def parse_chassis_fpc_output(fpc_values):
    fpc_inputs = []
    fpc_inputs = fpc_values.split('\r\n')
    fpc_slot_ids = []
    fpc_list = []
    fpc_dict = {}
    for line in fpc_inputs:
        if "Online" in line:
            # print("3###########################")
            # print(line)
            fpc_online_temp_list = line.split()
            # print("3.5###########################")
            # print(fpc_online_temp_list)
            fpc_slot_id = fpc_online_temp_list[0]
            fpc_slot_ids.append(fpc_online_temp_list[0])
            # print("3.6###########################")
            # print(fpc_slot_ids)
            fpc_dict = {
                        'fpc_slot' : fpc_online_temp_list[0],
                        'fpc_status' : fpc_online_temp_list[1],
                        'fpc_temp' : fpc_online_temp_list[2],
                        'fpc_cpu_util_pct' : fpc_online_temp_list[3],
                        'fpc_cpu_intr_pct' : fpc_online_temp_list[4],
                        'fpc_cpu_1min_avg' : fpc_online_temp_list[5],
                        'fpc_cpu_5min_avg' : fpc_online_temp_list[6],
                        'fpc_cpu_15min_avg' : fpc_online_temp_list[7],
                        'fpc_cpu_mem_dram_mb' : fpc_online_temp_list[8],
                        'fpc_cpu_mem_util_heap' : fpc_online_temp_list[9],
                        'fpc_cpu_mem_util_buf' : fpc_online_temp_list[10]
                        }

            # print("4###########################")
            fpc_list.append(fpc_dict)
            # print("5###########################")
            # print(fpc_dict)
            # print("6###########################")
            # print(fpc_list)
    return fpc_list

'''
[{'fpc_slot': '1', 'fpc_status': 'Online', 'fpc_temp': '45', 'fpc_cpu_util_pct': '27', 'fpc_cpu_intr_pct': '3', 'fpc_cpu_1min_avg': '28', 'fpc_cpu_5min_avg': '28', 'fpc_cpu_15min_avg': '29', 'fpc_cpu_mem_dram_mb': '2048', 'fpc_cpu_mem_util_heap': '66', 'fpc_cpu_mem_util_buf': '28'},
{'fpc_slot': '2', 'fpc_status': 'Online', 'fpc_temp': '45', 'fpc_cpu_util_pct': '31', 'fpc_cpu_intr_pct': '6', 'fpc_cpu_1min_avg': '31', 'fpc_cpu_5min_avg': '31', 'fpc_cpu_15min_avg': '31', 'fpc_cpu_mem_dram_mb': '2048', 'fpc_cpu_mem_util_heap': '65', 'fpc_cpu_mem_util_buf': '28'},
{'fpc_slot': '3', 'fpc_status': 'Online', 'fpc_temp': '52', 'fpc_cpu_util_pct': '30', 'fpc_cpu_intr_pct': '0', 'fpc_cpu_1min_avg': '32', 'fpc_cpu_5min_avg': '30', 'fpc_cpu_15min_avg': '29', 'fpc_cpu_mem_dram_mb': '2048', 'fpc_cpu_mem_util_heap': '71', 'fpc_cpu_mem_util_buf': '20'},
{'fpc_slot': '4', 'fpc_status': 'Online', 'fpc_temp': '60', 'fpc_cpu_util_pct': '15', 'fpc_cpu_intr_pct': '0', 'fpc_cpu_1min_avg': '15', 'fpc_cpu_5min_avg': '15', 'fpc_cpu_15min_avg': '15', 'fpc_cpu_mem_dram_mb': '3168', 'fpc_cpu_mem_util_heap': '35', 'fpc_cpu_mem_util_buf': '26'}]
'''
            # return fpc_list
    #         fpc_dict['fpc_slot'] =  fpc_online_temp_list[0]
    #         fpc_dict['fpc_status'] = fpc_online_temp_list[1]
    #         fpc_dict['fpc_temp'] = fpc_online_temp_list[2]
    #         fpc_dict['fpc_cpu_util_pct'] = fpc_online_temp_list[3]
    #         fpc_dict['fpc_cpu_intr_pct'] = fpc_online_temp_list[4]
    #         fpc_dict['fpc_cpu_1min_avg'] = fpc_online_temp_list[5]
    #         fpc_dict['fpc_cpu_5min_avg'] = fpc_online_temp_list[6]
    #         fpc_dict['fpc_cpu_15min_avg'] = fpc_online_temp_list[7]
    #         fpc_dict['fpc_cpu_mem_dram_mb'] = fpc_online_temp_list[8]
    #         fpc_dict['fpc_cpu_mem_util_heap'] = fpc_online_temp_list[9]
    #         fpc_dict['fpc_cpu_mem_util_buf'] = fpc_online_temp_list[10]
    #         print("4###########################")
    #         fpc_list.append(fpc_dict)
    #         print("5###########################")
    #         print(fpc_dict)
    #         print("6###########################")
    #         print(fpc_list)
    # return fpc_list


def sweep_status(inputs):
    func_inputs = inputs.split("\n")
    fpc_list = []
    for line in func_inputs:
        if "Online" in line:
            fpc_online_temp_list = line.split()
            fpc_list.append(fpc_online_temp_list[0])
    return fpc_list
