import ru_local as ru
import game
import time
import os
os.startfile(r'C:\Users\polin\Downloads\IMG_0999.JPEG')
budget = 16000
a = input(ru.BEGIN)
print('Day 1')
answer1_1 = input(ru.PHRASE1_1)
if answer1_1.lower() == ru.YES or answer1_1.lower() == 'yes':
    answer1_2 = input(ru.PHRASE1_2)
    if answer1_2.lower() == ru.YES or answer1_2.lower() == 'yes':
        budget = budget - 2500
        print(ru.PHRASE1_3, budget, ru.RUBLES)
        time.sleep(1.0)
        print(ru.PHRASE1_4)
    else:
        print(ru.PHRASE1_4)
        time.sleep(1.5)
    while True:
        answer1_3 = input(ru.PHRASE1_5)
        if answer1_3.lower() == ru.YES or answer1_3.lower() == 'yes':
            answer1_4 = input(ru.PHRASE1_7)
            answer1_4_1 = answer1_4.strip(' ,.;')
            summ = 0
            if '1' in answer1_4_1:
                summ += 200
            if '2' in answer1_4_1:
                summ += 300
            if '3' in answer1_4_1:
                summ += 200
            budget = budget - summ
            print(ru.PHRASE1_3, budget, ru.RUBLES)
            time.sleep(1.0)
            print(ru.PHRASE1_9)
            time.sleep(1.5)
            answer1_5 = input(ru.PHRASE1_8)
            if answer1_5.lower() == ru.YES or answer1_5.lower() == 'yes':
                budget = budget - 300
                print(ru.PHRASE1_3, budget, ru.RUBLES)
                time.sleep(1.0)
                print(ru.PHRASE1_13)
            else:
                print(ru.PHRASE1_10)
                time.sleep(2.0)
                print(ru.PHRASE1_11)
                time.sleep(2.0)
                print(ru.PHRASE1_12)
                time.sleep(2.0)
                budget = budget - 500
                print(ru.PHRASE1_3, budget, ru.RUBLES)
        else:
            print(ru.PHRASE1_6)
            continue
        break
else:
    print(ru.PHRASE1_4)
    time.sleep(1.5)
    while True:
        answer1_3 = input(ru.PHRASE1_5)
        if answer1_3.lower() == ru.YES or answer1_3.lower() == 'yes':
            answer1_4 = input(ru.PHRASE1_7)
            answer1_4_1 = answer1_4.strip(' ,.;')
            summ = 0
            if '1' in answer1_4_1:
                summ += 200
            if '2' in answer1_4_1:
                summ += 300
            if '3' in answer1_4_1:
                summ += 200
            budget = budget - summ
            print(ru.PHRASE1_3, budget, ru.RUBLES)
            time.sleep(1.0)
            print(ru.PHRASE1_9)
            time.sleep(1.5)
            answer1_5 = input(ru.PHRASE1_8)
            if answer1_5.lower() == ru.YES or answer1_5.lower() == 'yes':
                budget = budget - 300
                print(ru.PHRASE1_3, budget, ru.RUBLES)
                time.sleep(1.0)
                print(ru.PHRASE1_13)
            else:
                print(ru.PHRASE1_10)
                time.sleep(2.0)
                print(ru.PHRASE1_11)
                time.sleep(2.0)
                print(ru.PHRASE1_12)
                time.sleep(2.0)
                budget = budget - 500
                print(ru.PHRASE1_3, budget, ru.RUBLES)
        else:
            print(ru.PHRASE1_6)
            continue
        break
time.sleep(1.5)

# day 2
print('Day 2')
time.sleep(1.5)
print(ru.phrase2_1)
interactive2_1 = input(ru.phrase2_2)
interactive2_1 = interactive2_1.strip('!?,.:;-_/ ')
if interactive2_1.lower() == ru.YES or interactive2_1.lower() == 'yes':
    interactive2_1_1 = input(ru.phrase2_2_1)
    interactive2_1_1 = interactive2_1_1.strip('!?,.:;-_/ ')
    if interactive2_1_1 == '1':
        print(ru.phrase_singly)
    interactive2_1_2 = input(ru.phrase2_2_2)
    interactive2_1_2 = interactive2_1_2.strip('!?,.:;-_/ ')
    if interactive2_1_2.lower() == ru.YES or interactive2_1_2.lower() == 'yes':

        while True:
            interactive_couple = input(ru.phrase_mutual_lang)
            interactive_couple = interactive_couple.strip('!?,.:;-_/ ')
            if interactive_couple.lower() == ru.YES or interactive_couple.lower() == 'yes':
                print(ru.phrase_accord)
                time.sleep(2.0)
                print(ru.phrase_cellar)
                time.sleep(2.0)
            else:
                break
        print(ru.phrase_conviction)
        time.sleep(3.0)
        print(ru.phrase_search)
        budget = budget - 1800
        time.sleep(2.0)
        print(ru.PHRASE1_3, budget, ru.RUBLES)
        time.sleep(2.0)
    else:
        print(ru.phrase_refusing)
        time.sleep(2.0)
        print(ru.phrase_search)
        budget = budget - 1800
        time.sleep(2.0)
        print(ru.PHRASE1_3, budget, ru.RUBLES)
        time.sleep(2.0)

