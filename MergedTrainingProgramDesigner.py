import random
import time
from operator import itemgetter

# Print 2D array row by row
def printArray(array):
    for i in range(0,len(array)):
        print(array[i])
# Prints a week with its scores
def printWeek(week, scores):
    print("Training|Score|Monday-Tuesday-Wednasday-Thursday-Friday")
    for i in range(0,len(week)):
        print(f'{scores[i][0]:8}{scores[i][1]:6}{week[i]}')
    print()
# Creates random scores for every training
def randomScores(scores):
    for i in range (0, len(scores)):
        scores[i][0] = chr(ord('A')+i)
        scores[i][1] = random.randint(0, 1000)
# Probability Function that return true or false for a training
def probilityScores(scores, i):
    if(scores[i][1] <=150):#Level = 1
        level = 1
    elif(151 <= scores[i][1] <=300):#Level = 2
        level = 2
    elif (301 <= scores[i][1] <= 450):#Level = 3
        level = 3
    elif (451 <= scores[i][1] <= 600):#Level = 4
        level = 4
    elif (601 <= scores[i][1] <= 750):#Level = 5
        level = 5
    elif (751 <= scores[i][1] <= 900):#Level = 6
        level = 6
    elif (901 <= scores[i][1] <= 1000):#Level = 7
        level = 7
    # For seven levels we have true false array with length 7
    trueFalseArray = [True] * 7
    # Puts false to array number of level times
    for j in range(0, level):
        trueFalseArray[j] = False
    # Shuffles the array for better probability
    random.shuffle(trueFalseArray)
    # Return a random element from the array true or false
    return trueFalseArray[random.randint(0, 6)]
# Creates a weekly schdule
def createWeekly(week,scores,scoresAdd):
    row = random.randint(0,8) # A random row
    column = random.randint(0,6) # A random column

    numberOfOnesRow = 0 # Holds the number ones in a row
    numberOfOnesColumn = 0 # Holds the number ones in a column
    for i in range(0,7): # Counts the number of ones in a row
        if(week[row][i] == 1):
            numberOfOnesRow += 1
    for i in range(0,9): # Counts the number of ones in a column
        if(week[i][column] == 1):
            numberOfOnesColumn += 1
    # Decides is possible to put a one to this random index
    if(week[row][column] == 0 and numberOfOnesRow <= 4 and numberOfOnesColumn <= 5 ):
        tf = probilityScores(scores, row) # Returns true or false with the probability of level for the training in this row
        if (column == 0 and week[row][column+1] == 0 and tf): # If right side of the index is available
            week[row][column] = 1 # Put a one
            scoresAdd[row] += random.randint(2,4) # Increase of the performance for this training
        elif (column == 6 and week[row][column-1] == 0 and tf): # If left side of the index is available
            week[row][column] = 1 # Put a one
            scoresAdd[row] += random.randint(2, 4) # Increase of the performance for this training
        elif (column !=0 and column != 6 and week[row][column-1] == 0 and week[row][column+1] == 0 and tf): # If right and left side of the index is available
            week[row][column] = 1 # Put a one
            scoresAdd[row] += random.randint(2, 4) # Increase of the performance for this training
#Creates a session
def createSessionProbability():

    scores = [[0 for i in range(2)]for j in range(9)] # Holds the scores of the trainings
    scoresAdd = [0] * 9 # Holds the performance increase for every training
    randomScores(scores) # Creates random scores
    #printArray(scores)

    for i in range(0,10): # Make schdule for 10 weeks
        week = [[0 for i in range(7)] for j in range(9)] # Create a week
        print("WEEK:",i+1)
        counter = 0 # For random index
        while(counter < 500 ):
            createWeekly(week, scores, scoresAdd)
            counter += 1
        printWeek(week, scores) # Print this week
    for i in range(0,9): # Adds the performance increases to trainings
        scores[i][1] = scores[i][1] + scoresAdd[i]
    print("FINAL PROGRAM")
    printWeek(week, scores) # Final program with performance increases
#******************NEW ALGORITHM******************
def createSessionLeastFive():
    LessonValues = []
    Lesson = [["A", int(random.uniform(1, 1000))], ["B", int(random.uniform(1, 1000))],
              # Creating random values for lessons.
              ["C", int(random.uniform(1, 1000))],
              ["D", int(random.uniform(1, 1000))], ["E", int(random.uniform(1, 1000))],
              ["F", int(random.uniform(1, 1000))], ["G", int(random.uniform(1, 1000))],
              ["H", int(random.uniform(1, 1000))],
              ["I", int(random.uniform(1, 1000))]]
    Lesson.sort(key=itemgetter(1), reverse=False)  # Sorting list from smallest to largest
    print(Lesson)
    counter = 0
    while counter < 10:  # Week counter.
        print("Week ", counter + 1, " program:")
        print(" ")
        Lesson.sort(key=itemgetter(1), reverse=False)  # Re-sort the list every week.
        FiveLesson = ["", "", "", "", ""]  # Five lessons that has least point.
        FourLesson = ["", "", "", "", "empty"]  # Four lessons that has the most point.
        i = 0
        while i < 5:  # Creating five lessen list
            FiveLesson[i] = Lesson[i][0]
            i = i + 1

        while i < 9:  # Creating four lesson list.
            FourLesson[i - 5] = Lesson[i][0]
            i = i + 1

        print("%-15s %-15s %-15s %-15s %-15s %-15s  %s" % (  # Printing the program weekly.
            "Monday", "Tuesday", "Wednesday", "Thursday", "Friday,", "Saturday", "Sunday"))
        print("---------------------------------------------------------------------------------------------------------")
        i = 0
        while i < 5:
            print("%-15s %-15s %-15s %-15s %-15s %-15s %s" % (
            FiveLesson[i], FourLesson[i], FiveLesson[i], FourLesson[i], FiveLesson[i], FourLesson[i], FiveLesson[i]))
            i = i + 1
        i = 0
        """ Givig random points to the lesson between 2 and 4. Some least 5 lessons get 4 times, most 4 gets three times."""
        while i < 4:
            t = 0

            while t < 5:
                Lesson[t][1] = Lesson[t][1] + int(random.uniform(2, 4))
                t = t + 1
            i = i + 1
        i = 0
        t = 5
        while i < 3:
            t = 5

            while t < 9:
                Lesson[t][1] = Lesson[t][1] + int(random.uniform(2, 4))
                t = t + 1
            i = i + 1

        counter = counter + 1
