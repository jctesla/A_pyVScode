def save(x: "starting capital",
         y: "annual return (e.g., 0.1 == 10%)",
         n: "number of years"):
   return x * (1+y)**n

# Investing $10,000 at 10% for 50 years
print(save(10000, 0.1, 50))
# 1173908.5287969578
# = $1.1 million USD

print(save.__annotations__)                   # {'x': 'starting capital', 'y': 'annual return (e.g., 0.1 == 10%)', 'n': 'number of years'}