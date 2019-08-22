# This Python file uses the following encoding: utf-8
import json


with open("quiz.json") as json_file:
    data = json.load(json_file)
    print("Press 1 for sports quiz.\nPress 2 for maths quiz.")



    while True:
        i = int(input())
        if i == 1:
            result=[]
            sports = data["quiz"]["sport"]
            print("ANSWER FOLLOWING QUESTIONS BY SELECTING AAPROPRIATE OPTION")
            for u, v in sports.items():
                print(v["question"])
                i = 1
                for opt in v["options"]:
                    print(i, ".      ", opt)
                    i += 1
                ans = int(input())
                try:
                    if str(v["options"][ans - 1]) == v["answer"]:
                        result.append(1)
                    else:
                        result.append(0)
                except:
                    result.append(0)

            print("Total Correct Question: ", result.count(1), " out of ", len(sports))
            break

        elif i == 2:
            result = []
            maths = data["quiz"]["maths"]
            print("ANSWER FOLLOWING QUESTIONS BY SELECTING AAPROPRIATE OPTION")
            for u, v in maths.items():
                print(v["question"])
                i = 1
                for opt in v["options"]:
                    print(i, ".      ", opt)
                    i += 1
                ans = input()
                try:
                    if str(v["options"][ans - 1]) == v["answer"]:
                        result.append(1)
                    else:
                        result.append(0)
                except:
                    result.append(0)

            print("Total Correct Question: ", result.count(1), " out of ", len(maths))
            break
        else:
            print("!!! Please select appropriate option from the given options !!!")


