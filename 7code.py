class MyDefaultMiddleware(object):


    def __init__(self):
        '''当服务器第一次调用请求会调用这个方法。'''
        print('初始化。。。')


    def process_request(self, request):
        '''在匹配url前调用这个方法，传入request'''
        pass
    

    def process_view(self, request, view_func, *view_args, **view_kwargs):
        '''匹配完url后，调用view函数前会调用这个方法'''
        pass


    def process_response(self, request, response):
        '''调用完view后，返回模板前调用这个方法'''
        pass


    def process_exception(self, excp):
        '''出现异常时会调用这个方法'''
        pass


if __name__ == '__main__':
    middleware = MyDefaultMiddleware()

