import time

def getPlayerInput(question):
    answer = input(question)
    return answer.lower().strip() 

def delayPrint(text, delay):
    print(text)
    time.sleep(delay) 

def coolTransition(delay=0.25):
    time.sleep(delay)
    for i in range(3):
        delayPrint(".", delay)
    time.sleep(delay)