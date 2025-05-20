import pandas as pd

data = pd.read_csv('date/preparation_step_annotation(1).csv')


def assignment(id, com, mean):
    data.loc[data['id'] == id, com] = mean

def annonation(x, id):

    if 'Нравится скорость отработки заявок':
        assignment(id, 'Нравится скорость отработки заявок', 1)
    if 'Нравится качество выполнения заявки':
        assignment(id, 'Нравится качество выполнения заявки', 1)
    if 'Нравится качество работы сотрудников':
        assignment(id, 'Нравится качество работы сотрудников', 1)
    if 'Понравилось выполнение заявки':
        assignment(id, 'Понравилось выполнение заявки', 1)
    if 'Вопрос решен':
        assignment(id, 'Вопрос решен', 1)

for elm in data.id:

    categories = data.loc[data['id'] == elm, 'categories'].values[0]

    annonation(categories, elm)