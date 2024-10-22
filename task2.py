from collections import Counter

def Task2Function(topWords):
    uniqueWordList = set()
    totalwordsList = []
    percentageOfOccurrence = {}

    with open('src/task2Input.txt','r') as file:
        data = file.read()
        totalLines = data.split('\n')
        for line in totalLines:
            for i in line.split():
                totalwordsList.append(i)
                uniqueWordList.add(i)

        word_counts = Counter(totalwordsList)
        top_5 = word_counts.most_common(topWords)        
        for key,value in word_counts.items():
            percentageOfOccurrence[key] = round((value / len(totalwordsList)) * 100,2)
            
        print("Total lines are : ",len(totalLines))
        print("Total words : ",len(totalwordsList))
        print("Total Unique words are : ",len(uniqueWordList))
        print("Top five words from list : ",top_5)
        print("Percentage Wise Distribution : ",percentageOfOccurrence)

if __name__ == '__main__':
    Task2Function(10)