import pytest
from PyShapes.PyShape import *
import os.path

def test_get_area():
	obj = PyShape(os.path.abspath("./tests/shapes1.png"))
	assert obj.get_area("circle", 1) == -1

def main():
	test_get_area()

if __name__ == "__main__":
	main()
