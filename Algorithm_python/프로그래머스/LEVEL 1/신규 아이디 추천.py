def solution(new_id):
    answer = ''
    new_id = new_id.lower()

    for ch in new_id:
        if ch.isalpha() or ch.isdigit() or ch in ['-', '_', '.']:
            answer += ch

    while '..' in answer:
        answer = answer.replace('..', '.')

    if len(answer) > 0:
        while len(answer) > 0 and (answer[0] == '.' or answer[-1] == '.'):
            answer = answer.strip('.')

    if answer == '':
        answer = 'a'

    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[0:-1]

    while len(answer) < 3:
        answer += answer[-1]

    return answer