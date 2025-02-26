# dict comprehension without block and tenerate result in sequence
# Syntax {expression for i in seq_obj if condition}
# ans = {}
# for i in range(1,6):
#     ans.update({i:i*i})
# print(ans)

# ans=[i for i in range(1,6)]
# print(ans)

# ans={i for i in range(1,6)}
# print(ans)

# ans={i:i*i for i in range(1,6)}
# print(ans)

# # WAP to print 5 number table
# reult={i:i*5 for i in range(1,11)}
# print(reult)

products = {"milk":50,"coffee":80,"bread":28}

# Convert all item price IRN to US and show update product data use dict copmprehsnsion
ans = {}
for k,v in products.items():
    ans.update({k:v/87})

print(ans)

print({k:v/87 for k,v in products.items()})

# show only those item whose price is grater than 30
print({k:v for k,v in products.items() if v > 30})

# show only cofee detail
print({k:v for k,v in products.items() if k == "coffee"})
