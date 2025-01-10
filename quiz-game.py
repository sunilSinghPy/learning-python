
questions = [
    {
        "prompt" : "What is the capital of Bihar",
        "option" : ['delhi','patna','kanpur','gorakhpur'],
        "answer" : "A"
    },
    {
        "prompt" : "Who is the  cheif ministar of Bihar",
        "option" : ['modi','mayawati','nitish','akhilesh'],
        "answer" : "C"
    },
    {
        "prompt" : "which is the lognest river in patna?",
        "option" : ['yamuna', 'ganga', 'gandak','ghaghra'],
        "answer" : "B"
    },
    {
        "prompt" : "who discover telephone?",
        "option" : ['ramanujan','luie pascal','wright brothers','graham bell'],
        "answer" : "D"
    },
    {
        "prompt" : "What is the capital of India?",
        "option" : ['delhi','patna','kanpur','gorakhpur'],
        "answer" : "A"
    },
]

def quiz(questions):
    scores = 0
    for question in questions:
        print(question['prompt'])
        option_index = {0:'A', 1:'B', 2:'C', 3:'D'}
        for i,o in enumerate(question['option']):
            for key,opt in option_index.items():
                if i == key:
                    print(opt+'.'+o)
        while True:
            answer = input("Please Enter right Option(A/B/C/D)").upper()
            if(answer == 'A' or answer =='B' or answer =='C' or answer == 'D'):
                break
            else:
                continue
        if answer == question['answer']:
            scores += 1
            print(f"Correct!! Your Score is {scores}")

        else:
            print(f"Wrong Answer!! Your Score is {scores}")
        print("=========================")
        
        
    print(f"Your final score is :{scores}")

quiz(questions)