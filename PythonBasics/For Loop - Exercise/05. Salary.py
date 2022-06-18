facebook_tab = 150
instagram_tab = 100
reddit_tab = 50

opened_tabs = int(input())
salary = float(input())

for _ in range(opened_tabs):
    tab_name = input()
    if tab_name == 'Facebook':
        salary -= facebook_tab
    elif tab_name == 'Instagram':
        salary -= instagram_tab
    elif tab_name == 'Reddit':
        salary -= reddit_tab

    if salary <= 0:
        print(f'You have lost your salary.')
        break
if salary > 0:
    print(int(salary))