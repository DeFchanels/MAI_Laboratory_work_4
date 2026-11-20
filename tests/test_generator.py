import pytest

from src.generator import (
    generate_almost_sorted,
    generate_random,
    generate_reversed,
    generate_sorted,
    generate_with_duplicates,
)


@pytest.mark.parametrize(
    "gen_func",
    [
        generate_random,
        generate_sorted,
        generate_reversed,
        generate_almost_sorted,
        generate_with_duplicates,
    ],
)
def test_generator_minus_n_error(gen_func):
    with pytest.raises(ValueError):
        gen_func(n = -5) # Отрицательный размер n вызывает ValueError


@pytest.mark.parametrize(
    "gen_func",
    [
        generate_random,
        generate_sorted,
        generate_reversed,
        generate_almost_sorted,
        generate_with_duplicates,
    ],
)
def test_generator_bounds_error(gen_func):
    with pytest.raises(ValueError):
        gen_func(n = 10, low_bound = 100, high_bound = 0) # Ошибочные границы (low > high) вызывают ValueError


@pytest.mark.parametrize(
    "gen_func",
    [
        generate_random,
        generate_sorted,
        generate_reversed,
        generate_almost_sorted,
        generate_with_duplicates,
    ],
)
def test_generator_empty_list(gen_func):
    assert gen_func(n = 0) == []

@pytest.mark.parametrize(
    "gen_func",
    [
        generate_random,
        generate_sorted,
        generate_reversed,
        generate_almost_sorted,
        generate_with_duplicates,
    ],
)
def test_generator_one_item_list(gen_func):
    res = gen_func(n = 1)
    assert len(res) == 1

def test_generate_sorted_properties():
    n = 100
    res = generate_sorted(n, seed=111)
    assert len(res) == n
    for i in range(len(res) - 1): # Проверяем отсортированность по возрастанию
        assert res[i] <= res[i + 1]

def test_generate_reversed_properties():
    n = 100
    res = generate_reversed(n, seed=111)
    assert len(res) == n
    for i in range(len(res) - 1): # Проверяем отсортированность по убыванию
        assert res[i] >= res[i + 1]

def test_generator_bounds():
    n = 50
    res = generate_random(n, seed=111, low_bound=1, high_bound=10)
    assert len(res) == n
    for val in res: # Проверяем, что все элементы лежат в заданном диапазоне
        assert 1 <= val <= 10


def test_generate_almost_sorted_properties():
    n = 100
    res = generate_almost_sorted(n, seed=111)
    assert len(res) == n
    sorted_copy = sorted(res)
    assert sorted(res) == sorted_copy  # Cами элементы списка те же
    all_sorted = all(res[i] <= res[i + 1] for i in range(len(res) - 1)) # Хотя бы один элемент стоит не на своем отсортированном месте
    assert not all_sorted, "Почти отсортированный массив остался полностью отсортированным (Возможно случайно)"


def test_generate_with_duplicates_unique_count():
    n = 200
    res = generate_with_duplicates(n, seed=111, unique_count=10)
    assert len(res) == n
    assert len(set(res)) <= 10 # Количество уникальных элементов меньше или равно unique_count


def test_generate_with_duplicates_validation():
    with pytest.raises(ValueError):
        generate_with_duplicates(n=10, unique_count=0)


@pytest.mark.parametrize(
    "gen_func",
    [
        generate_random,
        generate_sorted,
        generate_reversed,
        generate_almost_sorted,
        generate_with_duplicates,
    ],
)
def test_generators_reproducibility(gen_func):
    seed = 100
    res1 = gen_func(n=50, seed=seed)
    res2 = gen_func(n=50, seed=seed)
    assert res1 == res2 # Одинаковый seed дает абсолютно одинаковые списки
    res3 = gen_func(n=50, seed=11)
    if gen_func in [generate_random, generate_almost_sorted, generate_with_duplicates]: # В общем случае (с разными сидами) наборы будут отличаться
        assert res1 != res3