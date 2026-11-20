import random


def generate_reversed(n, seed=None, low_bound = -1000, high_bound = 1000):
    """Generates n random elements from high to low.
    Get as arguments:
    1. n: number of elements in target list
    2. seed: seed for random number generator (optional)
    3. low_bound: lower bound of elements (optional, default=-1000)
    4. high_bound: upper bound of elements (optional, default=1000)
    Raises:
        ValueError: if n < 0 or low_bound > high_bound.
    """
    if n < 0:
        raise ValueError("Size n must be zero or positive")
    if low_bound > high_bound:
        raise ValueError("Lower bound 'low' cannot exceed 'high'")
    rng_generator = random.Random(seed) # Создаем генератор, зависящий от введенного (или none по дефолту) seed
    res = [rng_generator.randint(low_bound, high_bound) for i in range(n)]
    res.sort(reverse=True)
    return res


def generate_sorted(n, seed=None, low_bound = -1000, high_bound = 1000):
    """Generates n random elements from low to high.
    Get as arguments:
    1. n: number of elements in target list
    2. seed: seed for random number generator (optional)
    3. low_bound: lower bound of elements (optional, default=-1000)
    4. high_bound: upper bound of elements (optional, default=1000)
    Raises:
        ValueError: if n < 0 or low_bound > high_bound.
    """
    if n < 0:
        raise ValueError("Size n must be zero or positive")
    if low_bound > high_bound:
        raise ValueError("Lower bound 'low' cannot exceed 'high'")
    rng_generator = random.Random(seed) # Создаем генератор, зависящий от введенного (или none по дефолту) seed
    res = [rng_generator.randint(low_bound, high_bound) for i in range(n)]
    res.sort()
    return res


def generate_random(n, seed=None, low_bound = -1000, high_bound = 1000):
    """Generates n random elements.
    Get as arguments:
    1. n: number of elements in target list
    2. seed: seed for random number generator (optional)
    3. low_bound: lower bound of elements (optional, default=-1000)
    4. high_bound: upper bound of elements (optional, default=1000)
    Raises:
        ValueError: if n < 0 or low_bound > high_bound.
    """
    if n < 0:
        raise ValueError("Size n must be zero or positive")
    if low_bound > high_bound:
        raise ValueError("Lower bound 'low' cannot exceed 'high'")
    rng_generator = random.Random(seed) # Создаем генератор, зависящий от введенного (или none по дефолту) seed
    res = [rng_generator.randint(low_bound, high_bound) for i in range(n)]
    return res


def generate_almost_sorted(n, seed=None, low_bound = -1000, high_bound = 1000):
    """Generates n random elements from low to high, but close to 5% of elements will be swapped.
    Get as arguments:
    1. n: number of elements in target list
    2. seed: seed for random number generator (optional)
    3. low_bound: lower bound of elements (optional, default=-1000)
    4. high_bound: upper bound of elements (optional, default=1000)
    Raises:
        ValueError: if n < 0 or low_bound > high_bound.
    """
    if n < 0:
        raise ValueError("Size n must be zero or positive")
    if low_bound > high_bound:
        raise ValueError("Lower bound 'low' cannot exceed 'high'")
    rng_generator = random.Random(seed) # Создаем генератор, зависящий от введенного (или none по дефолту) seed
    res = [rng_generator.randint(low_bound, high_bound) for i in range(n)]
    res.sort()
    if n >= 2:
        for i in range(max(1, n // 20)): # Меняем случайные элементы местами (приблизительно 5%)
            j, k = rng_generator.randrange(n), rng_generator.randrange(n)
            res[j], res[k] = res[k], res[j]
    return res


def generate_with_duplicates(n, seed=None, low_bound = -1000, high_bound = 1000, unique_count = 5):
    """Generates a list of n elements with a high number of duplicates.
    Get as arguments:
    1. n: number of elements in target list
    2. seed: seed for random number generator (optional)
    3. low_bound: lower bound of elements (optional, default=-1000)
    4. high_bound: upper bound of elements (optional, default=1000)
    5. unique_count: number of unique elements (optional, default=5)
    Raises:
        ValueError: if n < 0 or low_bound > high_bound, or unique_count < 1.
    """
    if n < 0:
        raise ValueError("Size n must be zero or positive")
    if low_bound > high_bound:
        raise ValueError("Lower bound 'low' cannot exceed 'high'")
    if unique_count < 1:
        raise ValueError("Unique_count must be at least 1")
    if n == 0:
        return []
    rng_generator = random.Random(seed) # Создаем генератор, зависящий от введенного (или none по дефолту) seed
    res = [rng_generator.randint(low_bound, high_bound) for i in range(unique_count)]
    return rng_generator.choices(res, k=n)