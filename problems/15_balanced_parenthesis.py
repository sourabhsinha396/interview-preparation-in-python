import pytest


def get_balacing_parenthsis(parenthesis:str) -> str:
	if parenthesis == ")":
		return "("
	if parenthesis == "}":
		return "{"
	if parenthesis == "]":
		return "["


def is_valid_parenthesis(input:str) -> bool:
	stack = []
	for item in input:
		if item in ["{","(","["]:
			stack.append(item)
		if item in [")","}","]"]:
			balancing_parenthsis = get_balacing_parenthsis(item)
			if balancing_parenthsis == stack[-1]:
				stack.pop()
		else:
			continue 
	if stack == []:
		return True
	return False


iterable = [
("{}",True),
("{(})",False),
]


@pytest.mark.parametrize("input,result",iterable)
def test_should_identify_valid_parenthesis(input,result):
	assert is_valid_parenthesis(input) == result
