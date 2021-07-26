input = gets.split(" ")
reverse_nums = input.map do |char|
  total = 7
  total - char.to_i
end
puts reverse_nums.sum()