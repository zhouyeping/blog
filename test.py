# -*- coding: utf-8 -*-
# 增删改查, 是这样。  业务复杂，数据量大了怎么办, 处理高并发,应该怎么办呢？
# 每天都要坚持做，这样才能够熟练呀,哈哈. 现在学习好 flask，  mysql， Nginx， redis 这四个组件， 掌握好了在学习其他的,
#  这是现在的任务.

import datetime

from app import db, create_app
from app.models import User
from app.service.BlogService import BlogService


app = create_app('default')
app.app_context().push()


blogs = BlogService()
res = blogs.get_blog_bid(5)
print(res)

print(datetime.date.today())

