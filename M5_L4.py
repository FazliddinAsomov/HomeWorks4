1-masala
n = int(input().strip())

if n % 2 == 0:
    quloq_soni = n // 2
    print(quloq_soni)
else:
    print(-1)
2-masala
with open("INPUT.TXT", "r") as input_file:
    original_grade = int(input_file.readline().strip())
def evaluate_grade(original_grade):
    if original_grade < 40:
        return 40 - original_grade
    elif (original_grade + 5) % 3 == 0 and original_grade + 5 <= 100:
        return 5
    else:
        return 0
resulting_grade = original_grade + evaluate_grade(original_grade)
with open("OUTPUT.TXT", "w") as output_file:
    output_file.write(str(resulting_grade))
3-masala
with open("INPUT.TXT", "r") as input_file:
    N = int(input_file.readline().strip())
if N % 2 == 0:
    result = "First player"
else:
    result = "Second player"
with open("OUTPUT.TXT", "w") as output_file:
    output_file.write(result)
5-masala
with open("INPUT.TXT", "r") as input_file:
    N = int(input_file.readline().strip())
result = N // 2
with open("OUTPUT.TXT", "w") as output_file:
    output_file.write(str(result))