"""Difference between fsum() and sum()
fsum() is included in Python math module so we have to import it before using.
Where as sum() is part of built in functions of core Python so no need to import any library. 
fsum() returns always float dtype. However sum() returns the same dtype of input number."""
import math
a=print(math.fsum([2,3,6,8]))
a=print(sum([2,3,6,8]))
