import paramiko
from lib_ssh_connectivity import Device
#from lib-ssh_connectivity import create_handle
from lib_ssh_connectivity import create_handle_quiet
import os
import re
import sys
import time
from pprint import pprint
import argparse



'''Get FPC values from device'''
def get_chassis_fpc(dut_host):
    '''Command sets for device configuration'''
    command_set_1 = [f'show chassis fpc']
    '''Create handle'''
    dut_host_session = create_handle_quiet(dut_host)
    dut_host_terminal = dut_host_session.invoke_shell()
    #print(dir(dut_host_session))
    '''Start execution'''
    for command in command_set_1:
        print(f'Sending command: {command}\n')
        try:
            dut_host_terminal.send(f'{command}\n')
            time.sleep(1)
        except:
            print(f"An error occurred.")
        output = dut_host_terminal.recv(1000).decode('utf-8')
        #pprint(output)
    output_recv = output.split("\n")
    #pprint(output_recv)
    dut_host_terminal.send('exit\n')
    return output
    time.sleep(10)



'''Parse output from routing table data retrieved'''
def parse_chassis_fpc_output(fpc_values):
    fpc_inputs = fpc_values.split("\n")
    fpc_list = []
    fpc_dict = {}
    for line in fpc_inputs:
        if "Online" in line:
            fpc_online_temp_list = line.split()
            # print(fpc_online_temp_list)
            fpc_dict['fpc_slot'] =  fpc_online_temp_list[0]
            fpc_dict['fpc_status'] = fpc_online_temp_list[1]
            fpc_dict['fpc_temp'] = fpc_online_temp_list[2]
            fpc_dict['fpc_cpu_util_pct'] = fpc_online_temp_list[3]
            fpc_dict['fpc_cpu_intr_pct'] = fpc_online_temp_list[4]
            fpc_dict['fpc_cpu_1min_avg'] = fpc_online_temp_list[5]
            fpc_dict['fpc_cpu_5min_avg'] = fpc_online_temp_list[6]
            fpc_dict['fpc_cpu_15min_avg'] = fpc_online_temp_list[7]
            fpc_dict['fpc_cpu_mem_dram_mb'] = fpc_online_temp_list[8]
            fpc_dict['fpc_cpu_mem_util_heap'] = fpc_online_temp_list[9]
            fpc_dict['fpc_cpu_mem_util_buf'] = fpc_online_temp_list[10]
            fpc_list.append(fpc_dict)
    return fpc_list


def sweep_status(inputs):
    func_inputs = inputs.split("\n")
    fpc_list = []
    for line in func_inputs:
        #print(line)
        if "Online" in line:
            #print(line)
            fpc_online_temp_list = line.split()
            fpc_list.append(fpc_online_temp_list[0])
            #print(fpc_list)
    return fpc_list
