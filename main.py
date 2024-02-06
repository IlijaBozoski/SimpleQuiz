import time
def printQuestions():
    print("prasanja")
def printManual():
    print("upatostvo")
    with open('Upatstvo', 'r', encoding='utf-8') as file:
        prav=file.read()
        print(prav)
def printMax():
    print("max")
def printStartText():
    print("Dobrodojdovte vo kvizot")
    print("Izberete edna od opciite:")
    print("Upatstvo za igranje...............1")
    print("Start.............................2")
    print("Best Score........................3")
    print("Leave.............................4")
def cases(option):
    if option == 1:
        printManual()
        if input() == "Back":
            printStartText()
            option = int(input())
            cases(option)

    elif option == 2:
        printQuestions()
    elif option == 3:
        printMax()
    else:
        print("Vi blagodarime i prijatno")


def counter(sec,numOfQuestions):
    print(f"Na ova nivo imate {sec} da odgovorite na {numOfQuestions} prasanja")
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

    print("Vremeto istece  vnesete gi vasite odgovori")

questionsList=[];
with open('Prasanja', 'r',encoding='utf-8') as file:
    for line in file:
        questionsList.append(line.strip())
easyQuestions=questionsList[0:15]
midQuestions=questionsList[15:30]
hardQusetions=questionsList[30:]


printStartText()
option=int(input())
cases(option)


# print(questionsList[10])
# counter(50,5)