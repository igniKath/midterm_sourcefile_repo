# Store the raw comma-separated records.
raw_records = [
    "Ana,88,92,90",
    "Ben,70,72,74",
    "Cara,95,91,94",
    "Dan,78,80,76",
    "Ella,85,89,87",
    "FRed",
    "Henry,90,eighty,85",
]

# Store the passing average.
PASSING_GRADE = 75

# Create the dictionary that will map names to score lists.
student_scores = {}

# PART A: Parse and organize the records.
for record in raw_records:
    # TODO: Split the record into fields.
    fields = record.split(",")

    # TODO: Add a guardian condition for an invalid field count.
    if len(fields) != 4:
        print("Skipped invalid record:", record)
        continue

    # TODO: Store the student's name.
    name = fields[0]

    # TODO: Convert the score fields to numbers safely.
    scores = []

    try:
        for score in fields[1:]:
            scores.append(float(score))
    except ValueError:
        print("Skipped invalid record:", record)
        continue

    # TODO: Add the name and scores to student_scores.
    student_scores[name] = scores


# PART B: Display records alphabetically.
print("ORGANIZED STUDENT RECORDS")

# TODO: Sort the names and display every student and score list.
for name in sorted(student_scores.keys()):
    scores = student_scores[name]
    print(f"{name}: {scores}")


# Create a list for result tuples.
ranking = []

# Create counters for the class summary.
passed_count = 0
failed_count = 0
sum_of_averages = 0

# PART C: Calculate the student results.
for name, scores in student_scores.items():
    # TODO: Guard against an empty score list.
    if not scores:
        continue

    # TODO: Calculate total, average, highest, and lowest.
    total = sum(scores)
    average = total / len(scores)
    highest_score = max(scores)
    lowest_score = min(scores)

    # TODO: Determine the student's remark.
    if average >= PASSING_GRADE:
        remark = "Passed"
    else:
        remark = "Failed"

    # TODO: Update the passed or failed counter.
    if remark == "Passed":
        passed_count += 1
    else:
        failed_count += 1

    # TODO: Add the average to sum_of_averages.
    sum_of_averages += average

    # TODO: Append the result tuple to ranking.
    result = (
        average,
        name,
        highest_score,
        lowest_score,
        remark
    )
    ranking.append(result)


# PART D: Sort and display the ranking.
# TODO: Sort ranking from highest to lowest average.
ranking.sort(reverse=True)

print("\nSTUDENT GRADE REPORT")
print("Rank  Name       Average  Highest  Lowest  Remark")

# TODO: Use enumerate() and tuple unpacking to display the ranking.
for rank, result in enumerate(ranking, start=1):
    average, name, highest_score, lowest_score, remark = result

    print(
        f"{rank:<5} {name:<10} "
        f"{average:<8.2f} "
        f"{highest_score:<8.0f} "
        f"{lowest_score:<7.0f} "
        f"{remark}"
    )


# PART E: Display the class summary.
# TODO: Calculate the class average safely.
if ranking:
    class_average = sum_of_averages / len(ranking)
else:
    class_average = 0

# TODO: Use ranking[0] and ranking[-1] safely.
if ranking:
    highest_ranked = ranking[0]
    lowest_ranked = ranking[-1]
else:
    highest_ranked = None
    lowest_ranked = None

print("\nCLASS SUMMARY")

# TODO: Display all required summary information.
print(f"Number of Students: {len(ranking)}")
print(f"Passed: {passed_count}")
print(f"Failed: {failed_count}")
print(f"Class Average: {class_average:.2f}")

if highest_ranked:
    print(
        f"Highest: {highest_ranked[1]} - "
        f"{highest_ranked[0]:.2f}"
    )

if lowest_ranked:
    print(
        f"Lowest: {lowest_ranked[1]} - "
        f"{lowest_ranked[0]:.2f}"
    )