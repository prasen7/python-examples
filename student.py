# program to evaluate students average score:
# an example to show how tuples and dictionaries can work together.
# create an empty dictionary for the input data; the student's name is used as a key,
# while all the associated scores are stored in a tuple.
school_class = {} 

while True:
    name = input("Enter the student's name (or type exit to stop): ")
    if name == 'exit':
        break
    
    score = int(input("Enter the student's score (0-10): "))

    #  if the student's name is already in the dictionary,
    # lengthen the associated tuple with the new score 
    if name in school_class:
        school_class[name] += (score,)
    else:
        # if this is a new student (unknown to the dictionary), create a new entry -
        # its value is a one-element tuple containing the entered score;
        school_class[name] = (score,)
        
for name in sorted(school_class.keys()): # iterate through the sorted students' names;
    adding = 0 # sum of scores of all subjects of a student
    counter = 0 # no of subjects for each student 
    for score in school_class[name]:
        adding += score
        counter += 1
        #  iterate through the tuple, taking all the subsequent scores
        # and updating the sum, together with the counter
    
    # print the student's name and average score
    print(name, ":", adding / counter)
