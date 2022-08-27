# While a user is downloading a file which is X bytes in size, your job is to provide a function to
# estimate the time remaining in minutes. The system has a record of the amount (in bytes) B
# downloaded each minute.
# If the file is not completely downloaded, estimate the rate by taking the simple average of the last
# Z observations.
# Write a function:
# def solution(X, B, Z)
# that returns the amount of time remaining in minutes. X is an integer representing the file size. B is
# a length K array of integers listing the bytes downloaded at each minute starting from the
# beginning of the download until now. Return an integer representing the number of minutes
# remaining. Z is an integer. You may assume that all the values are reasonable.
# Example:
# 1. X=100, B= (10,6,6,8], Z=2
# 30 bytes = 10+6+6+8 have been downloaded.
# So 70 bytes remain.
# The average of the last two minutes (Z=2) is 7=(6+8)/2.
# The function should return 10 minutes (70/7).
# 2. X=10, B=[2,3), Z=2
# 5 bytes = 2+3 have been downloaded.
# So 5 bytes remain.
# The average of the last two minutes (Z=2) is 2.5=(2+3)/2.
# The function should return 2 minutes (=5/2.5).
# Note that:
# * If there are fewer than Z observations, use what you do have.
# * Your estimate of the time remaining should be rounded up to the nearest integer (ceiling).
# * Compute the average rate as a floating point number.
# * If the download is done, return O
# * If you are unable to produce an estimate, return -1.

import math
def solution(X, B, Z):
    if(Z > 0):
        total_downloaded = 0
        for i in B:
            total_downloaded = total_downloaded + i

        remaining = X - total_downloaded
        last_Z_mins = B[-Z:]
        total_downloaded
        sum_of_Z_mins = 0

        for i in last_Z_mins:
            sum_of_Z_mins = sum_of_Z_mins + i
        
        average_of_last_minutes = sum_of_Z_mins/Z
        return math.ceil(remaining/average_of_last_minutes)
    else:
        return -1

print(solution(10, [2,3], 2))



# From an integer X representing a time duration in seconds produce a simplified string
# representation.
# For example, given X=100, you should output: "1m40s"
# Use the following abbreviations w,d,h,m,s to represent:
# * 1w is 1 week
# * 1d is 1 day
# * Th is 1 hour
# * 1m is 1 minute
# * 1s is 1 second
# 
# Only the two largest non-zero units should be used. Round up the second unit if necessary so that
# the output only has two units even though this might mean the output represents slightly more
# time than X seconds
# Write a function:
# def solution(x)
# that, given an integer X, returns a string representing the duration.
# Examples:
# 1. Given X=100, return "1m40s"
# 2. Given X=7263, return "2h2m". (7263s=2h1m3s, but this uses too many units, so we round the
# second largest unit up to 2h2m)
# 3. Given X=3605, return "1h5s"
# Notes;
# * If a single unit is sufficient, then the output should only include one unit. ex. X=3600 outputs "1h",
# not "1hOs".
# * The output should be as close as possible to the real time without being less than X. ex.
# X=86461 is "1d1m1s" so the output would be "1d2m". Not "1d1h".
# * There should always be some output. The empty string ("") is not the outcome of any X.

def solution2(X):
    s = 0
    w = 604800
    d = 86400
    h = 3600
    m = 60

    list_of_measurements = [m, h, d , w]
    for i in list_of_measurements:
        if(X == i):
            result = f'{X}{i}'
            return result

    if(X > m and X < h):
        minutes_count = math.floor(X/m)
        seconds_count = X - m
        result = f'{minutes_count}m{seconds_count}s'
        return result
    elif(X > h and X < d):
        hours_count = math.floor(X/h)
        seconds_count = X - h
        if(seconds_count > 60):
            minutes_count = math.ceil(seconds_count / 3600)
            result = f'{hours_count}h{minutes_count}m'
        else:
            result = f'{hours_count}h{seconds_count}s'
        return result

print(solution2(100))



# An internal unit of company XYZ provides services to other departments,
# 2
# Service prices are fixed at the beginning of the quarter based on projected expenses and
# utilization. However, usage is billed at the end of the quarter.
# So while composing quarterly invoices there may be an excess. We suppose planning is very
# good, so there is only evèr a modest overage.
# This amount should be returned to the departments by discounting a portion of it on each
# invoice.
# Your job is to write a function which considers the excess S and allocates it fairly. Allocation
# proceeds from the largest to the smallest invoice. And is distributed as the ratio of the invoice's
# contribution to the sum of itself and those which follow.
# Example 1:
# Given S="300.01" and B=("300.00 "200.00""7 00.00"/..
# R[0] = "150.00 (=300.07 * 300.00/600.00)
# R(1] = "100.00" (=150.07 * 200.00/300.00)
# R[2] = "50.01" (=50.07 * 100.00/100.00)
# en
# Example 2 (Pay careful attention to this one):
# Given S="1.00" and B=I"0.05""1.00"].
# 1. First we consider 1.00 because it is the largest,
# a. 1.00 * 1.00 / 1:05 ~= 0.95238...
# b. Round 0.95238... to "0.95". Rounding down to carry pennies to smaller departments.
# C. Set Ri1=0.95 . Notice, this is in the same place as 1.00. It is the 2nd value in the result!
# 2. Now we have 0.05 left
# 3. Next we look at the smaller BI0]=0.05 department
# a. 0.05 * 0.05 / 0.05 = 0.05
# b. No rounding required
# C. Set RIO]=0.05.
# R=["0.05""0.95")