class Command:
  def __init__(self,method,hasParams:int):
    self.method = method
    self.hasParams = hasParams

  def useCommand(self,params):
    if self.hasParams:
      return(self.method(params))
    else:
      return(self.method())
