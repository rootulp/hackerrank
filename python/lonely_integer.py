def lonelyinteger(nums):
    for i in range(len(nums)):
        if nums.count(nums[i]) == 1:
            return nums[i]


if __name__ == '__main__':
    a = input()
    nums = map(int, raw_input().strip().split(" "))
    print(lonelyinteger(nums))
