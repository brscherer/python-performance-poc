print("===========================================================================\n\n\n\n")
# Reference: https://wiki.python.org/moin/PythonSpeed/PerformanceTips

import time

# Function call overhead in Python is relatively high.
start_time = time.time()
x = 0
def doit1(i):
    global x
    x = x + i

list = range(100000)
for i in list:
    doit1(i)
print("--- %s seconds ---" % (time.time() - start_time))

# This strongly suggest that when appropriate, function should handle data aggregation
start_time = time.time()
x = 0
def doit2(list):
    global x
    for i in list:
        x = x + i

list = range(100000)
doit2(list)
print("--- %s seconds ---" % (time.time() - start_time))

