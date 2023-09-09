'''

a simple grading system for canadian computer competition
grades the

in windows, we can specify input and output like this: command.cmd <input.in >output.out
test files are named like this: s5.1-01.in and s5.2-03.out
'''

import sys, os, time, subprocess
from typing import *

PYTHON_HOME = "python3"
TIME_OUT = 5
GROUP_NUM = 4

print("running on platform: ", sys.platform)

test_data_dir = input("the directory of the test data>>")
program_dir = input("the directory of the python script>>")

test_data_filenames_by_groups = [
    [] for i in range(GROUP_NUM)
]  # by group


def identical_file_compare(inputs:str, outputs:str, expected_outputs:str) -> bool:
    # compares the expected and actual output to see if the answer is corrected
    # note some of the problems accept multiple outputs, this function should be altered in such case
    expected_outputs_lines = expected_outputs.splitlines()
    output_lines = outputs.splitlines()
    if (output_lines < expected_outputs_lines):
        return False
    for line_num in range(len(expected_outputs_lines)):
        p1 = expected_outputs_lines[line_num].split()
        p2 = output_lines[line_num].split()
        if len(p1) != len(p2):
            return False
        for i in range(len(p1)):
            if p1[i] != p2[i]:
                return False
    return True


for root, dirs, files in os.walk(test_data_dir):
    for file in files:
        if root != test_data_dir:  # if the file in the subdirectory of the selected directory
            continue  # ignore it
        try:
            test_group = int(file.split("-")[0].split(".")[1]) - 1
        except ValueError:
            continue

        file = file.split(".")[0] + "." + file.split(".")[1]
        test_data_filenames_by_groups[test_group].append(os.path.join(test_data_dir, file))

for group_num in range(len(test_data_filenames_by_groups)):
    print("<--testing group:", group_num + 1, "-->")
    for test_file_name in test_data_filenames_by_groups[group_num]:
        input_file = test_file_name + ".in"
        expected_output_file = test_file_name + ".out"
        output_file = test_file_name + ".my_answer"

        print("testing", test_file_name, "...", end="    ")

        run_test_command = PYTHON_HOME + " " + program_dir + " <" + input_file + " >" + output_file

        if (sys.platform != "win32"):
            run_test_command = run_test_command  # TODO adapt linux and unix

        starting_time = time.time()
        p = subprocess.Popen(run_test_command, shell=True)
        while p.poll() is None:
            if time.time() - starting_time > TIME_OUT:
                p.terminate()
                print('\033[33m<--TIME LIMIT EXCEEDED for test data ' + test_file_name + '-->\033[0m')
                break
            time.sleep(0.01)
        if p.poll() is None:
            p.communicate()
            continue
        else:
            finish_time = time.time()

            # call to judge function
            expected_outputs = ""
            outputs = ""
            inputs = ""
            with open(input_file, "r") as f:
                inputs = str(f.read())
            with open(expected_output_file, "r") as f:
                expected_outputs = str(f.read())
            with open(output_file, "r") as f:
                outputs = str(f.read())
            if identical_file_compare(inputs, outputs, expected_outputs):
                print("\033[32mOK\033[0m", end=" ")
                print("<--time used:", finish_time - starting_time, "-->")
            else:
                print("\033[31mWRONG ANSWER\033[0m")

    print("\n\n")
    