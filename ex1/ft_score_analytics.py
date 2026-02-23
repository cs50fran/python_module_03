import sys


def score_analytics():
    print("=== Player Score Analytics ===")

    total_args: int = len(sys.argv)
    scores: list = []

    if total_args == 1:
        print("No scores provided. Usage: python3 "
              "ft_score_analytics.py <score1> <score2> ...")

    else:
        for i in range(1, total_args):
            try:
                score = int(sys.argv[i])
                scores.append(score)

            except ValueError:
                print(f"Score '{sys.argv[i]}' is not an int")
                return None
        print(f"Scores processed: {sys.argv[1:]}")
        print(f"Total Players: {total_args - 1}")
        print(f"Total Score: {sum(scores)}")
        print(f"Average Score: {sum(scores) / (total_args - 1)}")
        print(f"High Score: {max(scores)}")
        print(f"Low Score: {min(scores)}")
        print(f"Score Range: {max(scores) - min(scores)}")
        print()


if __name__ == "__main__":
    score_analytics()
