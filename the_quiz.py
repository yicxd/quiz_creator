question = open("questions.txt")
quest_line = question.readlines()
question.close()

answer = open("answers.txt")
ans_line = answer.readlines()
question.close()

print (quest_line[0]) #well it turns out file lines start at 0 so
print (ans_line[0])   #answer lines are now quest_lines times 2(for the question) PLUS 1(for the correct question)
print (ans_line[1])

print (quest_line[1])
print (ans_line[2])
print (ans_line[3])

print (quest_line[2])
print (ans_line[4])
print (ans_line[5])