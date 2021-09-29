import numpy as np
def gpa(letterGrade):
  if (90<=letterGrade<=100):
    return 4.0;
  elif (85<=letterGrade<=89):
    return 4.0;
  elif (80<=letterGrade<=84):
    return 3.7;
  elif (77<=letterGrade<=79):
    return 3.3;
  elif (73<=letterGrade<=76):
    return 3.0;
  elif (70<=letterGrade<=72):
    return 2.7;
  elif (67<=letterGrade<=69):
    return 2.3;
  elif (63<=letterGrade<=66):
    return 2.0;
  elif (60<=letterGrade<=62):
    return 1.7;
  elif (57<=letterGrade<=59):
    return 1.3;
  elif (53<=letterGrade<=56):
    return 1.0;
  elif (50<=letterGrade<=52):
    return 0.7;
  else:
    return 0.0;


marks= [72, 82, 72, 72, 79, 57, 59, 71, 66, 80,
   67, 62, 91, 74, 77, 62, 71, 78, 65, 80,
   70, 74, 70, 95, 76, 66, 85, 64, 79, 57,
   63, 78, 84, 78, 75, 73, 62, 69, 72, 87]

gpa_marks = map(gpa, marks)

print(np.average(list(gpa_marks)))
