import random

#file management
question = open("questions.txt")
quest_line = question.readlines()
total_lines = len(quest_line)
question.close()

answer = open("answers.txt")
ans_line = answer.readlines()
question.close()

#randomization
random_num = random.randrange(0, total_lines)

#print the quiz
rand_quest = quest_line[random_num]
choices = ans_line[random_num * 2]
correct_ans = ans_line[(random_num * 2) + 1]

print (rand_quest)
print (choices)
print (correct_ans)