import csv

a = []

with open('enjoysport.csv', 'r') as csvfile:
    for row in csv.reader(csvfile):
        a.append(row)
    print(a)

print("\nThe total number of training instances are: ", len(a))

num_attribute = len(a[0]) - 1
print("\nThe initial hypothesis is: ")

hypothesis = ['0'] * num_attribute
print(hypothesis)

for i in range(len(a)):
    if a[i][num_attribute] == 'yes':
        for j in range(num_attribute):
            if hypothesis[j] == '0' or hypothesis[j] == a[i][j]:
                hypothesis[j] = a[i][j]
            else:
                hypothesis[j] = '?'
        print("\nThe hypothesis for the training instance {} is: \n".format(i + 1), hypothesis)

print("\nThe Maximally specific hypothesis for the training instance is", hypothesis)
