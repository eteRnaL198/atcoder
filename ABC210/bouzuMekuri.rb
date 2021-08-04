n, s = $stdin.readlines(chomp: true).map{|l| l.split("").map(&:to_i)}
i = 0;
while s[i] != 1 do
  i += 1
end
looser = i % 2 === 0 ? "Takahashi" : "Aoki"
puts looser