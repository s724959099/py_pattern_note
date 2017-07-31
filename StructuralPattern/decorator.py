def try_catch(fn):
    def wrapper(*args, **kwargs):
        try:
            return fn(*args, **kwargs)
        except Exception as e:
            print(str(e))

    return wrapper


@try_catch
def error_func():
    print("error")
    raise Exception("i am error")


error_func()
