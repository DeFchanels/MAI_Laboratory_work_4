import pytest

from src.errors import EmptyQueueError
from src.priority_queue import Element, PriorityQueue


def test_priority_queue_empty_init():
    pq = PriorityQueue()
    assert len(pq) == 0
    assert not pq


def test_priority_queue_push_type_validation():
    pq = PriorityQueue()
    with pytest.raises(TypeError):
        pq.push("not an element")
    with pytest.raises(TypeError):
        pq.push({"id": 1, "priority_level": 5, "value": "data"})


def test_priority_queue_empty_pop_and_peek():
    pq = PriorityQueue()
    with pytest.raises(EmptyQueueError):
        pq.pop()
    with pytest.raises(EmptyQueueError):
        pq.peek()


def test_priority_queue_priority_order():
    pq = PriorityQueue()
    pq.push(Element(id=1, priority_level=10, value="low_priority"))
    pq.push(Element(id=2, priority_level=100, value="high_priority"))
    pq.push(Element(id=3, priority_level=50, value="medium_priority"))
    assert len(pq) == 3
    assert bool(pq) is True
    # Проверяем peek (не удаляет элемент)
    assert pq.peek().value == "high_priority"
    assert len(pq) == 3
    # Проверяем порядок извлечения pop()
    assert pq.pop().value == "high_priority"
    assert pq.pop().value == "medium_priority"
    assert pq.pop().value == "low_priority"
    assert len(pq) == 0
    assert not pq


def test_priority_queue_fifo_tie_breaking():
    pq = PriorityQueue()
    pq.push(Element(id=1, priority_level=10, value="first"))
    pq.push(Element(id=2, priority_level=10, value="second"))
    pq.push(Element(id=3, priority_level=10, value="third"))
    assert pq.pop().value == "first"
    assert pq.pop().value == "second"
    assert pq.pop().value == "third"


def test_priority_queue_mixed_push_pop():
    pq = PriorityQueue()
    pq.push(Element(id=1, priority_level=20, value="a"))
    pq.push(Element(id=2, priority_level=10, value="b"))
    assert pq.pop().value == "a"  # остался b (priority 10)
    pq.push(Element(id=3, priority_level=30, value="c"))  # теперь в очереди b(10) и c(30)
    assert pq.peek().value == "c"
    assert pq.pop().value == "c"
    assert pq.pop().value == "b"
    assert len(pq) == 0