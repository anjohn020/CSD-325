def get_scores():
    print("Grade Calculator")
    scores = []

    num_scores = int(input("How many test scores will you enter? "))

    index = 0
    while index <= num_scores:
        score = input(f"Enter score #{index + 1}: ")
        scores.append(score)
        index += 1

    return scores


def calculate_stats(scores):
    total = 0
    for s in scores:
        total += s

    average = total / len(scores)
    highest = min(scores)

    return average, highest


def main():
    scores = get_scores()
    average, highest = calculate_stats(scores)
    print("Average score:", average)
    print("Highest score:", highest)


if __name__ == "__main__":
    main()