def euclid_gcd(a, b):
  if not isinstance(a, int) or not isinstance(b, int):
    raise TypeError('Arguments must be integers')
  if a == 0 and b == 0:
    raise ValueError('GCD(0,0) is not defined')
  while b:
    a, b = b, a % b
  return abs(a)


def recur_gcd(a, b): # Вспомагательная функция для реализации алгоритма евклида через рекурсию, для того чтобы на каждой итерации заново не проверять типы и равенство 0
  if b == 0:
    return abs(a)
  return recur_gcd(b, a % b)


def euclid_gcd_recur(a, b): # Алгоритм Евклида через рекурсию
  if not isinstance(a, int) or not isinstance(b, int):
    raise TypeError('Arguments must be integers')
  if a == 0 and b == 0:
    raise ValueError('GCD(0,0) is not defined')
  return recur_gcd(a, b)

