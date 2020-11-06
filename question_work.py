from datetime import datetime
from random import shuffle
import os


# FUNCTIONS #

def cleanStr(str):
    return str.replace('\n', '').replace('\r', '').replace('\t', '').replace(' ', '')



def getQuestions(questionsFile, answersFile):
    try:
        quesFile = open(questionsFile)
        questions = quesFile.readlines()
        quesFile.close()
        
        ansFile = open(answersFile)
        answers = ansFile.readlines()
        ansFile.close()
        
        resultList = []
        cnt = 0
        
        for ques in questions:
            ques = cleanStr(ques)
            ans = cleanStr(answers[cnt])
            resultList.append([ques, ans])
            cnt += 1 
        
    except FileNotFoundError as e:
        print('Нет указанного файла: \'' + e.filename + '\'')
        raise SystemExit
    
    except IndexError:
        print('Несовпадение кол-ва вопросов и ответов в файлах')
        raise SystemExit
    
    else:
        return resultList



def askQuestions(questions):
    shuffle(questions)
    questions = questions[:5]
    start = datetime.now()
    end = 0
    userName = ''
    rating = 0

    userName = input('Пожалуйста, укажитете ваше имя\n')
    print('Пожалуйста, ответьте на вопросы:\n')
    
    cnt = 0
    while cnt < len(questions):
        ans = cleanStr( input(questions[cnt][0]+'\n') )
        if ans == questions[cnt][1]:
            result = 'right'
            rating += 1
        else:
            result = 'wrong'
        questions[cnt].append(ans)
        questions[cnt].append(result)
        cnt += 1

    end = datetime.now()
    return userName, start, end, questions, rating



def setAnswersProtocol(userName, start, end, questions, rating):
    ansDir = '.'+ os.sep +'answers'+ os.sep
    if (not os.path.isdir(ansDir)):
        os.mkdir(ansDir)    
    fileName = start.strftime("%Y-%m-%d__%H-%M-%S")
    pathFile = ansDir + fileName + '.txt'
    f = open(pathFile, 'w')
    
    f.write('Имя: '+ userName +'\n')
    
    for quest in questions:
        f.write(quest[0] +'  '+ quest[1] +'  '+ quest[2]+'  '+ quest[3] + '\n')
        
    f.write('Начало: '+ str(start) +'\n')
    f.write('Конец: '+ str(end) +'\n')
    f.write('Оценка: '+ str(rating))
    f.close()


# END FUNCTIONS #



# формируем список вопросов и ответов
questions = getQuestions('questions.txt', 'answers.txt')

# задаём вопросы, получаем ответы
userName, start, end, questions, rating = askQuestions(questions)

# пишем результат
setAnswersProtocol(userName, start, end, questions, rating)
