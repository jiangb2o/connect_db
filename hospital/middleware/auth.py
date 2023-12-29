from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect

class AuthMiddleware(MiddlewareMixin):
    # def process_request(self, request):
    #     # 截获请求的url路径
    #     path = request.path_info

    #     # 排除不需登录就可以访问的页面
    #     if path == '/login/' or path == '/enroll/':
    #         return
        
    #     # 读取session，如果登录方式符合请求url就允许登录
    #     login_type = request.session.get('info')['login_type']
    #     print(request.session.get('info'))
    #     if login_type == 'patient_login' and '/patient/' in path:
    #         return
    #     elif login_type == 'doctor_login' and '/doctor/' in path:
    #         return
        
    #     # 没有登陆过就回到登陆界面
    #     return redirect('/login/')
    pass