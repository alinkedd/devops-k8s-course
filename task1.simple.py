import base64

steps = ["plan", "code", "test", "delivery", "deploy", "monitor"]

for step in steps:
  print(base64.b64encode(step.encode('utf-8')))
