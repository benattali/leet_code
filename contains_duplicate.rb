# @param {Integer[]} nums
# @return {Boolean}
def contains_duplicate(nums)
  nums_occurences = {}

  nums.each do |num|
    return true if nums_occurences[num]

    nums_occurences[num] = 1
  end
  false
end

nums = [-1, 0, -1]
puts contains_duplicate(nums)
