T = [(1,2), (4,5), (6,7)]

import Func
Func.print_list(T)                  #imports all functions

import Func as f
f.print_list(T) 

from Func import *                  #imports every function and calls by the function only not the program
print_list(T)

from Func import print_list         #imports only function mentioned(can be print1,print2...)
print_list(T)

from Func import print_list as pl
pl(T)