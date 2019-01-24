

def coroutine(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs):
        g.send(None)
        return g
    return inner


class CastomException(Exception):
    pass


#@coroutine
def subgen():
    while True:
        try:
            message = yield
        #except CastomException:
        except StopIteration:
            #print('Exception work')
            break
        else:
            print('Message: ', message)

    return 'Returned from subgen()'

@coroutine
def delegator(g):
    # while True:
    #     try:
    #         data = yield
    #         g.send(data)
    #     except CastomException as c:
    #         g.throw(c)
    result = yield from g
    print(result)
