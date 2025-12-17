n = int(input())
s = input()
count = 0
i = 0
while i < n - 1:
    if s[i] == s[i+1]:
        length = 1
        while i + 1 < n and s[i] == s[i+1]:
            i += 1
            length += 1
        count += length // 2
    i += 1
print(count)
