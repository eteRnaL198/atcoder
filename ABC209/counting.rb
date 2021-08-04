a, b = gets.split(" ").map(&:to_i)
count = b - a + 1
puts count > 0 ? count : 0