dictionary = {'Table':'Стол', 'Apple':'Яблоко', 'Phone':'Телефон'}
Length = len(dictionary)
print('Длина словаря = ', Length)

reversed = {}
for n, m in dictionary.items():
    reversed[m]=n
Sorted = sorted(list(reversed.keys()))
for i in Sorted:
  print(i,":",reversed[i])
