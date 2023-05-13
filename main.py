import ru_local as ru
import time
budget = 8000
a = input(ru.BEGIN)
print('Day 1')
answer1_1 = input(ru.PHRASE1_1)
if answer1_1.lower() == 'da' or answer1_1.lower() == 'yes':
    answer1_2 = input(ru.PHRASE1_2)
    if answer1_2.lower() == 'da' or answer1_2.lower() == 'yes':
        budget = budget - 2500
        print(ru.PHRASE1_3, budget, ru.RUBLES)
        time.sleep(1.0)
        print(ru.PHRASE1_4)
    else:
        print(ru.PHRASE1_4)
        time.sleep(1.5)
    answer1_3 = input(ru.PHRASE1_5)
    if answer1_3.lower() == 'da' or answer1_3.lower() == 'yes':
        answer1_4 = input(ru.PHRASE1_7)
        answer1_4_1 = answer1_4.strip(' ,.;')
        if answer1_4_1 == '1' or answer1_4_1 == '3':
            budget = budget - 200
            print(ru.PHRASE1_3, budget, ru.RUBLES)
        elif answer1_4_1 == '2':
            budget = budget - 300
            print(ru.PHRASE1_3, budget, ru.RUBLES)
        elif answer1_4_1 in ['12', '21', '23', '32']:
            budget = budget - 500
            print(ru.PHRASE1_3, budget, ru.RUBLES)
        elif answer1_4_1 in ['13','31']:
            budget = budget - 400
            print(ru.PHRASE1_3, budget, ru.RUBLES)
        else:
            budget = budget - 700
            print(ru.PHRASE1_3, budget, ru.RUBLES)
        time.sleep(1.0)
        print(ru.PHRASE1_9)
        time.sleep(1.5)
        answer1_5 = input(ru.PHRASE1_8)
        if answer1_5.lower() == 'da' or answer1_5.lower() == 'yes':
            budget = budget - 300
            print(ru.PHRASE1_3, budget, ru.RUBLES)
            time.sleep(1.0)
            print(ru.PHRASE1_13)
        else:
            a = input(ru.PHRASE1_10)
            time.sleep(1.0)
            b = input(ru.PHRASE1_11)
            time.sleep(1.0)
            c = input(ru.PHRASE1_12)
            budget = budget - 500
            print(ru.PHRASE1_3, budget, ru.RUBLES)
    else:
        while True:
            print(ru.PHRASE1_6)
            try:
                answer1_3 = input(ru.PHRASE1_5)
                if answer1_3.lower() == 'da' or answer1_3.lower() == 'yes':
                    break
            except:
                break
else:
    print()
time.sleep(1.5)
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
        print(ru.phrase_search)