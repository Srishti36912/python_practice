if __name__ == '__main__':
    student_list = []
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student_list.append([name, score])
        scores.append(score)
           
    scores = list(dict.fromkeys(scores))
    scores.sort()
    targetVal = scores[1]
    
    final_list = []
    for n in range(0, len(student_list)):
        if student_list[n][1] == targetVal :
            final_list.append(student_list[n][0])
        
    final_list.sort()
    
    for a in final_list:
        print(a)