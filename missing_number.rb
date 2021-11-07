# @param {Integer[]} nums
# @return {Integer}
def missing_number(nums)
  nums_length = nums.length
  all_nums_in_range = {}

  nums.each do |num|
    all_nums_in_range[num] = true
  end

  (nums_length + 1).times do |i|
    return i unless all_nums_in_range[i]
  end
end
