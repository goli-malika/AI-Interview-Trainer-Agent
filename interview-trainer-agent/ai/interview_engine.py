import random

question_bank = {
    'python developer': [
        'Explain list and tuple difference.',
        'What is Flask?',
        'Explain OOP concepts in Python.',
        'What are decorators in Python?',
        'Difference between GET and POST methods?'
    ],

    'data analyst': [
        'What is data cleaning?',
        'Explain pandas library.',
        'Difference between supervised and unsupervised learning?',
        'What is data visualization?',
        'Explain mean, median, and mode.'
    ],
    'web developer': [
        'What is HTML?',
        'Difference between CSS and JavaScript?',
        'What is responsive design?',
        'Explain frontend and backend.',
        'What is API?'
    ]
}


def generate_questions(role):
    role = role.lower()

    if role in question_bank:
        return random.sample(question_bank[role], 3)

    return [
        'Tell me about yourself.',
        'Why should we hire you?',
        'What are your strengths?'
    ]
def evaluate_answer(question, answer):
    answer_length = len(answer)

    if answer_length > 150:
        score = '9/10'
        feedback = 'Excellent answer with detailed explanation.'

    elif answer_length > 80:
        score = '7/10'
        feedback = 'Good answer but can improve with more technical details.'

    elif answer_length > 30:
        score = '5/10'
        feedback = 'Average answer. Try to explain more clearly.'

    else:
        score = '3/10'
        feedback = 'Answer too short. Add more explanation and examples.'

    return {
        'score': score,
        'message': feedback
    }