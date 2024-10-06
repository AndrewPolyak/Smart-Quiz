# The userkey is a list of user's answers expressed as a number from 0-3 corresponding a - d

def grader(userkey, AI_Output):
    answerkey = []
    answer = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # Generate the correct answer key, i+1 = question number j['question'] = question, k = correct answer id
    for i, j in enumerate(AI_Output):
        for k, l in enumerate(j['answers']):
            if l['is_correct'] == 1:
                answerkey.append(k)
    for m, n in enumerate(answerkey): # m is the question number
        if userkey[m] == answerkey[m]:
            answer[m] = AI_Output[m]['answers'][answerkey[m]]['answer']
        
    return(answer)