lines = $stdin.readlines(chomp: true).map{|line| line.split(" ").map(&:to_i)}
money = lines[0][1]

lines[0][0].times do |i|
  money -= ((i+1) % 2 != 0) ? lines[1][i] : lines[1][i] - 1
end

puts money >= 0 ? "Yes" : "No"