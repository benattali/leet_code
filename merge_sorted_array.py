class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        num_one_iter = m - 1
        num_two_iter = n - 1
        insert_index = m + n - 1
        not_done = False

        while num_two_iter >= 0:
            if num_one_iter < 0:
                not_done = True
                break
            if nums1[num_one_iter] > nums2[num_two_iter]:
                nums1[insert_index] = nums1[num_one_iter]
                num_one_iter -= 1
            else:
                nums1[insert_index] = nums2[num_two_iter]
                num_two_iter -= 1
            insert_index -= 1

        if not_done:
            for i in range(num_two_iter + 1):
                nums1[i] = nums2[i]

        return nums1


nums1 = [2, 0]
m = 1
nums2 = [1]
n = 1
print(nums1)
Solution().merge(nums1, m, nums2, n)
print(nums1)
