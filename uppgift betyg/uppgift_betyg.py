p = int(input("vad fick hen for poang pa provet (0-100)"))

if p>90:
    print("betyg A")
elif p<90 and p>80:
    print("betyg B")
elif p<80 and p>70:
    print("betyg C")
elif p<70 and p>60:
    print("betyg D")
elif p<60 and p>50:
    print("betyg E")
else:
    print("betyg F")

