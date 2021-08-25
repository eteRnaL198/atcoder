s = $stdin.readlines(chomp: true)
isDuplicate = s.count > s.uniq.count ? true : false
puts isDuplicate ? "No" : "Yes"