from collections import Counter


def Task2Function(top_Words: int) -> None:
    """Function gives total lines, total words, total unique words, top 10 words and percentage wise distribution of words from given file"""

    unique_Word_List = set()
    total_words_List: list[str] = []
    percentage_Of_Occurrence: dict[str, float] = {}

    with open("src/task2Input.txt", "r") as file:
        data = file.read()
        total_Lines = data.split("\n")
        for line in total_Lines:
            for i in line.split():
                total_words_List.append(i)
                unique_Word_List.add(i)

        word_counts = Counter(total_words_List)
        top_5: list[tuple[str, int]] = word_counts.most_common(top_Words)
        for key, value in word_counts.items():
            percentage_Of_Occurrence[key] = round(
                (value / len(total_words_List)) * 100, 2
            )

        print("Total lines are : ", len(total_Lines))
        print("Total words : ", len(total_words_List))
        print("Total Unique words are : ", len(unique_Word_List))
        print("Top five words from list : ", top_5)
        print("Percentage Wise Distribution : ", percentage_Of_Occurrence)


if __name__ == "__main__":
    Task2Function(5)