##******************NEW ALGORITHM******************
def sum_column(arr,column_number): #sum 1's of a column
    sum=0
    for i in range(len(arr)):
            sum+=arr[i][column_number]
    return sum
def fixedDaysToLeves():
    levels_to_days=[4,3,3,3,2,2,1] # level 1 to 7 as training days, for level 1 there are 4 days and so on

    schedule=[['A','none',0,0,0,0,0,0,0,0], #this is my schedule for weekly
              ['B','none',0,0,0,0,0,0,0,0],
              ['C','none',0,0,0,0,0,0,0,0],
              ['D','none',0,0,0,0,0,0,0,0],
              ['E','none',0,0,0,0,0,0,0,0],
              ['F','none',0,0,0,0,0,0,0,0],
              ['G','none',0,0,0,0,0,0,0,0],
              ['H','none',0,0,0,0,0,0,0,0],
              ['I','none',0,0,0,0,0,0,0,0]]



    for i in range(len(schedule)): #assigning random scores between 0-1000 and their levels into schedule array
        choose_score=random.randint(0,1000)
        schedule[i][1]=choose_score
        level=(choose_score//150)+1
        #print(choose_score,' ',level)
        schedule[i][2]=level

    week=0
    while week!=10: #10 weeks
        post_scores=[0,0,0,0,0,0,0,0,0] #post scores A to I

        for i in range(len(schedule)): #A to I
            days_number=levels_to_days[schedule[i][2]-1] #assign how many day will work according to level

            if days_number==4: #level 1 there will be 4 days for sure and there is one option
                schedule[i][3] = 1
                schedule[i][5] = 1
                schedule[i][7] = 1
                schedule[i][9] = 1

            counter = 0 # trying times to putting 1's and can't find a position
            while days_number!=4 and days_number!=0: #if days number is not 0 and 4

                choose_day = random.randint(3, 9) #choosing a day randomly

                #if conditions for the rules column can't be more than 5 or days can't come consecutively
                if schedule[i][choose_day]!=1 and (sum_column(schedule,choose_day)<=5) and choose_day!=3 and choose_day!=9 and schedule[i][choose_day-1]!=1 and schedule[i][choose_day+1]!=1:
                    days_number=days_number-1
                    schedule[i][choose_day]= 1
                elif schedule[i][choose_day]!=1 and (sum_column(schedule,choose_day)<=5) and choose_day==3 and schedule[i][choose_day+1]!=1:
                    days_number = days_number - 1
                    schedule[i][choose_day] = 1
                elif schedule[i][choose_day]!=1 and (sum_column(schedule,choose_day)<=5) and choose_day==9 and schedule[i][choose_day-1]!=1:
                    days_number = days_number - 1
                    schedule[i][choose_day] = 1
                else:
                    counter+=1

                if counter==100: #trying times
                    break #if there is no more proper position leave it

        #printing schedule
        print("\nWEEK :" , week+1, "\n")
        for i in range(len(schedule)):
            for j in range(3,len(schedule[i])):
                if schedule[i][j] == 1:
                    post_scores[i]+=random.randint(2, 4)

            if week==9: #print weekly , post level-scores too at the end
                print(schedule[i],'[' ,post_scores[i]+schedule[i][1],((post_scores[i]+schedule[i][1]) // 150) + 1, ']')  # post scores
            else:
                print(schedule[i])



        for i in range(len(schedule)): #RESET weekly
            for j in range(3,len(schedule[i])):
                schedule[i][j]=0


        week+=1 #next week


print("***WELCOME TO TRAINING PROGRAM DESIGNER***")
wanted = 0
while wanted != 4:
    print("\nHow would you want to create a 10 week training session?")
    wanted = int(input("1.With least 5 training \n2.Trainings with Probability  \n3.With Fixed Day According to Levels \n4. For quit\n"))
    if wanted == 1:
        createSessionLeastFive()
    elif wanted == 2:
        createSessionProbability()
    elif wanted == 3:
        fixedDaysToLeves()
    elif wanted != 4:
        print("NOT A VALID INPUT!!!")
print("QUITING...")
time.sleep(1)
print("QUITED")
