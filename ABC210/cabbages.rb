n, a, x, y = gets.split(" ").map(&:to_i)
payment = 0
n.times do |i|
  payment += i+1 > a ? y : x
end
puts payment