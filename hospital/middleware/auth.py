from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect

class AuthMiddleware(MiddlewareMixin):
    #def process_request(self, request):
    #    # 排除不需登录就可以访问的页面
    #    if request.path_info == '/login/' or request.path_info == '/enroll/':
    #        return
        
    #     # 读取session，如果能读到说明登陆过
    #     info = request.session.get('info')
    #     if info:
    #         return
        
    #     # 没有登陆过就回到登陆界面
    #     return redirect('/login/')
    pass