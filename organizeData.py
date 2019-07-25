import pandas as pd

# read in company info 
data = pd.read_csv(r'company_list.csv')

# sort based on different things
sorted_elo = data.sort_values(by='ELO')
sorted_true_skill = data.sort_values(by='TrueSkill')
sorted_students_skill = data.sort_values(by=['Total number of students', 'TrueSkill'])
sorted_wins = data.sort_values(by='Total "wins"')

# write sorted things to different values 
sorted_elo.to_csv("sorted_elo.csv")
sorted_true_skill.to_csv("sorted_true_skill.csv")
sorted_students_skill = sorted_students_skill.to_csv("sorted_students_skill.csv")
sorted_wins = sorted_wins.to_csv("sorted_wins.csv")

