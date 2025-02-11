import heapq

class Solution:
    def maxScore(self, nums1, nums2, k):
        n = len(nums1)
        pairs = [(nums1[i], nums2[i]) for i in range(n)]
        pairs.sort(key=lambda x: x[1], reverse=True)
        heap = []
        sum_nums1 = 0
        for i in range(k):
            sum_nums1 += pairs[i][0]
            heapq.heappush(heap, pairs[i][0])
        min_nums2 = pairs[k-1][1]
        max_score = sum_nums1 * min_nums2
        for i in range(k, n):
            sum_nums1 += pairs[i][0] - heap[0]
            heapq.heappop(heap)
            heapq.heappush(heap, pairs[i][0])
            min_nums2 = min(min_nums2, pairs[i][1])
            max_score = max(max_score, sum_nums1 * min_nums2)
        return max_score
