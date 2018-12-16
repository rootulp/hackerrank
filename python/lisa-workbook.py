chapters, problems_per_page = list(map(int, input().strip().split(' ')))
problems_per_chapter = list(map(int, input().strip().split(' ')))

pages = [[]]
special_problems = 0

for chapter, problems in enumerate(problems_per_chapter):
    current_problem = 1
    if len(pages[-1]) != 0:
        pages.append([])
    while current_problem <= problems:
        if len(pages[-1]) == problems_per_page:
            pages.append([])
        if current_problem == len(pages):
            special_problems += 1
        pages[-1].append(current_problem)
        current_problem += 1

print(special_problems)
