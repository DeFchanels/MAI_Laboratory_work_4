import time

from generator import (
    generate_almost_sorted,
    generate_random,
    generate_reversed,
    generate_sorted,
    generate_with_duplicates,
)
from sort_algorithms import heap_sort, selection_sort


def measure_time(sort_func, data, repeats = 5):
    """
    Measure the average execution time of a sorting function in milliseconds.
    Performs validation against `sorted(data)` and returns the average time over `repeats` runs.
    """
    expected_result = sorted(data)  # ожидаемый результат сортировки
    times = []
    for i in range(repeats):
        arr = data.copy()  # копируем данные до старта таймера
        start = time.perf_counter() # Запускаем таймер
        result = sort_func(arr) # Сортируем
        end = time.perf_counter() # Останавливаем таймер
        assert result == expected_result, f"Ошибка в {sort_func.__name__}"
        times.append((end - start) * 1000)  # переводим секунды в миллисекунды
    return sum(times) / len(times) # Возвращаем среднее время


def run_benchmarks():
    algorithms = {
        "Heap Sort": heap_sort,
        "Selection Sort": selection_sort,
    }
    generators = {
        "random": generate_random,
        "sorted": generate_sorted,
        "reversed": generate_reversed,
        "almost_sorted": generate_almost_sorted,
        "duplicates": generate_with_duplicates,
    }
    sizes = [100, 10000, 100000, 1000000]
    seed = 111
    print(f"{'Dataset':<15} | {'Size':<6} | {'Selection (ms)':<15} | {'Heap (ms)':<12}")
    print("-" * 56)
    for gen_name, gen_func in generators.items():
        for n in sizes:
            base_data = gen_func(n, seed=seed) # Генерим массив, на котором будем тестировать сортировки
            sel_time = measure_time(algorithms["Selection Sort"], base_data) # Сортировка выбором
            heap_time = measure_time(algorithms["Heap Sort"], base_data) # Сортировка 'пирамидой'
            print(f"{gen_name:<15} | {n:<6} | {sel_time:<12.3f} | {heap_time:<12.3f}")
        print("-" * 56)


if __name__ == "__main__":
    run_benchmarks()