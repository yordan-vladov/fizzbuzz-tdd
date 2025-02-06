import pytest
from fizzbuzz import fizzbuzz  # Import function (yet to be implemented)

def test_returns_number():
	simple_number = 1 # avoid magic numbers
	assert fizzbuzz(simple_number) == simple_number # Expect 1 to return 1
