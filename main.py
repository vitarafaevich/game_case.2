import ru_local as ru
budget = 8000

# day 2
print(ru.phrase2_1)
interactive2_1 = input(ru.phrase2_2)
interactive2_1 = interactive2_1.strip('!?,.:;-_/ ')
if interactive2_1 == 'да' or interactive2_1 == 'yes':
    interactive2_1_1 = input(ru.phrase2_2_1)
    interactive2_1_1 = interactive2_1_1.strip('!?,.:;-_/ ')
    if interactive2_1_1 == '1':
        print(ru.phrase_singly)
    interactive2_1_2 = input(ru.phrase2_2_2)
    interactive2_1_2 = interactive2_1_2.strip('!?,.:;-_/ ')
    if interactive2_1_2 == 'да' or interactive2_1_2 == 'yes':
        print('круто')
    else:
        print(ru.phrase_refusing)