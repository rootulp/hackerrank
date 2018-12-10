#!/bin/python3

import math
import os
import random
import re
import sys
from statistics import median

def getTrailingExpenditures(dayNumber, dailyExpenditures, trailingDays):
    return dailyExpenditures[dayNumber - trailingDays : dayNumber]

def getTrailingMedian(dayNumber, dailyExpenditures, trailingDays):
    trailingExpenditures = getTrailingExpenditures(dayNumber, dailyExpenditures, trailingDays)
    return median(trailingExpenditures)

def activityNotificationOnDay(dayNumber, dailyExpenditures, trailingDays):
    """
    Returns True if there an activity notification will be triggered on dayNumber
    Returns False if no activity notification will be triggered on dayNumber
    """
    todaySpend = dailyExpenditures[dayNumber]
    trailingMedian = getTrailingMedian(dayNumber, dailyExpenditures, trailingDays)
    return todaySpend >= 2 * trailingMedian

def activityNotifications(dailyExpenditures, trailingDays):
    activityNotifications = 0
    for dayNumber in range(trailingDays, len(dailyExpenditures)):
        if activityNotificationOnDay(dayNumber, dailyExpenditures, trailingDays):
            activityNotifications += 1

    return activityNotifications

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nd = input().split()
    n = int(nd[0])
    d = int(nd[1])
    expenditure = list(map(int, input().rstrip().split()))
    result = activityNotifications(expenditure, d)
    fptr.write(str(result) + '\n')
    fptr.close()
