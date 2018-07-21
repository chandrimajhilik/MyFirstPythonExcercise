import os
from indexed import IndexedOrderedDict
clear = lambda :os.system('cls')
d={1:'One',2:'Two',3:'Three'}
ix = IndexedOrderedDict(sorted(d.items(),key=lambda t:t[0]))
