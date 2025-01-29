# Type conversion
# 1) implicit conversion-automatic
# 2) Explicit conversion-forcefully user-defined

print("implicit conversion")
a = 56
b = 4.3 * a
print(b,type(b)) # auto resilt in float
print(b/45, type(b)) # 5.351111111111111 auto resilt in float

print("Explicit conversion")
a = 56
b = int(4.3) * a # result 4*a
print(b,type(b)) # int
print(int(a/45)) # 1 as int

n = 15