line, candies = $stdin.readlines(chomp: true).map{|l| l.split(" ").map(&:to_i)}
n = line[0]
k = line[1]

def addKinds(k, n)
  if k[n]
    k[n] += 1
  else
    k[n] = 1
  end
end

kinds = {}
k.times do |idx|
  addKinds(kinds, candies[idx])
end

max = 0
kinds.each{ |key, val| 
  max += val > 0 ? 1 : 0
}

i = 0
while i < n-k
  kinds[candies[i]] -= 1
  tempMax = kinds[candies[i]] === 0 ? max-1 : max
  tempMax += (kinds[candies[i+k]] === nil || kinds[candies[i+k]] === 0) ? 1 : 0
  addKinds(kinds, candies[i+k])
  max = tempMax > max ? tempMax : max
  i += 1
end

puts max