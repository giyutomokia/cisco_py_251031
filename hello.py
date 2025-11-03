from statistics import mean

sum_input = input()
ans = sum_input.split()
valid = []

# convert safely to float
for x in ans:
    try:
        valid.append(float(x))
    except ValueError:
        print("Skipping invalid input:", x)

ans = valid
ans1 = tuple(ans)

print(ans)
print(ans1)

if len(ans) > 0:
    summes = sum(ans)
    avg = mean(ans)

    print("Sum:", summes)
    print("Average:", avg)

    with open("pytttt.txt", "w") as outputfile:
        outputfile.write(str(ans))
        outputfile.write("\nSum: " + str(summes))
        outputfile.write("\nAverage: " + str(avg))

    with open("pytttt.txt", "r") as outputfile:
        print("\nFile content:\n")
        print(outputfile.read())
else:
    print("No valid numeric inputs found.")
