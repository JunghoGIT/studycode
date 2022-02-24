
def make_time_list(time):
    """
    시간 범위를 나타내는 문자열 형태를 비교가 가능하도록 근무가 끝나는 시간의 리스트로서 변환
    """
    for i in range(5):
        if ';' in time[i] :
            time[i] = time[i].replace(':00', '').replace(';', '~').split('~')
            temp = []
            for j in range(int(time[i][0]) + 1, int(time[i][1]) + 1):
                temp.append(j)
            for k in range(int(time[i][2]) + 1, int(time[i][3]) + 1):
                temp.append(k)
            time[i] = temp
        else:
            time[i] = time[i].replace(':00','').split('~')
            temp = []
            for j in range(int(time[i][0]) + 1, int(time[i][1]) + 1):
                temp.append(j)
            time[i] = temp
    return time

def get_count_rank(work_time_count):
    """
    스케줄이 적은 순으로 알바생 순위 리스트를 반환하는 함수

    만약 A를 우선적으로 탐색했을 경우 A가 수요일쯤 최대 근무 가능 시간인 10시간을 넘기게 됨,
    이럴 경우 목, 금에 A가 근무 가능함에도 근무하지 못 하는 경우 발생,
    그러므로 근무 가능한 시간이 여유로운 사람을 우선적으로 탐색함으로서 해당 문제 상황 해결
    """
    min = 10
    rank = []
    for i in range(4):
        if work_time_count[i] <= min :
            min = work_time_count[i]
            rank.insert(0, i)
        else:
            rank.append(i)
    return rank



def make_timetable(a_time, b_time, c_time, d_time):
    a_time = make_time_list(a_time)
    b_time = make_time_list(b_time)
    c_time = make_time_list(c_time)
    d_time = make_time_list(d_time)

    times = [a_time,b_time,c_time,d_time] # 유동적으로 근무가능 시간표를 호출하기 위해서 고차원 리스트 사용

    schedule = [
        [11, 12, 13, 14, 15, 16, 17, 18],
        [11, 12, 13, 14, 15, 16, 17, 18],
        [11, 12, 13, 14, 15, 16, 17, 18],
        [11, 12, 13, 14, 15, 16, 17, 18],
        [11, 12, 13, 14, 15, 16, 17, 18],
    ] # 끝나는 시간을 기준으로 비교하기 위해서 5일치 스케쥴표 생성
    work_time_count = [0,0,0,0] # 10시간 초과근무 카운트
    for i in range(5): # 가능한 근무자가 유일한 시간대에 한하여 우선적으로 시간표 배정
        for j in range(8):
            checker = {
                '근무자후보': '',
                '후보인덱스': 0,
            }
            cnt = 0
            if schedule[i][j] in times[0][i] and work_time_count[0] < 10:
                checker['근무자후보'] = 'A'
                checker['후보인덱스'] = 0
                cnt += 1
            if schedule[i][j] in times[1][i] and work_time_count[1] < 10:
                checker['근무자후보'] = 'B'
                checker['후보인덱스'] = 1
                cnt += 1
            if schedule[i][j] in times[2][i] and work_time_count[2] < 10:
                checker['근무자후보'] = 'C'
                checker['후보인덱스'] = 2
                cnt += 1
            if schedule[i][j] in times[3][i] and work_time_count[3] < 10:
                checker['근무자후보'] = 'D'
                checker['후보인덱스'] = 3
                cnt += 1
            if cnt >= 2:
                continue
            elif cnt == 0:
                schedule[i][j] = 'X'
            else :
                schedule[i][j] = checker['근무자후보']
                work_time_count[checker['후보인덱스']] +=1
    worker_list = ['A','B','C','D']
    for i in range(5): # 스케줄이 적은 순으로 탐색하여 시간표 배정
        for j in range(8):
            rank = get_count_rank(work_time_count)
            if schedule[i][j] in times[rank[0]][i] and work_time_count[0] < 10:
                schedule[i][j] = worker_list[rank[0]]
                work_time_count[rank[0]] += 1
                continue
            if schedule[i][j] in times[rank[1]][i] and work_time_count[1] < 10:
                schedule[i][j] = worker_list[rank[1]]
                work_time_count[rank[1]] += 1
                continue
            if schedule[i][j] in times[rank[2]][i] and work_time_count[2] < 10:
                schedule[i][j] = worker_list[rank[2]]
                work_time_count[rank[2]] += 1
                continue
            if schedule[i][j] in times[rank[3]][i] and work_time_count[3] < 10:
                schedule[i][j] = worker_list[rank[3]]
                work_time_count[rank[3]] += 1
                continue
    return schedule



a_time = ['10:00~14:00', '15:00~18:00', '11:00~13:00;14:00~16:00', '10:00~11:00', '15:00~18:00']
b_time = ['11:00~14:00', '14:00~16:00', '16:00~18:00', '10:00~11:00;12:00~13:00', '14:00~16:00']
c_time = ['14:00~16:00', '16:00~18:00', '10:00~12:00', '12:00~14:00', '14:00~16:00']
d_time = ['14:00~18:00', '10:00~18:00', '12:00~14:00', '14:00~15:00;16:00~17:00', '10:00~12:00']


schedule = make_timetable(a_time, b_time, c_time, d_time)
print('월 :',schedule[0],'\n화 :',schedule[1],'\n수 :',schedule[2],'\n목 :',schedule[3],'\n금 :',schedule[4])




