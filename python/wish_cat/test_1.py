import random


def get_team_numbers(members):
    """
    최대한 적은 수의 조가 편성되도로 조별 인원 산출 함수
    7로 나눈 나머지가 5보다 작을 때에 한하여 조별 인원을 1명~2명씩 차감하는 식으로 계산
    """
    member_len = len(members)
    if member_len % 7 == 0:
        team_number = [7] * (member_len//7)
        return team_number
    elif member_len % 7 >= 5:
        team_number = [7] * (member_len//7)
        team_number.append(member_len % 7)
        return team_number
    elif member_len % 7 < 5:
        team_number = [7] * (member_len//7)
        team_number.append(member_len % 7)
        index=0
        while team_number[-1] < 5 :
            if team_number[index] == 5 :
                index += 1
            team_number[index] -= 1
            team_number[-1] += 1
        return team_number


def mix_member(members):

    team_numbers = get_team_numbers(members)
    output = {}
    for i in range(len(team_numbers)) :
        member_list = []
        for j in range(team_numbers[i]) :
            member_list.append(members.pop(random.randint(0, len(members)-1)))
        output[f'{i+1}조'] = member_list
    return output


members = [i for i in range(100)]
output = mix_member(members)
print(output)
