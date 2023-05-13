import ru_local as ru
budget = 8000

# day 2
print(ru.phrase2_1)
interactive2_1 = input(ru.phrase2_2)
interactive2_1.strip('!?,.:;-_/ ')
if interactive2_1 == 'да' or interactive2_1 == 'yes':
    print('a')