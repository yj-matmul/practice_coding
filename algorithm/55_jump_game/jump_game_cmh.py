def canJump(self, nums):
    """
    :type nums: List[int]
    :rtype: bool
    """

    # defalut 로 True 설정
    answer = True

    try:
        # nums에 0이 하나도 없으면 answer = True
        if 0 not in nums:
            answer = True

        # nums[0] = 0 일때, 전체 길이가 0 이면 True 아니면 False
        elif nums[0] == 0:
            if len(nums) == 1:
                answer = True
            else:
                answer = False

        else:
            # 맨끝값을 버림 (0인경우를 제외하기 위함)
            nums.pop()

            # nums 값 중 0일떄만 수행
            for x in range(len(nums)):

                # nums[x] 가 0 이면
                if nums[x] == 0:
                    # 현재의 index를 check에 저장
                    check = x
                    # 거리변수 1로 설정
                    distance = 1
                    # check - distance 가 -1 일때까지 계속 수행
                    while (check - distance) != -1:
                        # nums[x] 의 뒤에값이 distance 보다 크면 answer = True 작으면 distance 를 1증가 후 answer = False
                        if nums[check - distance] > distance:
                            answer = True
                            break
                        else:
                            distance += 1
                            answer = False
                            # answer 가 false 일 경우 false 이므로 break

                if not answer:
                    break

        # answer 반환
        return answer

    # nums가 빈값일 경우 answer 반환
    except:
        return answer