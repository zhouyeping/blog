# coding: utf-8
from app import create_app
from app.models import User


def get_users():
    return User.query.all()


if __name__ == '__main__':              # 暂时成功了呀， 后来再调试吧.
    app = create_app('default')
    app.app_context().push()

    res = get_users()
    for one in res:
        print one.username



