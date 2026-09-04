class Solution:
    def floodFill(self, image, sr, sc, color):
        old_color = image[sr][sc]

        if old_color == color:
            return image

        rows = len(image)
        cols = len(image[0])

        def dfs(r, c):
            # Outside the image
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return

            # Only fill pixels having the original color
            if image[r][c] != old_color:
                return

            # Change the color
            image[r][c] = color

            # Visit four neighboring pixels
            dfs(r + 1, c)  # down
            dfs(r - 1, c)  # up
            dfs(r, c + 1)  # right
            dfs(r, c - 1)  # left

        dfs(sr, sc)

        return image