def forever(function):
  while True:
    function()
    
"""
forever(lambda: (
  print("Hello World!"),
  print("It's a function, that runs forever!")
))
"""
