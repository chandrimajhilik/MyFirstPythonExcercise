def divide(a,b):
  try:
    result = a/b
    print(result)
    raise JhilikError('Jhilik Error')
    # raise EOFError('some error')
  except ZeroDivisionError:
    print("Error")
  except EOFError:
    print('EOFError')
  except JhilikError as someerr:
    print(someerr)
  finally:
    print("completed")

class Error(Exception):
  pass

class JhilikError(Error):
  def __init__(self, message):
    self.message = message