class Solution(object):
    def generate(self, numRows):
        result = []

        for i in range(numRows):
            row = [1]

            if i > 0:
                previous = result[i - 1]

                for j in range(1, i):
                    row.append(previous[j - 1] + previous[j])

                row.append(1)

            result.append(row)

        return result