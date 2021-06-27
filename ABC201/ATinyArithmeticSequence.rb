lines = gets.split(" ")
num_lines = lines.map do |char|
  char.to_i
end
asc_lines = num_lines.sort
if asc_lines[2] - asc_lines[1] == asc_lines[1] - asc_lines[0]
  puts "Yes"
else
  puts "No"
end