from django.http import HttpResponse


def http_method_list(methods: list):
    def http_methods_decorator(func):
        def function_wrapper(request, **kwargs):
            nonlocal methods
            methods = [method.upper() for method in methods]
            if not request.method.upper() in methods:
                return HttpResponse(status=405)   # not allowed

            return func(request, **kwargs)
        return function_wrapper
    return http_methods_decorator
