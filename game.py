import time
GAME_1 = '''Вам будет предложено решить 10 примеров. Чтобы решить задание и ввести ответ дается 15 секунд.
Проигрывая один раз вы завершаете свое участие и не добираетесь до Красноярска :(
'''
GAME_0 = 'Если ответ верный, введите "1", иначе "0"'

print(GAME_1)
print(GAME_0)
ans_1 = input('25*3 > 6*10 + 5')
counter = 0
if time.sleep <= (12) and '1' in ans_1:
    counter += 1
ans_2 = input('436+416=852')
if time.sleep <= (12) and '1' in ans_2:
    counter += 1
ans_3 = input('')
else:
    print('Game over :(')

ans_3 = '45*13 = 586'
ans_5 = 'x^2 - 144 = 0 при x = 12'
ans_6 = 'lg 100 = 10'
ans_7 = ''
