import time

exampleData = r"Day1\exampleInputData.txt"
realData = r"Day1\inputData"



def createSortedLists(dataPath):
    start_time = time.perf_counter()

    l_values = []
    r_values = []
    with open(dataPath, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            parts = line.split()
            if len(parts) >= 2:
                l_values.append(int(parts[0]))
                r_values.append(int(parts[1]))
            else:
                print(f"Empty line or no data: {line}")
    
    l_values.sort()
    r_values.sort()

    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print(f"createSortedLists executed in {elapsed_time:.6f} seconds.")

    return l_values, r_values

def totalDistanceBetweenLists(left_list, right_list):
    start_time = time.perf_counter()

    distance = 0
    if len(left_list) == len(right_list):
        for i in range(len(left_list)):
            if left_list[i] > right_list[i]:
                distance += left_list[i] - right_list[i]
            else:
                distance += right_list[i] - left_list[i]
    
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print(f"totalDistanceBetweenLists executed in {elapsed_time:.6f} seconds.")

    return distance

def smililartyScore(left_list,right_list):
    similarityScore = 0
    for value in left_list:
        similarityScore += value * (right_list.count(value))

    return similarityScore

def test(dataPath): 
    l_sorted_values, r_sorted_values = createSortedLists(dataPath)
    
    """
    totalDistance = totalDistanceBetweenLists(l_sorted_values, r_sorted_values)
    print("\nTotal distance:", totalDistance)
    """
    Score = smililartyScore(l_sorted_values,r_sorted_values)
    print(Score)


if __name__ == "__main__":
    test(realData)