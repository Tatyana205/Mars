import datetime
from flask import Flask, render_template
from sqlalchemy import text

from Class.data import db_session
from Class.data.users import User
from Class.data.jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
@app.route('/index')
def index():
    param = {'data': []}
    # db_name = input()
    db_session.global_init(f"db/mars_explorer.db")
    db_sess = db_session.create_session()
    for job in db_sess.query(Jobs).all():
        if job.work_size == 1:
            ws = 'hour'
        else:
            ws = 'hours'
        if job.is_finished:
            isf = 'Is finished'
        else:
            isf = 'Is not finished'
        param['data'].append(
            {'id': job.id, 'Title of activity': job.job, 'Team leader': f'{job.user.name} {job.user.surname}',
             'Duration': f'{job.work_size} {ws}', 'List of collaborators': job.collaborators,
             'Is finished': isf})
    # param['title'] = 'Заготовка'
    return render_template('index.html', param=param)


'''def main():
    param = {'data': []}
    # db_name = input()
    db_session.global_init(f"db/mars_explorer.db")
    db_sess = db_session.create_session()
    for job in db_sess.query(Jobs).all():
        param['data'].append(
            {'id': job.id, 'Title of activity': job.job, 'Team leader': f'{job.user.name} {job.user.surname}',
             'Duration': job.work_size, 'List of collaborators': job.collaborators,
             'Is finished': job.is_finished})
    for d in param['data']:
        print(d['id'])
    # param['title'] = 'Заготовка'
    print(param)'''

if __name__ == '__main__':
    app.run(debug=True)
    # main()
