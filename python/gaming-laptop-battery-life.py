# Problem Solving (Basic) Skill Verification Test

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getBattery' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY events as parameter.
#

def getBattery(events):
    battery_level = 50
    while events != []:
        battery_level = perform_event(events.pop(0), battery_level)
    return battery_level

def perform_event(event, battery_level):
    potential_battery = battery_level + event
    if potential_battery >= 100:
        return 100
    elif potential_battery <= 0:
        return 0
    else:
        return potential_battery

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    events_count = int(input().strip())

    events = []

    for _ in range(events_count):
        events_item = int(input().strip())
        events.append(events_item)

    result = getBattery(events)

    fptr.write(str(result) + '\n')

    fptr.close()
