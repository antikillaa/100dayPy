count_total = 0

for count in range(2, 101, 2):
    count_total += count

print(count_total)

count_total2 = 0

for count in range(1, 101):
    if count % 2 == 0:
        count_total2 += count

print(count_total2)

