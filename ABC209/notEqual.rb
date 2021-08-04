n, c = $stdin.readlines(chomp: true).map{|l| l.split(" ").map(&:to_i)}
sortedC = c.sort
count = 1
n[0].times do |i|
  count = count * (sortedC[i] - i) % 1000000007
end
puts count 