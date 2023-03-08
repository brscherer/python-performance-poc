# Useful to speed up string comparison when we need to compare some long string and the same value may appear many times
# Calling (intern()) explicitly will remove the burden of knowing implicit complex rules that can differ from version to version

import sys
# c = 'Y'*4097
# d = 'Y'*4097
# c is d # Outputs False

# c = sys.intern('Y'*4097)
# d = sys.intern('Y'*4097)
# c is d # Outputs True

# USING EQUALS INSTEAD OF IS, TO COMPARE VALUE IF IDENTITY IS DIFFERENT

c = 'Y'*4097
d = 'Y'*4097
c == d # Outputs True

# c = sys.intern('Y'*4097)
# d = sys.intern('Y'*4097)
# c == d # Outputs True