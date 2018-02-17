def get_answer(question):
	question = str(question).lower()	
	answers = {'привет':'И тебе привет!',
	'как дела?':'лучше всех',
	'пока':'Увидимся'}
	return(answers[question])
result = get_answer(input('Введите свой вопрос '))
print(result)