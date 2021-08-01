lines = $stdin.readlines(chomp: true).map{|line| line.split(" ").map(&:to_i)}
citizens_total = lines[0][0]
snack_total = lines[0][1]
citizens = Hash.new
lines[0][0].times do |i|
  citizens.store(lines[1][i], snack_total/citizens_total)
end

residue = snack_total % citizens_total
sortedCitizenNums = lines[1].sort

residue.times do |i|
  citizens[sortedCitizenNums[i]] += 1
end

citizens.each{|key, val|
  puts val
}