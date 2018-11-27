import random

def selection():
    print('What section would you like to play? (Python, Math, General Knowledge)')
    category = input('>>>').lower()
    if category == 'python':
        return 'Category_Python.txt'
    elif category == 'math':
        return 'Category_Math.txt'
    elif category == 'general knowledge':
        return 'Category_GK.txt'
    else:
        print('That is no category!')

def main():
    score = 0
    category = selection()
    num_lines = sum(1 for line in open(category))
    questions = []
    for x in range(0, num_lines):
        if (x%2!=0):
            questions.append(x)
    game = 0
    while game == 0:
        f = open(category, "r")
        lines = f.readlines()
        choice = random.choice(questions) - 1
        print(lines[choice])
        answer = input('>>>')
        if score >= 5:
            print('You won!')
            game = 1
        elif answer == lines[choice + 1].strip():
            print('Correct')
            score += 1
        elif answer == 'save':
            print('What is your name?')
            name = input('>>>')
            save = open("saves.txt", "a")
            save.writelines(name)
            save.writelines(str(score))
        else:
            print('In-Correct')
    print('Thank you for playing!')



main()