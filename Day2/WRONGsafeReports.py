import time

exampleData = r"Day2\exampleData"
exampleData2 = r"Day2\exampleData2"
realData = r"Day2\input"


def amountOfSafeReports(dataPath):
    start_time = time.perf_counter()
    safeReports = 0

    with open(dataPath, "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue

                parts = list(map(int, line.split()))
                lineIsSafe = True
                

                if is_strictly_increasing(parts) or is_strictly_increasing_dampener(parts):
                    #print(f"{parts} is strictly increasing")
                    for i in range(len(parts) - 1):
                        diff = abs(parts[i] - parts[i + 1])
                        if 1 <= diff <= 3:
                            print(f"value {parts[i]} and value {parts[i+1]} are okay")
                        else:
                            lineIsSafe = False
                            break  # Exit the loop as the line is not safe
                    if lineIsSafe:
                        safeReports += 1

                elif is_strictly_decreasing or is_strictly_decreasing_dampener(parts):
                    #print(f"{parts} is strictly decreasing")
                    for i in range(len(parts) - 1):
                        diff = abs(parts[i] - parts[i + 1])
                        if 1 <= diff <= 3:
                            print(f"value {parts[i]} and value {parts[i+1]} are okay")
                        else:
                            lineIsSafe = False
                            break  # Exit the loop as the line is not safe
                    if lineIsSafe:
                        safeReports += 1

    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print(f"amountOfSafeReports executed in {elapsed_time:.6f} seconds.")
    return safeReports

def is_strictly_increasing(lst):
    return len(lst) >= 2 and all(lst[i] < lst[i + 1] for i in range(len(lst) - 1))

def is_strictly_decreasing(lst):
    return len(lst) >= 2 and all(lst[i] > lst[i + 1] for i in range(len(lst) - 1))

def is_strictly_increasing_dampener(lst):
    #If we pop ONE value from the list can it be in a safe state?
    if len(lst) >= 2:
        for i in range(len(lst) - 1):
            # if the first value is NOT smaller than the second value we try to pop the 
            if not lst[i] < lst[i + 1]:
                
                lst.pop(i+1)
                if is_strictly_increasing(lst):
                    return True
                else:
                    return False
        
def is_strictly_decreasing_dampener(lst):
    #If we pop ONE value from the list can it be in a safe state?
    if len(lst) >= 2:
        for i in range(len(lst) - 1):
            if not lst[i] > lst[i + 1]:
                lst.pop(i)
                if is_strictly_increasing(lst):
                    return True
                else:
                    return False


if __name__ == "__main__":
    amountOfSR = amountOfSafeReports(exampleData)
    # amountOfSR = amountOfSafeReports(realData)
    print(amountOfSR)