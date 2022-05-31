import random

y = random.sample(range(1, 21), 3)


is_right = 0

while is_right==0:
    ans = input('숫자를 입력하세요.(구분자:,) ')
    ans = ans.split(',')
    ans = [int(a) for a in ans]
    print('입력한 숫자:', ans)

    s = 0;b = 0

    if y == ans:
        print('3 스트파이크, 0 볼')
        print('정답:', y)
        is_right = 1
    else:
        for a in ans:
            if a in y:
                if y.index(a) == ans.index(a):
                    s = s + 1
                elif y.index(a) != ans.index(a):
                    b = b + 1

        print(f'{s} 스트라이크, {b} 볼')