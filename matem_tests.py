print('This is a good game, but also this is test kinda')
questions = ['Kvadrātsakne no 81 = ', '10 2. pakāpe ir = ', '101- 23 = ', '100 * 2 = ', '2x = 120 ; x = ',
             '3y = 60 ; y = ', '4x = 120 ; x = ', '100 : 4 = ', '20 * 4 = ', '22 - 10 = ']
answers = [''] * 10

answers[0] = 9
answers[1] = 100
answers[2] = 78
answers[3] = 200
answers[4] = 60
answers[5] = 20
answers[6] = 30
answers[7] = 25
answers[8] = 80
answers[9] = 12

right = 0
for x in range(10):
    answer = int(input(f'{x + 1}) {questions[x]}'))
    if answer == answers[x]:
        right += 1

print(f'Jūsu atzīme ir {right}')