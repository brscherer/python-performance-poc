print("===========================================================================\n\n\n\n")
# Reference: https://wiki.python.org/moin/PythonSpeed/PerformanceTips

import time
# Even with a simple body of a loop, the interpreter overhead of the `for`` loop itself can be a substantial amount of overhead.
start_for_time = time.time()
wordlist = ["some", "python", "performance", "tips"]

newlist = []
for word in wordlist:
    newlist.append(word.upper())

newlist
print("--- %s seconds ---" % (time.time() - start_for_time))

# Using `map` we push the loop from interpreter into compiled C code, but the restriction is we need to use a function (str.upper) instead of `body` instruction
start_map_time = time.time()
newlist = map(str.upper, wordlist)
print("--- %s seconds ---" % (time.time() - start_map_time))

# List comprehension provides a syntatically more compact and more efficient way of writing above for loop
start_lc_time = time.time()
newlist = [s.upper() for s in wordlist]
print("--- %s seconds ---" % (time.time() - start_lc_time))

# Similar to List Comprehensions, we can use Generators (added in Python 2.4). They is almost the same, but generators avoid the overhead of generating entire list at once
start_generator_time = time.time()
iterator = (s.upper() for s in wordlist)
print("--- %s seconds ---" % (time.time() - start_generator_time))
