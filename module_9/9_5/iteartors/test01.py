#1 

import sys
from itertools import repeat

ex_itertor = repeat("4", 100_000)
print(ex_itertor)
print(f"Размер итератора - {sys.getsizeof(ex_itertor)}")

ex_str = "4" * 100_000
print(f"Размер строки - {sys.getsizeof(ex_str)}")