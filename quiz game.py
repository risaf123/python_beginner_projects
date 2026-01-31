# QUIZ GAME USING PYTHON

questions = (
    'Which is the tallest animal in the world as of right now?',
    'Is studying engineering at Amal Jyothi a good option?',
    'Who is the GOAT of football?',
    'Which is the fastest animal in the world?',
    'Which is the most decorated programming language in the world?'
)

options = (
    ('A. Elephant', 'B. Zebra', 'C. Lion', 'D. Giraffe'),
    ('A. Yes', 'B. No'),
    ('A. Ronaldo', 'B. Messi', 'C. Pele', 'D. Maradona'),
    ('A. Lion', 'B. Tiger', 'C. Cheetah', 'D. Giraffe'),
    ('A. C++', 'B. JavaScript', 'C. Java', 'D. Python')
)

answers = ('D', 'A', 'B', 'C', 'D')  # all answers in single-letter format

score = 0
guesses = []

for question_num in range(len(questions)):
    print('_____________________')
    print(questions[question_num])
    for option in options[question_num]:
        print(option)
    guess = input('Enter your guess (A/B/C/D): ').upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print('Correct!')
    else:
        print('Incorrect!')
        print(f'The correct answer was {answers[question_num]}')

# Display results
print('________________')
print('RESULTS')
print('________________')
print('Correct Answers:', ' '.join(answers))
print('Your guesses  :', ' '.join(guesses))
score_percentage = (score / len(questions)) * 100
print(f'Score = {score_percentage}%')
