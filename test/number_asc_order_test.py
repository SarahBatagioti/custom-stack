import pytest

from src.custom_stack_class import CustomStack
from src.number_asc_order import NumberAscOrder


def test_sort_returns_numbers_in_ascending_order_from_stack():
    stack = CustomStack(6)
    for number in [42, 7, 33, 15, 8, 26]:
        stack.push(number)

    sorter = NumberAscOrder()

    result = sorter.sort(stack)

    assert result == [7, 8, 15, 26, 33, 42]
    assert stack.size() == 6
    assert stack.top() == 26


def test_sort_returns_empty_list_for_empty_stack():
    stack = CustomStack(6)
    sorter = NumberAscOrder()

    result = sorter.sort(stack)

    assert result == []


def test_sort_raises_type_error_for_invalid_argument():
    sorter = NumberAscOrder()

    with pytest.raises(TypeError):
        sorter.sort([1, 2, 3, 4, 5, 6])
