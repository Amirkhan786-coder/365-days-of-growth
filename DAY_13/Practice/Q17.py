# Q17. Display Python module search paths.

import sys

print("Python Module Search Paths:")

for path in sys.path:
    print(path)