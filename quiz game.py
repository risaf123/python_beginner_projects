#QUIZ GAME USING PYTHON
questions=(('Which is the tallest animal in the world as of right now?'),
           ('Is studying engineering at amal jyothi a good option?'),
           ('Who is the Goat of football?'),
           ('Which is the fastest animal in the world?'),
           ('Which is the most decorated programming language in the world?'))
options=(('A.elephant','B.zebra','C.lion','D.giiraff'),
         ('yes','no'),
         ('A.Ronaldo','B.Messi','C.Pele','D.Maradona'),
         ('A.lion','B.tiger','C.cheetah','D.giiraff'),
         ('A.c++','B.javascript','C.java','D.python'))
score=0
answers=('D','yes','A','C','D')
gueses=[]
question_num=0
for quetion in questions:
    print('_____________________')
    print(quetion)
    for option in options[question_num]:
        print(option)
    guess=input('enter your guess as(A,B,C,D)').upper()
    gueses.append(guess)
    if guess==answers[question_num]:
        score+=1
        print('correct' )
    else:
         print('incorrect')
         print(f'{answers[question_num]} was correct')
    question_num+=1
print('________________')
print('RESULTS')
print('________________')
print('ANSWERS', end=' ')
for answer in answers:
    print(answer,end=' ')
print()
score=score/len(questions)*100
print('score=',score)