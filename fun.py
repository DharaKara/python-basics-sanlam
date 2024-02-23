# this is name file
import cool
print(cool.to_upper_case("Alex"))

# Importing only the to_upper_case function from cool.py (few functions)
from cool import to_upper_case
print(to_upper_case("Alex"))

# Importing the entire cool module with an alias
from cool import to_upper_case as to_upper

# Inbuild
from math import pi
