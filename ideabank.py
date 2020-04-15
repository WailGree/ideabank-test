import sys


while True:
    
    answer = input("What is your new idea? ")
    if answer == "close":
        break
    if   answer == "list":
        print(ideas)
    else:
        ideas = open("ideas.txt", 'w+')

        ideas.write(answer)
        ideas.close()
    if len(sys.argv) > 1 and sys.argv[1]:
        if sys.argv == "--list":
            ideas = open("ideas.text", r)
            for i in len(ideas.readlines):
                print(i+1, ideas[i])