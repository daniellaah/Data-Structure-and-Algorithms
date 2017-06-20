'''Smallest Rectangle Enclosing Black Pixels
An image is represented by a binary matrix with 0 as a white pixel and 1 as a black pixel.
The black pixels are connected, i.e., there is only one black region.
Pixels are connected horizontally and vertically.
Given the location (x, y) of one of the black pixels,
return the area of the smallest (axis-aligned) rectangle that encloses all black pixels.
Example
For example, given the following image:

[
  "0010",
  "0110",
  "0100"
]
and x = 0, y = 2,
Return 6.
'''
class Solution(object):
    # @param image {List[List[str]]}  a binary matrix with '0' and '1'
    # @param x, y {int} the location of one of the black pixels
    # @return an integer
    def hasBlackPixel(self, index, image, axis=0):
        if axis == 0:
            for pixel in image[index]:
                if pixel == '1':
                    return True
            return False
        if axis == 1:
            for i in range(len(image)):
                if image[i][index] == '1':
                    return True
            return False

    def minArea(self, image, x, y):
        # Write your code here
        row, col = len(image), len(image[0])
        left = upper = bottom = right = 0

        # find left
        start, end = 0, col - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if self.hasBlackPixel(mid, image, 1):
                end = mid
            elif y < mid:
                end = mid
            else:
                start = mid
        if self.hasBlackPixel(start, image, 1):
            left = start
        elif self.hasBlackPixel(end, image, 1):
            left = end

        # find right
        start, end = 0, col - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if self.hasBlackPixel(mid, image, 1):
                start = mid
            elif y < mid:
                end = mid
            else:
                start = mid
        if self.hasBlackPixel(end, image, 1):
            right = end
        elif self.hasBlackPixel(start, image, 1):
            right = start

        # find upper
        start, end = 0, row - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if self.hasBlackPixel(mid, image, 0):
                end = mid
            elif x < mid:
                end = mid
            else:
                start = mid
        if self.hasBlackPixel(start, image, 0):
            upper = start
        elif self.hasBlackPixel(end, image, 0):
            upper = end

        # find bottom
        start, end = 0, row - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if self.hasBlackPixel(mid, image, 0):
                start = mid
            elif x < mid:
                end = mid
            else:
                start = mid
        if self.hasBlackPixel(end, image, 0):
            bottom = end
        elif self.hasBlackPixel(start, image, 0):
            bottom = start

        return (right - left + 1) * (bottom - upper + 1)
