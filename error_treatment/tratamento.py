"""Classe auxiliar"""
class Treatment:
    """Faz o tratamento de erro"""
    def error_treatment(type_of_error: tuple, message: tuple[bool, str]):
        def receive_func(func):
            def closure(*args, **kwgs):
                try:
                    return func(*args, **kwgs)
                except type_of_error:
                    if message[0]:
                        print(message[1])
            return closure
        return receive_func
