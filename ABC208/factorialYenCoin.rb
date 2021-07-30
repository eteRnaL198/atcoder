price = gets.to_i

def calcFact(n)
  return n <= 1 ? 1 : n * calcFact(n-1)
end

count = 0
10.times do |i|
  fact = calcFact(10-i)
  while price - fact >= 0
    price -= fact
    count += 1
  end
end

puts count