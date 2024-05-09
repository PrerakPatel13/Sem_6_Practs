import random 
candidates = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Candidates: ", candidates)
interviewed = []
hired = []
for candidate in candidates:
    interviewed.append(candidate)
    if not hired or candidate > max(hired):
        hired.append(candidate)
firing_cost = len(hired) - 1  
print("Normal way : ")
print("Interviewed candidates:", interviewed)
print("Hired candidates:", hired)
print("Number of candidates hired:", len(hired))
print("Firing cost:", firing_cost)

candidates = [0,1,2,3,4,5,6,7,8,9,10]
print(f"CANDIDATES: {candidates}")
interviewed = []
hired = []

for i in range(len(candidates)):
    temp  = random.choice(candidates)
    interviewed.append(temp)
    candidates.remove(temp)

max = -1
for i in interviewed:
    if i>max:
        hired.append(i)
        max = i

print(f"RANDOMISED INTERVIEW ORDER OF CANDIDATES: {interviewed}")
print(f"CANDIDATES HIRED: {hired}")
print(f"HIRING COST: {len(hired)}")
print(f"FIRING COST: {len(hired)-1}")