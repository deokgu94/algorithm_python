def solution(food_times, k):
#     if sum(food_times) <= k:
#         return -1
    
#     num = len(food_times)
#     _count = 0
#     while _count <= k:
#         if food_times[_count % num] != 0:
#             food_times[_count % num] -= 1
#         _count += 1

#     return (_count % num) +1 if max(food_times) > 0 else -1
    while True:
        # 초과 return 
        if sum(food_times) <= k:
            return -1
        
        min_num = min(food_times)
        for x in range(food_times):
            food_time[x] -= min_num
            
        for x in range(food_time):
            
            