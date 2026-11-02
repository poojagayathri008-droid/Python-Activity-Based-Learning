p = ["good", "excellent", "happy"]
n = ["bad", "poor", "worst"]

f = input("Enter feedback: ").lower()
score = 0

for w in p:
    if w in f:
        score += 1

for w in n:
    if w in f:
        score -= 1

print("Score:", score)

if score > 0:
    print("Positive Feedback")
elif score < 0:
    print("Negative Feedback")
else:
    print("Neutral Feedback")

