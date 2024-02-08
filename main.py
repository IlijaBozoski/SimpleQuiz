import random
import time
import sys
def counter(sec,numOfQuestions):
    print(f"Na ova nivo imate {sec} sekundi da odgovorite na {numOfQuestions} prasanja")
    time.sleep(10)
    sec=sec-10
    while sec>=10:
        if(sec==10):
            while sec>0:
                print(sec)
                time.sleep(1)
                sec = sec - 1
        else:
            print(sec)
            time.sleep(10)
            sec = sec - 10

    print("Vremeto istece  vnesete gi vasite odgovori vo format 'abcde'")
def stripAnswer(answer):
    answerCp=answer
    answer1=answerCp[:-3]
    correct=answer[-2]
    return {'answer':answer1,'correct':correct}
def generateQuestionsAndAnswers(questions,answers,l):
    corrAns=""
    pozicija = random.randint(0, l-1)
    print(questions[pozicija])
    finalAns = stripAnswer(answers[pozicija])
    print(finalAns['answer'])
    print("")
    return finalAns['correct']

def printNivo1(easyQuestions,answers):
    correctA=""
    print("Dobredojdovte vo nivo 1")
    questions=easyQuestions
    for i in range(0,5):
        tocno=generateQuestionsAndAnswers(questions,answers,len(questions))
        correctA=correctA+tocno
    return correctA
def printNivo2(easyQuestions,midQuestions,answers):
    correctA = ""
    print("Dobredojdovte vo nivo 2")
    questions= easyQuestions+midQuestions
    print(len(questions))
    for i in range(0,10):
        tocno = generateQuestionsAndAnswers(questions, answers, len(questions))
        correctA=correctA+tocno
    return correctA
def  printNivo3(hardQusetions,answers):
    correctA = ""
    print("Dobredojdovte vo nivo 3")
    questions= hardQusetions
    print(len(questions))
    for i in range(0,5):
        tocno = generateQuestionsAndAnswers(questions, answers, len(questions))
        correctA=correctA+tocno
    return correctA

def checkPoints(inpAns,correctAns):
    pt=0
    if len(inpAns)>len(correctAns):return 0
    else:
        for i in range (0,len(inpAns)):
            if inpAns[i]==correctAns[i]:
                pt+=1
    return pt
def printQuestions(easyQuestions,answers):
    correctAns1=printNivo1(easyQuestions,answers)
    print(correctAns1)
    # counter(60,5)
    inpAns = input().upper()
    points1=checkPoints(inpAns,correctAns1)
    print(f'Vo prvoto nivo osvoivte {points1} poeni')
    if points1<4:
        print("\033[91mXXXXX\033[0m")
        print("\033[91mNemate dovolno poeni za da prodolzite ponatamu\033[0m")

        cases(5)
    print("\033[92mOsvoivte dovolno poeni vo ovaa faza\033[0m")
    time.sleep(2)
    correctAns2=printNivo2(easyQuestions,midQuestions,answers)
    # counter(80,10)
    print(correctAns2)
    inpAns = input().upper()
    points2=checkPoints(inpAns,correctAns2)
    print(f'Vo vtoroto nivo osvoivte {points2} poeni')
    if points2<7:
        print("\033[91mXXXXX\033[0m")
        print("\033[91mNemate dovolno poeni za da prodolzite ponatamu\033[0m")
        cases(5)
    print("\033[92mOsvoivte dovolno poeni vo ovaa faza\033[0m")
    time.sleep(2)
    correctAns3=printNivo3(hardQusetions,hardAnswers)
    # counter(30,5)
    print(correctAns3)
    inpAns = input().upper()
    points3 = checkPoints(inpAns, correctAns3)
    print(f'Vo tretoto nivo osvoivte {points3} poeni')
    points=points1+points2+points3
    print(f'Vkupniot broj na poeni koj go osvoivte e {points}')
    if points>=printMax():
        with open('Scores','w')as file:
            file.write(str(points))
        print("Cestitki vie postavivte nov rekord na poeni")
    else:
        print(f"Dosegasniot rekord na poeni e {printMax()}")
    print("Dali sakate da igrate povtorno [YES/NO]")
    if input().upper()=="YES":
        cases(2)
    else:
        printStartText()
        option = int(input())
        cases(option)


def printManual():
    print("upatostvo")
    with open('Upatstvo', 'r', encoding='utf-8') as file:
        prav=file.read()
        print(prav)
def printMax():
    scores=[]
    with open('Scores', 'r', encoding='utf-8') as file:
        for line in file:
            scores.append(int(line))

    return max(scores)
def printReadTutorial():
    tutorials=[]
    with open('Tutorials', 'r', encoding='utf-8') as file:
        for line in file:
            tutorials.append(line)
    random.shuffle(tutorials)
    print(tutorials[0])

def printStartText():
    print("Dobrodojdovte vo kvizot")
    print("Izberete edna od opciite:")
    print("Upatstvo za igranje...............1")
    print("Start.............................2")
    print("Best Score........................3")
    print("Tutorials.........................4")
    print("Leave.............................5")
def checkBackForEverythingExceptTutorials():
    inp = input()
    if inp == "Back":
        printStartText()
        option = int(input())
        cases(option)

def checkBack():
    inp=input()
    if inp == "Back":
        printStartText()
        option = int(input())
        cases(option)
    elif inp=="Next":
        checkNextTutorial()

def checkNextTutorial():
        printReadTutorial()
        checkBack()


def cases(option):
    if option == 1:
        printManual()
        checkBackForEverythingExceptTutorials()
    elif option == 2:
        printQuestions(easyQuestions,answers)
    elif option == 3:
        print(printMax())
        checkBackForEverythingExceptTutorials()
    elif option==4:
        printReadTutorial()
        checkBack()

    else:
        print("Vi blagodarime i prijatno")
        sys.exit()

questionsList=[];
with open('Prasanja', 'r',encoding='utf-8') as file:
    for line in file:
        questionsList.append(line.strip())
easyQuestions=questionsList[0:16]
midQuestions=questionsList[16:30]
hardQusetions=questionsList[30:]
answers=[]
with open('Odgovori', 'r' ,encoding='utf-8')as file:
    for line in file:
        answers.append(line)

hardAnswers=answers[30:]
printStartText()
option=int(input())
cases(option)
