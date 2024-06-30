n = int(input())
a = list(map(int, input().split()))
w = list(map(int, input().split()))

box_id_to_item_amount = [0] * n
for box_id in a:
    box_id_to_item_amount[box_id - 1] += 1
empty_cnt = box_id_to_item_amount.count(0)

w_box_id = {}
for i in range(len(w)):
    w_box_id[w[i]] = a[i] - 1
print(w_box_id)
sorted_w = sorted(w)
print(sorted_w)

total = 0

for sw in sorted_w:
    if box_id_to_item_amount[w_box_id[sw]] >= 2:
        print(sw)
        total += sw
        empty_cnt -= 1
        box_id_to_item_amount[w_box_id[sw]] -= 1
    if empty_cnt == 0:
        print(total)
        exit()
