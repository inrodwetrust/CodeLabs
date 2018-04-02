#A: 90-100
#B: 80-89
#C: 70-79
#D: 60-69
#F: <60

score = int(input("Enter the test score: "))
if score >= 97:
    print("A+")
elif 93 < score < 97:
    print("A")
elif 90 <= score < 93:
    print("A-")
elif 87 <= score < 90:
    print("B+")
elif 83 < score < 87:
    print("B")
elif 80 <= score < 83:
    print("B-")
elif 77 <= score < 80:
    print("C+")
elif 73 < score < 77:
    print("C")
elif 70 <= score < 73:
    print("C-")
elif 67 <= score < 70:
    print("D+")
elif 63 < score < 67:
    print("D")
elif 90 <= score < 93:
    print("D-")
else:
    print("F")
