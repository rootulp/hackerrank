# Problem Solving (Basic) Skill Verification Test
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getMinCost' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY employee_id
#  2. INTEGER_ARRAY job_id
#

def getMinCost(employee_id, job_id):
    employees = sorted(employee_id)
    jobs = sorted(job_id)
    total_distance = 0
    for index in range(len(employees)):
        total_distance += abs(employees[index] - jobs[index])
    return total_distance

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    employee_id_count = int(input().strip())

    employee_id = []

    for _ in range(employee_id_count):
        employee_id_item = int(input().strip())
        employee_id.append(employee_id_item)

    job_id_count = int(input().strip())

    job_id = []

    for _ in range(job_id_count):
        job_id_item = int(input().strip())
        job_id.append(job_id_item)

    result = getMinCost(employee_id, job_id)

    fptr.write(str(result) + '\n')

    fptr.close()
