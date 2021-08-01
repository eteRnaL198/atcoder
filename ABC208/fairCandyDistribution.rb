lines = $stdin.readlines(chomp: true).map{|line| line.split(" ").map(&:to_i)}
citizens_total = lines[0][0]
snack_total = lines[0][1]
citizens = []

lines[0][0].times do |i|
  hash = Hash.new
  hash.store(:citizen_num, lines[1][i])
  hash.store(:snack, snack_total/citizens_total)
  citizens.push(hash)
end

residue = snack_total % citizens_total
sortedCitizenNums = lines[1].sort

residue.times do |i|
  # citizens中のcitizen_numがsortedCitizenNums[i]である要素のsnackをインクリメントする
  a = citizens.select do |citizen|
    citizen[:citizen_num] === sortedCitizenNums[i]
  end
  a[:snack] += 1
end

for citizen in citizens do
  print citizen[:citizen_num], " ", citizen[:snack]
  puts ""
end

# { 8 => 3, 1 => 4} でいいかも