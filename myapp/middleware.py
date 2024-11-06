


class simplemiddleware:


    def __init__(self,get_response):
        self.get_response = get_response


    def __call__(self, request):

        print('Before internship')
        
        response =self.get_response(request)

        print('After internship')

        return response