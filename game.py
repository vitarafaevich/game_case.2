import time
def game():
    GAME_1 = '''Вам будет предложено решить 10 примеров.
Проигрывая один раз, вы завершаете игру и не добираетесь до Красноярска :(
'''
    GAME_0 = 'Если ответ верный, введите "1", иначе "0"'

    ans_1 = '25*3 > 6*10 + 5\n'
    ans_2 = '436 + 416 = 852\n'
    ans_3 = '45*13 = 586\n'
    ans_4 = '''|27 43|
|13 81| = 1528\n'''
    ans_5 = 'x^2 - 144 = 0 при x = 12\n'
    ans_6 = 'lg 100 = 10\n'
    ans_7 = '81/3 + sin(pi/2) = 27\n'
    ans_8 = 'lim (n^2 + n) / n^2 = 1\n'
    ans_9 = 'e^2 > log₂128\n'
    ans_10 = '4! + 6! = 724\n'
    q1, q2, q3, q4, q5, q6, q7, q8, q9, q10 = (1, 1, 0, 0, 1, 0, 0, 1, 1, 0)
    list_answers = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]
    list_questions = [ans_1, ans_2, ans_3, ans_4, ans_5, ans_6, ans_7, ans_8, ans_9, ans_10]
    list_general = zip(list_questions, list_answers)

    list_interactive = []
    while list_interactive != list_answers:
        print(GAME_1)
        time.sleep(2.0)
        print(GAME_0)
        time.sleep(2.0)

        for question, answer in list_general:
            interactive = int(input(question))
            if interactive != answer:
                list_general = zip(list_questions, list_answers)
                list_interactive.clear()
                print('Game over :(')
                time.sleep(2.0)
                break
            else:
                list_interactive.append(interactive)