from django import template
from ..models import Post,Category
register=template.Library()#实例化该类

@register.simple_tag#注册这个函数为模板标签
#方便在视图页面中使用语句调用
def get_recent_posts(num=5):
    return Post.objects.all().order_by('-created_time')[:num]

@register.simple_tag
def archives():
    #接受的三个参数值表明了这些含义，一个是 created_time ，
    #即 Post 的创建时间，month 是精度，order='DESC' 表明降序排列
    #（即离当前越近的时间越排在前面）。
    #实现按月归档降序排列
    return Post.objects.dates('created_time', 'month', order='DESC')
@register.simple_tag
def get_categories():
    # 别忘了在顶部引入 Category 类
    return Category.objects.all()