else:
    time.sleep(2.0)
    print(ru.phrase_good)
    time.sleep(2.0)
    print(ru.phrase_lada)
    time.sleep(2.0)
    print(ru.phrase_hotel)
    time.sleep(2.0)
    print(ru.phrase_spending)
    time.sleep(2.0)
    budget = budget - 800
    print(ru.PHRASE1_3, budget, ru.RUBLES)
    time.sleep(3.0)

#day 3
print('Day 3')
time.sleep(1.5)
print(ru.DAY3_Q1)
time.sleep(2.5)
budget = budget - 2500
print(ru.PHRASE1_3, budget, ru.RUBLES)
time.sleep(2.0)
b_ = input(ru.DAY3_Q2)
if b_.lower() == ru.NO or b_.lower() == 'no':
    print(ru.DAY3_Q2_NO)
    time.sleep(2.5)
    print('Day 4')
    time.sleep(1.5)
if b_.lower() == ru.YES or b_.lower() == 'yes':
    print(ru.DAY3_Q2_YES_1_1)
    time.sleep(2.0)
    print(ru.PHRASE3_5)
    time.sleep(2.0)
    print(ru.DAY3_Q2_YES_1_2)
    time.sleep(3.0)
    while True:
        answer_q3 = input(ru.DAY3_Q2_YES_1_3)
        if '1' in answer_q3:
            time.sleep(1.5)
            print(ru.DAY3_Q3_1)
            budget1 = budget - 5000
            print(ru.PHRASE1_3, budget1, ru.RUBLES)
            time.sleep(2.0)
            print(ru.PHRASE3_13)
            time.sleep(2.5)
            print(ru.DAY3_Q3_1_2)
            time.sleep(2.5)
            print(ru.DAY3_Q3_1_3)
            time.sleep(2.0)
            print(ru.DAY3_Q3_1_4)
            time.sleep(3.0)
            print(ru.DAY3_Q3_1_5)
            time.sleep(2.0)
        else:
            time.sleep(1.5)
            print(ru.DAY3_Q3_2_1)
            time.sleep(2.0)
            print(ru.DAY3_Q3_2_2)
            if answer1_5.lower() == ru.YES or answer1_5.lower() == 'yes':
                budget = budget - 2500
                print(ru.PHRASE1_3, budget, ru.RUBLES)
                time.sleep(2.0)
                print(ru.DAY3_Q4_1_1)
            if answer1_5.lower() == ru.NO or answer1_5.lower() == 'no':
                budget = budget - 5000
                print(ru.PHRASE1_3, budget, ru.RUBLES)
                time.sleep(2.0)
                print(ru.DAY3_Q5_1_1)
                time.sleep(2.0)
                print(ru.DAY3_Q4_1_2)
                time.sleep(2.0)
            break
    time.sleep(2.0)
    print(ru.DAY3_Q6_1_1)
    time.sleep(1.5)
    print(ru.PHRASE3_23)
    budget = budget - 400
    print(ru.DAY3_Q6_1_3, ru.PHRASE1_3, budget, ru.RUBLES)
    time.sleep(2.0)
    print(ru.DAY3_Q6_1_2)
    time.sleep(2.5)
    print('Day 4')
    time.sleep(1.5)
    print(ru.DAY4_Q1_2)
    time.sleep(2.0)
if b_.lower() == ru.YES or b_.lower() == 'yes':
    time.sleep(2.0)
    print(ru.DAY4_Q1_2_2)
    time.sleep(2.0)
    game.game()
    print(ru.DAY4_CONCLUSION)
    time.sleep(2.0)
    budget = budget + 10000
    print(ru.PHRASE1_3, budget, ru.RUBLES)
    time.sleep(2.0)
    while True:
        k = input(ru.DAY4_RENT)
        if k == '1':
            if budget - 6600 >= 0:
                print(ru.DAY4_CHOISE)
            else :
                print(ru.DAY4_NOMONEY)
                continue
        elif k == '2':
            if budget - 20000 >= 0:
                print(ru.DAY4_CHOISE)
            else:
                print(ru.DAY4_NOMONEY)
                continue
        else:
            if budget - 12000 >= 0:
                print(ru.DAY4_CHOISE)
            else:
                print(ru.DAY4_NOMONEY)
                continue
        break
else:
    if budget<= 5000:
        print(ru.DAY4_Q1_1)
        game.game()
        time.sleep(3.0)
        print(ru.DAY4_CONCLUSION1)
        time.sleep(2.0)
    else:
        print(ru.PHRASE1_3, budget, ru.RUBLES)
        time.sleep(1.5)
        coffee = input(ru.DAY4_PETROL)
        if coffee.lower() == ru.YES or coffee.lower() == 'yes':
            budget = budget - 5300
            print(ru.PHRASE1_3, budget, ru.RUBLES)
        else:
            budget = budget - 5000
            print(ru.PHRASE1_3, budget, ru.RUBLES)
time.sleep(2.0)
print(ru.DAY4_ROAD)



