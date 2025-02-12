from pkg import mod

print(mod._is_leap(4))
if len(mod.argv[1:])==0:
    mod.testprint('Вызов функции из пакета')
else:
    mod.testprint(' '.join(mod.argv[1:]))