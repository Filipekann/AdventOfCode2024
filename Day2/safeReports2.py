exampleData = r"Day2\exampleData"
exampleData2 = r"Day2\exampleData2"
realData = r"Day2\input"


def readFileToList(filePath):
    fileAsList = []
    with open(filePath, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            lineValue = list(map(int, line.split()))
            fileAsList.append(lineValue)
    return fileAsList


def amountOfSafeReports(listOfReports):
    amountOfSafeReports = 0
    for report in listOfReports:
        # Check if the original report is safe
        if is_report_safe(report):
            amountOfSafeReports += 1
        else:
            # Try removing each level one by one
            for i in range(len(report)):
                modified_report = report[:i] + report[i+1:]
                if is_report_safe(modified_report):
                    amountOfSafeReports += 1
                    break  # No need to try any more removals
    return amountOfSafeReports



def is_report_safe(report):
    # Check if report has at least two levels
    if len(report) < 2:
        return False

    # Check if differences are within the allowed range and determine direction
    diffs = [report[i+1] - report[i] for i in range(len(report)-1)]
    if not all(1 <= abs(d) <= 3 for d in diffs):
        return False  # Differences out of allowed range

    # Check if strictly increasing or decreasing
    if all(d > 0 for d in diffs):
        return True  # Strictly increasing
    elif all(d < 0 for d in diffs):
        return True  # Strictly decreasing
    else:
        return False  # Not strictly increasing or decreasing

if __name__ == "__main__":
    listOfReports = readFileToList(realData)
    safeReports = amountOfSafeReports(listOfReports)
    print(f"Amount of safe reports: {safeReports}")