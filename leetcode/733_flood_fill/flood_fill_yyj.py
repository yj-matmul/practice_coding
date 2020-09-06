class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, new_color: int) -> List[List[int]]:
        update_color = image[sr][sc]
        r_size = len(image)
        c_size = len(image[0])
        stack = [[sr, sc]]
        visited = []

        while stack:
            idx_info = stack.pop()
            r = idx_info[0]
            c = idx_info[1]
            visited.append([r, c])

            if r >= 0 and r < r_size and c >= 0 and c < c_size:
                if image[r][c] == update_color:
                    image[r][c] = new_color
                    if r - 1 >= 0 and [r - 1, c] not in visited: stack.append([r - 1, c])
                    if r + 1 < r_size and [r + 1, c] not in visited: stack.append([r + 1, c])
                    if c - 1 >= 0 and [r, c - 1] not in visited: stack.append([r, c - 1])
                    if c + 1 < c_size and [r, c + 1] not in visited: stack.append([r, c + 1])

        return image