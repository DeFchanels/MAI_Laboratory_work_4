import pytest

from src.sort_algorithms import heap_sort, selection_sort


@pytest.mark.parametrize("sort_func", [selection_sort, heap_sort])
def test_sort_empty_and_single(sort_func):
    assert sort_func([]) == []
    arr = [11]
    res = sort_func(arr)
    expected = [11]
    assert res == expected
    assert res == expected


@pytest.mark.parametrize("sort_func", [selection_sort, heap_sort])
def test_sort_basic_and_random(sort_func):
    data = [5, -2, 9, 1, 5, 6, 0, -10]
    expected = sorted(data)
    arr = data.copy()
    res = sort_func(arr)
    sorted_arr = res
    assert sorted_arr == expected


@pytest.mark.parametrize("sort_func", [selection_sort, heap_sort])
def test_sort_edge_cases(sort_func):
    cases = [
        [1, 2, 3, 4, 5],  # уже отсортирован
        [5, 4, 3, 2, 1],  # обратно отсортирован
        [7, 7, 7, 7, 7],  # сплошные дубликаты
        [3, 1, 4, 1, 5, 9, 2, 6],  # с дубликатами
    ]
    for case in cases:
        expected = sorted(case)
        arr = case.copy()
        res = sort_func(arr)
        sorted_arr = arr if res is None else res
        assert sorted_arr == expected