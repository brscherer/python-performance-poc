print("===========================================================================\n\n\n\n")
# Reference: https://wiki.python.org/moin/PythonSpeed/PerformanceTips

import time

words = ["some", "python", "performance", "tips", "python", "tips", "python", "performance"]
# Simple way of building a dictionary of words frequency
start_time = time.time()
wdict = {}
for word in words:
    if word not in wdict:
        wdict[word] = 0
    wdict[word] += 1
wdict
print("--- %s seconds ---" % (time.time() - start_time))

# It will enter in if statement only the first time word is found, subsequent finds will always fail if clause
# In situations like this where initialization value is only going to occur once and the augmentation of that value will occur many times, is cheaper use a `try`` statement:
start_time = time.time()
wdict = {}
for word in words:
    try:
        wdict[word] += 1
    # It is important catch expected `KeyError` and not have a default `except`
    except KeyError:
        wdict[word] = 1
wdict
print("--- %s seconds ---" % (time.time() - start_time))

# Python 2.x release brought `get()` method which wil return a default value if the desired key isn't found in the dictionary
start_time = time.time()
wdict = {}
get = wdict.get
for word in words:
    wdict[word] = get(word, 0) + 1
print("--- %s seconds ---" % (time.time() - start_time))

# It doesn't avoid having to look up the key twice, but at least the double lookup is performed in C.