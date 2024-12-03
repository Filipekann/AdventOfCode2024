import re

exampleData = r"Day3\exampleinput.txt"
realData = r"Day3\input"



def readFileAsAString(filePath):
    try:
        with open(filePath, 'r') as file:
            file_contents = file.read()
        return file_contents
    except FileNotFoundError:
        print(f"Error: The file at {filePath} was not found.")
        return ""

def findMatches(combined_regex, dataString):
    matches = re.finditer(combined_regex, dataString)

    results = []
    keep = True  # Tracks whether to include matches
    for match in matches:
        if match.group(0) == "do()":
            keep = True
        elif match.group(0) == "don't()":
            keep = False
        elif keep and match.group(1) and match.group(2):  # mul(X,Y)
            results.append((int(match.group(1)), int(match.group(2))))
    return results

def multiplyAllMatches(list_of_matches):
    return sum(x * y for x, y in list_of_matches)

def remove_unnecesasry(list):
    keep = True
    keep_list = []
    for match in list:
        if match == "do()":
            keep = True
        elif match == "don't()":
            keep = False

        if keep and match != "do()" and match != "don't()":
            keep_list.append(match)

    return keep_list



if __name__ == "__main__":
    dataString = readFileAsAString(realData)
    #dataString = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    #regular expression
    # mul_regex = r"mul\((\d+),(\d+)\)"
    # do_regex = r"do\(\)"
    # dont_regex = r"don't\(\)"
    combined_regex = r"mul\((\d+),(\d+)\)|do\(\)|don't\(\)"


    # Find and filter matches
    filtered_matches = findMatches(combined_regex, dataString)

    # Print filtered matches
    print("Filtered Matches:", filtered_matches)

    # Multiply all matches
    all_values_multiplied = multiplyAllMatches(filtered_matches)
    print("Result of Multiplication:", all_values_multiplied)

    #values_of_matches = findMatches(mul_regex, dataString)

    #all_values_multiplied = multiplyAllMatches(values_of_matches)

    #print(all_values_multiplied)