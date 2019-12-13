#-*- coding:utf-8 -*-
def outer_function(msg):
    def inner_function():
        print msg
    return inner_function

hi_func = outer_function('Hi')
bye_func = outer_function('Bye')

hi_func() #print 부분
bye_func() #print 부분

def decorator_function(original_function): #1
    def wrapper_function(): #5
        return original_function() #7
    return wrapper_function #6

def display(): #2
    print 'display 함수가 실행 되었습니다.' #8

decorated_display = decorator_function(display) #3
decorated_display() #4

# decorator 을 사용하면 기존의 코드를 수정하지 않고도,
# (wapper)함수를 이용하여 여러 기능을 추가 할 수 있다.

def decorator_function(original_function):
    def wrapper_function():
        print '{} 함수가 호출되기전 입니다.'.format(original_function.__name__)
        return original_function()
    return wrapper_function

def display_1():
    print 'display_1 함수가 실행됐습니다.'
def display_2():
    print 'display_2 함수가 실행됐습니다.'

display_1 = decorator_function(display_1)
display_2 = decorator_function(display_2)

display_1()
print
display_2()
