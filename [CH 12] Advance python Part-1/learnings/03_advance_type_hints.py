# here i learnt advance type hints in pyhton

# Python's typing module provides more advanced type hints, such as List, Tuple, Dict, and Union.

from typing import List, Tuple, Dict, Union

# List of integers

numbers: List[int] = [1, 2, 3, 4, 5]

# Tuple of a string and an integer

person: Tuple[str, int] = ("Alice", 30)

# Dictionary with string keys and integer 

scores: Dict[str, int] = {"Alice": 90, "Bob": 85}

# Union type for variables that can hold multiple types

identifier: Union[int, str] = "ID123"

identifier = 12345 # Also valid