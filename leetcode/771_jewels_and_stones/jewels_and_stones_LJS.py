def numJewelsInStones(self, J: str, S: str) -> int:
    # hash key들을 담을 공간을 만들어 줍니다.
    keys = []
    # key에 있냐 없냐를 판단하는 hash func.을 통해 통과되면 buckets에 담아줍니다.
    buckets = 0

    for i in J:
        keys.append(i)

    for j in S:
        if j in keys:
            buckets = buckets + 1

    return buckets