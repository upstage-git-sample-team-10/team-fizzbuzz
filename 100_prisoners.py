from random import shuffle

def find_num():
    # 죄수 번호가 들어갈 박스
    boxes = {}

    # 죄수 번호(1-100)를 셔플
    nums = [i for i in range(1, 101)]
    shuffle(nums)

    # 앞 죄수가 열어본 박스
    visited = set()

    # 셔플된 죄수 변호를 하나씩 뽑아 박스에 할당
    for i, num in enumerate(nums):
        boxes[i+1] = num

    # 각 죄수가 방에 들어가 자신의 번호가 매겨진 박스부터 열어봄
    for prisonor in range(1, 101):

        if prisonor in visited:
            continue
        open_num = prisonor
        for _ in range(50):
            visited.add(open_num)
            open_num = boxes[open_num]
            if open_num == prisonor:
                #print(i, '번호를 찾았다')
                break
            else:
                #print(i, '번호를 못 찾았다')
                return 0
    return 1

success = 0
for _ in range(10000):
    success += find_num()

print(success / 10000)

