score_list=[]
unit_list=[]
for i in range(0, 10):
  que=input("input unit\n")
  if que in('4'):
     score=float(input("input your score\n"))
     if (score>=75 and score<=100):
       score_list.append(16)
       unit_list.append(4)
     elif(score>=70 and score<=74):
        score_list.append(14.5)
        unit_list.append(4)
     else:
        print("u cant score less than 70 in project")
  elif que in('3'):
     score1=float(input("input your score\n"))
     if (score1>=75 and score1<=100):
       score_list.append(12)
       unit_list.append(3)
     elif(score1>=70 and score1<=74):
        score_list.append(10.5)
        unit_list.append(3)
     else:
        print("u cant score less than 70 for now")
  elif que in('2'):
     score2=float(input("input your score\n"))
     if (score2>=75 and score2<=100):
       score_list.append(8)
       unit_list.append(2)
     elif(score2>=70 and score2<=74):
        score_list.append(7)
        unit_list.append(2)
     else:
        print("u cant score less than 70 in project")
  elif que in('1'):
     score3=float(input("input your score\n"))
     if (score3>=75 and score3<=100):
       score_list.append(4)
       unit_list.append(1)
print("\nScore List: ",score_list)
print("Unit List: ",unit_list)
score_list= sum(score_list)
unit_list=sum(unit_list)
gp= score_list/unit_list
print("\nYour Total score is: ",score_list)
print("Your Total unit is: ",unit_list)
print("\nYour G.P. is:  ",gp)