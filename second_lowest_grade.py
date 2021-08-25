
if __name__ == '__main__':
    
    class_records = []
    scores = set()
    second_lowest = []
   
    for _ in range(int(input())):
        name = input()
        score = float(input())
        scores.add(score)
        class_records.append([name, score])
            
    scores_list = list(scores)
    scores_list.sort()
    second_min = scores_list[1]
    print(f'second min is {second_min}')
    print(f'class_records are {class_records}')
    for record in class_records:
        student = record[0]
        grade = record[1]
        if grade == second_min:
            print(f'name is {record[0]} and grade is {record[1]}')
            second_lowest.append(student)
    
    second_lowest.sort()
    for names in second_lowest:
        print(names)
    
