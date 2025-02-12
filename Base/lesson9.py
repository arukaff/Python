data = ["один", "два", "три", "четыре", "пять", "шесть", "семь",
]
a, b, c, *d = data
print(f'{a=} {b=} {c=} {d=}')
a, b, *c, d = data
print(f'{a=} {b=} {c=} {d=}')
a, *b, c, d = data
print(f'{a=} {b=} {c=} {d=}')
*a, b, c, d = data
print(f'{a=} {b=} {c=} {d=}')


link = 'https://docs.python.org/3/faq/programming.html#how-can-i-pass-optional-or-keyword-parameters-from-one-function-to-another'
prefix, *_, suffix = link.split('/')
print(prefix,suffix)


data = [2, 4, 6, 8, 10, ]
for item in data:
    print(item, end='\t')
#И аналогичная операция в одну строку с распаковкой:
data = [2, 4, 6, 8, 10, ]
print(*data, sep='\t')

my_dictcomp = {i: chr(i) for i in range(97, 123)}
print(my_dictcomp) # {97: 'a', 98: 'b', 99: 'c',... }
for number, char in my_dictcomp.items():
    print(f'dict[{number}] = {char}')


def factorial(n):
    number = 1
    for i in range(1, n + 1):
        number *= i
        yield number
for i, num in enumerate(factorial(10), start=1):
    print(f'{i}! = {num}')


def gen(a: int, b: int) -> str:
    if a > b:
        a, b = b, a
    for i in range(a, b + 1):
        yield str(i)
for item in gen(10, 1):
    print(f'{item = }')
