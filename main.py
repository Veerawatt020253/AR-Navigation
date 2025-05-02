# รับจำนวนคู่
n = int(input())

# รับตัวเลขทั้งหมดในรูปแบบ list
nums = list(map(int, input().split()))

# สร้างรายการเก็บตัวเลขที่มากกว่าของแต่ละคู่
greater_nums = []

# วนลูปผ่านแต่ละคู่
for i in range(0, 2 * n, 2):
    a = nums[i]
    b = nums[i + 1]
    greater_nums.append(max(a, b))

# สร้างสมการผลรวม
expression = ' + '.join(map(str, greater_nums))
total = sum(greater_nums)

# แสดงผลลัพธ์
print(f"{expression} = {total}")