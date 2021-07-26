line = gets
line_o_idxs = (line.split("")).each_index.select{|idx| line[idx] == "o"}
line_x_idxs = (line.split("")).each_index.select{|idx| line[idx] == "x"}
if line_o_idxs.length > 4
  puts 0
else
  count = 0
  10000.times do |num|
    target = "xxxxxxxxxx"
    (num.to_s).split("").each do |idx|
      target[(idx.to_i)] = "o"
    end

    flag = true
    line_o_idxs.each do |idx|
      if line[idx] != target[idx]
        flag = false
      end
    end
    line_x_idxs.each do |idx|
      if line[idx] != target[idx]
        flag = false
      end
    end
    count = flag ? count+1 : count

  end
  puts count
end