from rest_framework.views import APIView, Response, status

import ast
import copy
import cantera as ct

class SolutionView(APIView):
    def get(self, request, **kwargs):
        solutions = []

        for substance in request.GET.get('substances').split(' '):
            try:
                solutions.append(ct.Solution(kwargs['input'] + '.cti', substance))
            except (RuntimeError, ValueError) as e:
                continue

        data = []
        for solution in solutions:
            obj = {'name': solution.name, 'data': []}
            obj_data = obj['data']

            for TP in request.GET.get('TP', '300,101325').split(' '):
                TP = ast.literal_eval(TP)
                solution.TP = TP

                property_dict = {}
                for property in request.GET.get('properties', 'T P density').split(' '):
                    try:
                        if property == u'species':
                            property_dict[property] = map(str, solution.species())
                        else:
                            property_dict[property] = getattr(solution, property, None)
                    except Exception as e:
                        property_dict[property] = None

                obj_data.append(property_dict)

            data.append(obj)

        return Response(data=data)