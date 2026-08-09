class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre_prod = []
        suf_prod = []
        ans_prod = []
        
        curr_prod = 1
        j=0
        for i, num in enumerate(nums):
            if j<i:
                curr_prod *= nums[j]
                j+=1
            if j==i:
                pre_prod.append(curr_prod)

        curr_prod = 1
        j=0
        reversed_nums = list(reversed(nums))
        for i, num in enumerate(reversed_nums):
            if j<i:
                curr_prod *= reversed_nums[j]
                j+=1
            if j==i:
                suf_prod.append(curr_prod)
        
        suf_prod.reverse()
        for i in range(len(nums)):
            ans_prod.append(pre_prod[i] * suf_prod[i])

        return ans_prod