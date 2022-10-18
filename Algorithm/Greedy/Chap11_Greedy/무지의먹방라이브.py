# 내가 생각한 답
def solution(food_times, k):
    answer = 0
    
    foodIdx = 0
    foodLen = len(food_times)
    
    for i in range(k):
        if food_times[foodIdx] != 0: # 현재 음식이 남아있을 경우
            food_times[foodIdx] -= 1 # 해당 음식에서 1만큼 뺀다
            
            # 다음 음식으로 인덱스 이동
            if foodIdx != foodLen - 1: 
                foodIdx += 1
            else:
                foodIdx = 0
        else: # 현재 음식이 남아있지 않을 경우
            zeroCnt = 0 # 전체 음식중에 0이 몇 개인지 확인
            
            while zeroCnt != foodLen: # 전체 음식이 0이면 종료
                # 현재 음식이 0인 경우
                if food_times[foodIdx] == 0:
                    zeroCnt += 1 # 현재 음식이 0이므로 +1
                
                    # 현재 음식이 0이므로 인덱스 up
                    if foodIdx != foodLen - 1:
                        foodIdx += 1
                    else:
                        foodIdx = 0
                        
                # 현재 음식이 0이 아닌 경우
                else:
                    food_times[foodIdx] -= 1 # 해당 음식에서 1만큼 뺀다
            
                    # 다음 음식으로 인덱스 이동
                    if foodIdx != foodLen - 1: 
                        foodIdx += 1
                    else:
                        foodIdx = 0
                        
                    break
                        
            if zeroCnt == foodLen:
                answer = -1
                break
           
    answer = foodIdx + 1
    
    return answer

# 답
import heapq

def solution(food_times, k):
		# 전체 음식을 먹는 시간보다 k가 크거나 같으면 -1을 출력한다.
		# k가 더 작다면 어떤 음식이든 출력될 것이기에 -1을 출력할 경우의 수는 없어진다.
    if sum(food_times) <= k:
        return -1
    
		# 최소힙을 사용할 변수 지정
    q = []
    for i in range(len(food_times)):
				# heapq는 기본적으로 최소 힙 방식으로 구성된다.
				# q 변수에 (음식 시간, 음식 번호)을 저장한다.
        heapq.heappush(q, (food_times[i], i + 1))
    
		# 먹기 위해 사용한 시간    
    sum_value = 0
		# 직전에 다 먹은 음식 시간
    previous = 0
    # 남은 음식 개수
    length = len(food_times)
    
		# 먹기 위해 사용한 시간 + (현재 음식 시간 - 직전에 다 먹은 음식 시간) * 남은 음식 개수 <= k
    while sum_value + ((q[0][0] - previous) * length) <= k:
				# 최소 힙에서 pop 한 음식의 시간 데이터
        now = heapq.heappop(q)[0]
				# 먹기 위해 사용한 시간 += (현재 값 - 직전에 다 먹은 음식 시간) * 남은 음식 개수
        sum_value += (now - previous) * length
				# 1개 빠졌으니 -1
        length -= 1
				# 이제 빠진게 직전에 다 먹은 음식 시간이 된다.
        previous = now
    
		# 음식 번호 기준으로 정렬    
    result = sorted(q, key = lambda x: x[1])
		# 남은 음식 중 몇 번째 음식인지 확인해 출력
		# (k - sum_value) % length = 위 예시에서... 
		# (15초 - 12초) % 2 = 1
    return result[(k - sum_value) % length][1]