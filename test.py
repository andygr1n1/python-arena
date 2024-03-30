def removeDuplicates(nums: list[int]) -> int:

        c = 1
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[c] = nums[i]
                c += 1
        print(nums)
        return c

        
removeDuplicates([1, 1, 2, 2, 3, 4, 5, 5])                

        