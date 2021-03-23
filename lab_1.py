import math
import matplotlib.pyplot as mpl
from numpy import NaN

# Запит даних (область визначення функції та крок табуляції)
startInterval = int(input('Початок області визначення функції (ціле число) = '))
endInterval = int(input('Кінець області визначення функції (ціле число) = '))
step = float(input('Крок табуляції = '))

if endInterval <= startInterval:
    print('Вкажіть правильно область визначення функції!')
    SystemExit()

# формування області визначення, враховуючи крок табуляції
x = []
for index in range(0, int((endInterval - startInterval) / step) + 1):
    newValue = startInterval + index * step
    if (newValue % math.pi) < step:
        x.append(NaN)
    x.append(startInterval + index * step)
# Формування значень функції, враховуючи значення, в яких функція не визначена
y = []
for value in x:
    if math.sin(value) != 0:
        yValue = value / math.sin(value)
        y.append(yValue)
    else:
        y.append(NaN)

# обробка значень, коли sin(x) = 0
if startInterval > 0:
    startForPi = int(startInterval / math.pi) + 1
else:
    startForPi = int(startInterval / math.pi)

if endInterval < 0:
    endForPi = int(endInterval / math.pi) - 1
else:
    endForPi = int(endInterval / math.pi)

# формування масиву значень, коли sin(x) = 0
exceptions = []
for index in range(startForPi, endForPi + 1):
    exceptions.append(math.pi * index)

print(exceptions, '- значення, на яких функція не є визначеною')

# визначення і побудова графіка
mpl.grid()
mpl.plot(x, y)
mpl.show()
