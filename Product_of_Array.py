# Title: Product of Array Except Self (Leetcode)
# Difficulty: Medium
# Problem: https://leetcode.com/problems/product-of-array-except-self/description/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # count the number of zeroes
        number_of_zeroes = nums.count(0)

        # if there are no zeroes
        if number_of_zeroes == 0:
        # find the product
            product = 1
            for i in nums:
                product *= i
            for i in range(len(nums)):
                # product of all elements except the ith element
                nums[i] = product//nums[i]
            return nums # return the array

        # if there is only one zero then there will be just one non-zero value in the output array
        elif number_of_zeroes == 1:
            # find the product of all elements except the one zero elements
            product = 1
            for i in nums:
                if i != 0:
                    product *= i
            index = nums.index(0)
            nums = [0 for i in range(len(nums))] # create an array of zeroes
            nums[index] = product # put the product of all other elements at the index of 0 element
            return nums # return the array of one non-zero element
        else:
            # return an array of all zeroes as every product will have at least one zero
            return [0 for i in range(len(nums))]
