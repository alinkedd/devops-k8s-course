import sys # NOTE: no sys in the course environment!
import base64

def str_to_base64(s: str) -> bytes:
  return base64.b64encode(s.encode('utf-8'))

# Simple positive test. In case of success, nothing will be logged,
# otherwise AssertionError will be raised
def test():
  msg = "<plan> should be encoded into <b'cGxhbg=='>"
  assert str_to_base64('plan') == b'cGxhbg==', msg

def main():
  steps = ["plan", "code", "test", "delivery", "deploy", "monitor"]

  for step in steps:
    print(str_to_base64(step))

if __name__ == '__main__':
  if ('--test' in sys.argv):
    test()
  else:
    main()
