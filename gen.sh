#!/bin/bash

# Check if an argument is provided
if [ -z "$1" ]; then
  echo "Please provide a number as an argument."
  exit 1
fi

# Get the number from the argument
num=$1

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
