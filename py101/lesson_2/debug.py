# debug.py

import pdb

counter = 1

pdb.set_trace() # Another breakpoint

while counter <= 5:
    print(counter)
    pdb.set_trace()  # Add breakpoint
    counter += 1

#Output:
#1
#> /Users/xyzzy/ls_test/test.py(10)<module>()
#-> counter += 1
#(Pdb)

#meaning -> counter += 1 program execution stopped at this line. where we added the breakpoint.