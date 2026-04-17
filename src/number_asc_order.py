from src.custom_stack_class import CustomStack


class NumberAscOrder:

    def sort(self, stack):
        if not isinstance(stack, CustomStack):
            raise TypeError("stack deve ser uma instância de CustomStack")

        if stack.is_empty():
            return []

        return sorted(stack.elements)
