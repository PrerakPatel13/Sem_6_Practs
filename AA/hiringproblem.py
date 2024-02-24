import random

candidates = [
    (0, 8.5, 2),
    (1, 7.8, 3),
    (2, 9.2, 1),
    (3, 7.0, 4),
    (4, 8.0, 2),
    (5, 8.7, 3),
    (6, 9.0, 2),
    (7, 7.5, 4),
    (8, 8.3, 1),
    (9, 9.5, 3),
]

roles = {
    0: 'analyst',
    1: 'sales',
    2: 'analyst',
    3: 'developer',
    4: 'analyst',
    5: 'sales',
    6: 'analyst',
    7: 'developer',
    8: 'analyst',
    9: 'sales',
}

cgpa_weightage = 0.5
experience_weightage = 0.4
rank_weightage = 0.3

interviewed_candidates = []
hired_candidates = []

candidates_copy = candidates.copy()

for i in range(len(candidates)):
    selected_candidate = random.choice(candidates_copy)
    interviewed_candidates.append(selected_candidate + (roles[i],))
    candidates_copy.remove(selected_candidate)

num_to_hire = random.randint(1, len(interviewed_candidates))

interviewed_candidates_copy = interviewed_candidates.copy()

for _ in range(num_to_hire):
    max_score = -1
    best_candidate = None

    for candidate in interviewed_candidates_copy:
        _, cgpa, experience, role = candidate
        score = (rank_weightage * random.random()) + (experience_weightage * experience) + (cgpa_weightage * cgpa)
        
        if score > max_score:
            max_score = score
            best_candidate = candidate

    hired_candidates.append(best_candidate)
    interviewed_candidates_copy.remove(best_candidate)

firing_cost = len(hired_candidates) - 1

print("Interviewed candidates:")
for candidate in interviewed_candidates:
    print(f"ID: {candidate[0]}, CGPA: {candidate[1]}, Experience: {candidate[2]}, Role: {candidate[3]}")

print("\nHired candidates:")
for candidate in hired_candidates:
    print(f"ID: {candidate[0]}, CGPA: {candidate[1]}, Experience: {candidate[2]}, Role: {candidate[3]}")

print("\nNumber of candidates hired:", len(hired_candidates))
print("Firing cost:", firing_cost)
