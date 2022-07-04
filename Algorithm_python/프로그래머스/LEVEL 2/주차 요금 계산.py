import math


def solution(fees, records):
    answer = []
    number_fee = dict()
    number_intime = dict()
    number_staytime = dict()
    basic_fee_time, basic_fee, additional_fee_time, additional_fee = fees
    for record in records:
        record = record.replace(':', ' ')
        record_list = record.split()
        hour = int(record_list[0])
        minute = int(record_list[1])
        number = int(record_list[2])
        in_or_out = record_list[3]

        if number not in number_fee:
            number_fee[number] = 0
        if number not in number_intime:
            number_intime[number] = 0
        if number not in number_staytime:
            number_staytime[number] = 0

        if in_or_out == 'IN':
            number_intime[number] = hour * 60 + minute
        elif in_or_out == 'OUT':
            number_staytime[number] = hour * 60 + minute - number_intime[number]
            del (number_intime[number])

    for (number, intime) in number_intime.items():
        number_staytime[number] += 23 * 60 + 59 - intime

    for (number, staytime) in number_staytime.items():
        if staytime > basic_fee_time:
            number_fee[number] += basic_fee + math.ceil(
                (staytime - basic_fee_time) / additional_fee_time) * additional_fee
        else:
            number_fee[number] += basic_fee

    number_fee = sorted(number_fee.items())
    for (key, value) in number_fee:
        answer.append(value)

    return answer

fees = [120, 0, 60, 591]
records = ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]

print(solution(fees, records))