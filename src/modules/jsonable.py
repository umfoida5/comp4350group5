import datetime
import json

"""
    Decorator class that adds a to_dict() function to the decorated
    class
"""
class Jsonable:
    def __init__(self, *args):
        self.fields = args

    def __call__(self, cls):
        cls._jsonFields = self.fields

        def to_dict(self):
            dict_representation = {}

            for attribute in self.__class__._jsonFields:
                value = getattr(self, attribute)

                if isinstance(value, list):
                    dict_representation[attribute] = []
                    for i in value:
                        if hasattr(i.__class__, '_jsonFields'):
                            dict_representation[attribute].append(i.to_dict())
                        else:
                            dict_representation[attribute].append(i)
                    continue

                if type(value) is datetime.date:
                    dict_representation[attribute] = str(value) 
                elif type(value) is datetime.datetime:
                    dict_representation[attribute] = value.strftime("%y-%m-%d %H:%M:%S")                
                elif hasattr(value.__class__, '_jsonFields'):
                    dict_representation[attribute] = value.to_dict()
                else:
                    dict_representation[attribute] = value

            return dict_representation

        cls.to_dict = to_dict
        return cls

"""
    This function accepts a jsonable value (list or single element)
    and calls to_dict() to transform the value into a python dictionary.

    Useful for passing lists resulting from a query
"""
def make_jsonable(value):
	if isinstance(value, list):
		jsonable_data = []	
		for element in value:
			jsonable_data.append(element.to_dict())
	else:
		jsonable_data = value.to_dict()

	return jsonable_data