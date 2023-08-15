score=float(input("Enter the score: "))
if score<0.0 or score>1.0:
    print("Invalid score")
    raise SystemExit
else:
    if score>=0.9:
        grade='A'
    elif score>=0.8:
        grade='B'
    elif score>=0.7:
        grade='C'
    elif score>=0.6:
        grade='D'
    else:
        grade='F'
print("Grade =",grade)
