array = [4, 3, 6, 7, 8, 3, 4, 5, 3, 4, 1]

# 배열을 2차원 배열로 변환하는 함수
def make_2d_array(arr, size):
    result = []  # 빈 2차원 배열 생성
    for i in range(0, len(arr), size):
        result.append(arr[i:i+size])  # 배열의 일부분을 잘라서 2차원 배열에 추가
    return result

# 2차원 배열 만들기
two_d_array = make_2d_array(array, 3)

# 결과 출력
print(two_d_array)
