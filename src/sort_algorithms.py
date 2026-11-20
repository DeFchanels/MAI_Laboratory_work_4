def selection_sort(li):
    if not (isinstance(li, (list, tuple))): # Проверка корректного типа введенного аргумента
        raise TypeError('Argument must be a list or tuple')
    res = list(li) # Копируем данные для сортировки
    n = len(res)
    for j in range(n - 1):
        min_index = j # Для начала считаем, что первый элемент неотсортированной части - минимален
        for i in range(j + 1, n): # Проходим по неотсортированной части (без первого элемента, проверять его незачем)
            if res[i] < res[min_index]: # Нашли новый минимум
                min_index = i
        res[j], res[min_index] = res[min_index], res[j]
    return res


def heapify(li, heap_size, i):
    largest = i # Сам элемент
    left = 2 * i + 1 # Левый ребенок
    right = 2 * i + 2 # Правый ребенок
    if left < heap_size and li[left] > li[largest]: # Если существует левый потомок и он больше родителя, меняем максимальный элемент
            largest = left
    if right < heap_size and li[right] > li[largest]: # Если существует правый потомок и он больше родителя, меняем максимальный элемент
            largest = right
    if largest != i: # Если родитель не максимальный, то меняем местами с максимумом, и просеиваем дальше вниз
        li[i], li[largest] = li[largest], li[i]
        heapify(li, heap_size, largest) # Запускаем просеивание для бывшего родителя, опустившегося вниз


def heap_sort(li):
    if not (isinstance(li, (list, tuple))): # Проверка корректного типа введенного аргумента
        raise TypeError('Argument must be a list or tuple')
    res = list(li)
    heap_len = len(res)
    for i in range(heap_len // 2 - 1, -1, -1): # Проходим по всем элементам, у которых есть потомки
        heapify(res, heap_len, i) # Просеиваем
    for i in range(heap_len - 1, 0, -1):
        res[0], res[i] = res[i], res[0] # Меняем местами верхушку дерева и последний элемент (из-за цикла он после не рассматривается, куча уменьшается)
        heapify(res, i, 0)
    return res

