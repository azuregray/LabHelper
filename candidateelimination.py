import numpy as np
import pandas as pd

data = pd.read_csv('enjoysport.csv')

concepts = np.array(data.iloc[:, 0:-1])
print("Concepts:\n", concepts)

target = np.array(data.iloc[:, -1])
print("Target:\n", target)

def learn(concepts, target):
    specific_h = concepts[0].copy()
    print("Initialization of specific_h and general_h")
    print("Specific Hypothesis:", specific_h)

    general_h = [["?" for i in range(len(specific_h))] for i in range(len(specific_h))]
    print("General Hypothesis:", general_h)
    for i, h in enumerate(concepts):
        print("For Loop Iteration", i + 1)
        if target[i] == "yes":
            print("Instance is Positive")
            for x in range(len(specific_h)):
                if h[x] != specific_h[x]:
                    specific_h[x] = '?'
                    general_h[x][x] = '?'

        elif target[i] == "no":
            print("Instance is Negative")
            for x in range(len(specific_h)):
                if h[x] != specific_h[x]:
                    general_h[x][x] = specific_h[x]
                else:
                    general_h[x][x] = '?'
        print("Steps of Candidate Elimination Algorithm", i + 1)
        print("Specific Hypothesis:", specific_h)
        print("General Hypothesis:", general_h)
        print("\n")
    general_h = [h for h in general_h if h != ['?' for _ in range(len(specific_h))]]
    return specific_h, general_h

s_final, g_final = learn(concepts, target)
print("Final Specific Hypothesis:", s_final)
print("Final General Hypothesis:", g_final)