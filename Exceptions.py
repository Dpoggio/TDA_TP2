
class CustomException(Exception):
     def __init__(self, *args, **kwargs):
         default_message = 'This is a default message!'

         # if no arguments are passed set the first positional argument
         # to be the default message. To do that, we have to replace the
         # 'args' tuple with another one, that will only contain the message.
         # (we cannot do an assignment since tuples are immutable)
         if not (args or kwargs): args = (default_message,)

         # Call super constructor
         super().__init__(*args, **kwargs)
