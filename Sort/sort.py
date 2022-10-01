
# 버블정렬은 인접한 두 원소를 검사하여 정렬
# 시간복잡도는 (O^2)

test = [3,10,8,22,2,1]

def BubbleSort(arr):
    print("BubbleSort : ")
    result = arr
    for i in range(len(result) - 1):
        for j in range(len(result) - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
                print(result)
    return print(result)

# 선택정렬은 전체 데이터에서 매번 가장 작은(큰) 데이터를 선택하여
# 0번(마지막) 인덱스와 위치를 변경하는 과정을 반복함.
# 시간복잡도는 버블소트와 동일함

def SelectionSort(arr):
    print("SelectionSort_maxIdx : ")
    result = arr
    for i in range(len(result)):
        max_idx = 0
        for j in range(len(result) - i):
            if (result[max_idx] < result[j]):
                max_idx = j
        result[j], result[max_idx] = result[max_idx], result[j]
        print(result)
    return print(result)

def SelectionSort_min(arr):
    print("SelectionSort_minIdx : ")
    result = arr
    for i in range(len(result)):
        min_idx = i
        for j in range(i + 1, len(result)):
            if (result[min_idx] > result[j]):
                min_idx = j
        result[i], result[min_idx] = result[min_idx], result[i]
        print(result)
    return print(result)
    
BubbleSort(test)
SelectionSort(test)
SelectionSort_min(test)