input = gets.split(' ')
a = input[0].to_i
b = input[1].to_i
if b >= a && b <= 6*a
  puts "Yes"
else
  puts "No"
end