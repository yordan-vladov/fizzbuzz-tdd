import pytest
from fizzbuzz import fizzbuzz  # Import function (yet to be implemented)

def test_returns_number():
    assert fizzbuzz(3) == "Fizz"
    assert fizzbuzz(5) == "Buzz"
    assert fizzbuzz(15) == "FizzBuzz"
    assert fizzbuzz(7) == 7