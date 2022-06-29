def solution(numbers, hand):
    answer = ''
    keyPad = {
        '1': (0, 0),
        '2': (0, 1),
        '3': (0, 2),
        '4': (1, 0),
        '5': (1, 1),
        '6': (1, 2),
        '7': (2, 0),
        '8': (2, 1),
        '9': (2, 2),
        '*': (3, 0),
        '0': (3, 1),
        '#': (3, 2),
    }
    right = (3, 0)
    left = (3, 2)
    for num in numbers:
        idx = f'{num}'
        if num % 3 == 1:
            answer += 'L'
            left = keyPad[idx]
        elif num % 3 == 0 and num != 0:
            answer += 'R'
            right = keyPad[idx]
        else:
            dist_left = abs(keyPad[idx][0] - left[0]) + abs(keyPad[idx][1] - left[1])
            dist_right = abs(keyPad[idx][0] - right[0]) + abs(keyPad[idx][1] - right[1])
            print(f'{num}, {dist_left}, {dist_right}')

            if dist_left > dist_right:
                answer += 'R'
                right = keyPad[idx]
            elif dist_left < dist_right:
                answer += 'L'
                left = keyPad[idx]
            elif dist_left == dist_right:
                if hand == 'left':
                    answer += 'L'
                    left = keyPad[idx]
                else:
                    answer += 'R'
                    right = keyPad[idx]

    return answer

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
hand = "right"
print(solution(numbers, hand))