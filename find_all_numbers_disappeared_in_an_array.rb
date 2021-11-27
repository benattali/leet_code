# @param {Integer[]} nums
# @return {Integer[]}
def find_disappeared_numbers(nums)
  appearing_nums = {}
  missing_nums = []

  nums.each do |n|
    appearing_nums[n] = true
  end

  (1..nums.length).each do |i|
    missing_nums << i if !appearing_nums[i]
  end
  missing_nums
end

nums = [1,1]
p find_disappeared_numbers(nums) # [5,6]
