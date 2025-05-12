print(" Let's Learn Powers of 4!")
print("Here are the powers of 4 from 0 to 10:\n")

# Step 1: Show powers of 2
for i in range(11):
    print(f"4^{i} = {4 ** i}")

# Step 2: Simple quiz
print("\n🧠 Time for a Quick Quiz!")
answer = int(input("What is 4 to the power of 3? "))

if answer == 4 ** 3:
    print("🎉 Correct! 4^3 = 64")
else:
    print(f"❌ Oops! The correct answer if {4 ** 3}")