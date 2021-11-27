# @param {Integer[]} nums
# @return {Integer}
def single_number(nums)
  nums = nums.sort
  something = 0
  checker = nums[0]
  return checker if nums[1] != checker

  nums.drop(1).each do |n|
    if n != checker
      something += 1
      temp = n
    elsif n == checker
      something = 0
      next
    end
    return checker if something == 2

    checker = temp
  end
  nums[-1]
end
