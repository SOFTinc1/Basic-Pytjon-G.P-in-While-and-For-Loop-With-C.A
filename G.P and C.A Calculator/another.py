score_list=[]
unit_list=[]
while True:
  que=input("input unit")
  if que in('4'):
     score=float(input("input your score"))
     if (score>=75 and score<=100):
       score_list.append(16)
       unit_list.append(4)
     elif(score>=70 and score<=74):
        score_list.append(14.5)
        unit_list.append(4)
     else:
        print("u cant score less than 70 in project")
  elif que in('3'):
     score1=float(input("input your score"))
     if (score1>=75 and score1<=100):
       score_list.append(12)
       unit_list.append(3)
     elif(score1>=70 and score1<=74):
        score_list.append(10.5)
        unit_list.append(3)
     else:
        print("u cant score less than 70 for now")
  elif que in('2'):
     score2=float(input("input your score"))
     if (score2>=75 and score2<=100):
       score_list.append(8)
       unit_list.append(2)
     elif(score2>=70 and score2<=74):
        score_list.append(6.5)
        unit_list.append(2)
     else:
        print("u cant score less than 70 in project")
  elif que in('1'):
     score2=float(input("input your score"))
     if (score2>=75 and score2<=100):
       score_list.append(4)
       unit_list.append(1)
  try_again=input("do you want to try again? Continue or exit\n")
  if try_again in('y','yes','Y','YES'):
     True
  else:
     print("\nScore List: ",score_list)
     print("Unit List: ",unit_list)
     score_list= sum(score_list)
     unit_list=sum(unit_list)
     gp= score_list/unit_list
     print("\nYour Total score is: ",score_list)
     print("Your Total unit is: ",unit_list)
     print("\nYour G.P. is:  ",gp, "\n \n")