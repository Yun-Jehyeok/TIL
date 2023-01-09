# 실버 5
# 삭제에 remove가 아닌 discard가 사용되었다.
# 계속 런타임 에러가 뜨길래 찾아보니 remove는 없는 값을 삭제하려 하면 에러가 나온다고 한다.
import sys

N = int(sys.stdin.readline())

set_data = set()

for _ in range(N):
    str_data = sys.stdin.readline().strip().split(' ')
    method = str_data[0]

    if len(str_data) == 2:
        data = int(str_data[1])

    if method == 'add':
        set_data.add(data)
    elif method == 'remove':
        set_data.discard(data)
    elif method == 'check':
        if data in set_data:
            print('1')
        else:
            print('0')
    elif method == 'toggle':
        if data in set_data:
            set_data.discard(data)
        else:
            set_data.add(data)
    elif method == 'all':
        new_list = [x for x in range(1, 21)]
        set_data = set(new_list)
    else:
        set_data = set()
    