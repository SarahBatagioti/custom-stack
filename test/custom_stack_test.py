import pytest

from src.custom_stack_class import CustomStack, StackEmptyException, StackFullException


def test_push_adds_element_and_updates_stack_state():
    cut = CustomStack(5)

    cut.push(5.0)

    assert cut.is_empty() is False
    assert cut.top() == 5.0
    assert cut.size() == 1


def test_pop_returns_last_element_and_decrements_size():
    cut = CustomStack(5)
    cut.push(10)
    cut.push(20)

    result = cut.pop()

    assert result == 20
    assert cut.top() == 10
    assert cut.size() == 1


def test_push_raises_exception_when_stack_is_full():
    cut = CustomStack(2)
    cut.push(10)
    cut.push(20)

    with pytest.raises(StackFullException):
        cut.push(30)


def test_pop_raises_exception_when_stack_is_empty():
    cut = CustomStack(3)

    with pytest.raises(StackEmptyException):
        cut.pop()


def test_top_raises_exception_when_stack_is_empty():
    cut = CustomStack(3)

    with pytest.raises(StackEmptyException):
        cut.top()
