time_for_one_project = 3

name = input()
projects_to_do = int(input())
time_to_do_all_projects = projects_to_do * time_for_one_project

result = f"The architect {name} will need {time_to_do_all_projects} hours to complete {projects_to_do} project/s."

print(result)
