#!/bin/bash

# Check if a number is given as a command-line argument
if [[ -n $1 ]]; then
  # Use the provided argument as the next number
  next_number=$1
else
  # Find the directory with the highest number in the format ABC{number}
  max_number=0

  for dir in ABC*/; do
    # Extract the number after "ABC" in the directory name
    number=${dir#ABC}
    number=${number%/}
    
    # Update max_number if current number is greater
    if [[ $number -gt $max_number ]]; then
      max_number=$number
    fi
  done

  # Increment max_number by 1
  next_number=$((max_number + 1))
fi

num=$next_number

# Define the directory name
dirname="ABC${num}"

# Check if the directory already exists
if [ -d "$dirname" ]; then
  echo "Directory ${dirname} already exists. Aborting."
  exit 1
fi

# Create the directory
mkdir -p $dirname

# Generate the content for each file
echo "# https://atcoder.jp/contests/abc${num}/tasks/abc${num}_a

n, m = list(map(int, input().split()))
a = int(input())
" > "${dirname}/a.py"

echo "# https://atcoder.jp/contests/abc${num}/tasks/abc${num}_b

n, m = list(map(int, input().split()))
a = int(input())
" > "${dirname}/b.py"

echo "# https://atcoder.jp/contests/abc${num}/tasks/abc${num}_c

n, m = list(map(int, input().split()))
a = int(input())
" > "${dirname}/c.py"

# Output the result
echo "Directory ${dirname} has been created with a.py, b.py, and c.py."
