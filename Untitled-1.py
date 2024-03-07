from array import *
vals = array('i',[5,9,8,4,2])
print(vals)
vals = array('i',[5,9,-8,4,2])
print(vals.buffer_info())
vals.reverse()
print(vals)
# for i in range(len(vals)):
     # print(vals[i])
for i in vals:
    print(i)