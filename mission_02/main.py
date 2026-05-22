#RAW SCORES WITH MIXED VALUES(VALID AND INVALID ENTRIES)
raw_scores = [23,56,78,27,455,-56,0,90,131,-3]

#FUNCTION TO CLEAN THE SCORES
def clean_score(scores):
    cleaned_scores = []

    for score in scores:
        if 0 <= score <= 100:
            cleaned_scores.append(score)

    return cleaned_scores

#FUNCTION FOR REPORTING
def report(scores):
    #STATISTICS
    number_valid = len(scores)
    average_score = sum(scores) / number_valid
    highest_score = max(scores)
    lowest_score = min(scores)

    #PRINTING SUMMARY
    print("----------SUMMARY---------")
    print(f"Valid count: {number_valid}")
    print(f"Average: {average_score:.2f}")
    print(f"Highest: {highest_score}")
    print(f"Lowest: {lowest_score}")

    #CLASSIFICATION OF PERFORMANCE
    print("----------PERFORMANCE LABELS---------")
    for score in scores:
        if score >= 90:
            performance_label = "Excellent"
        elif score >= 75:
            performance_label = "Good"
        elif score >= 50:
            performance_label = "Pass"
        else:
            performance_label = "Needs Improvement"
            
        #PRINTING PERFORMANCE LABELS
        print(f"{score} -> {performance_label}")

#CALLING THE FUNCTION TO CLEAN SCORES
valid_scores = clean_score(raw_scores)
print("----------CLEANED SCORES---------")
print(valid_scores)

#CALLING THE FUNCTION TO GENERATE REPORT
report(valid_scores)