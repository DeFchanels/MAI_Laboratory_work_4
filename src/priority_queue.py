from dataclasses import dataclass
from typing import Any

from src.errors import EmptyQueueError


@dataclass
class Element:
  id: int
  priority_level: int # Чем выше тем приоритетнее
  value: Any


class PriorityQueue:
    def __init__(self):
        self.elements = []

    def push(self, element):
        """
        Add an element to the priority queue
        Difficulty: O(n).
        Raises TypeError if element is not an instance of Element
        """
        if not isinstance(element, Element):
            raise TypeError('Argument must be an Element')
        self.elements.append(element)
        self.sort_down()

    def sort_down(self):
        """
        Sorts the queue by priority level—the higher the level, the closer to the front of the queue.
        If priorities are equal, the element that was added to the queue earlier will be positioned closer to the end of the queue.
        """
        for i in range(len(self.elements) - 1, 0, -1):
            if self.elements[i].priority_level <= self.elements[i - 1].priority_level: # Продвигаем элемент влево, пока его приоритет ниже. Если приоритеты равны, все равно сдвигаем, чтобы соблюдалось FIFO
                self.elements[i], self.elements[i - 1] = self.elements[i - 1], self.elements[i]
            else:
                break

    def pop(self):
        """
        Remove and return an element from the priority queue
        Difficulty: O(1).
        Raises EmptyQueueError if queue is empty
        """
        if not self.elements:
            raise EmptyQueueError("Pop from empty priority queue")
        return self.elements.pop()

    def __len__(self):
        """Returns a length of queue. Difficulty: O(1)."""
        return len(self.elements)

    def __bool__(self):
        """Returns True, if queue is not empty. Difficulty: O(1)."""
        return bool(self.elements)

    def peek(self):
        """
        Returns the element at the top of the priority queue without removing it.
        Difficulty: O(1).
        Raises EmptyQueueError if queue is empty
        """
        if not self.elements:
            raise EmptyQueueError("Peek from empty priority queue")
        return self.elements[-1]