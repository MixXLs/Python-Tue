survey_results = [
    ["Python", "JavaScript", "C++"],
    ["Python", "JavaScript", "C#"],
    ["Python", "Java"],
    ["Python", "C++", "JavaScript"],
    ["Python", "JavaScript", "C++", "Java"]
]

survey_results_sets = [set(i) for i in survey_results]

all_participants = set.intersection(*survey_results_sets)
print(" All Participants :", all_participants)