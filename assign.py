import json

with open("quiz.json") as json_file:
    data = json.load(json_file)
    for u,v in data.items():
        i=1
        types = {}
        for type, question in v.items():
            print("Press {} for {} quiz.".format(i, type))
            types[i] = type
            i +=1
        select = int(input())
        result = []
        for q, ques in v[types.get(select)].items():
            print(ques["question"])
            i = 1
            for opt in ques["options"]:
                print(i, ".      ", opt)
                i += 1
            ans = int(input())
            try:
                if str(ques["options"][ans - 1]) == ques["answer"]:
                    result.append(1)
                else:
                    result.append(0)
            except:
                result.append(0)
        print("Total Correct Question: ", result.count(1), " out of ", len(result))
