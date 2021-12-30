import base64

import pytest

# message = 'tokopedia789'
# message_bytes = message.encode('ascii')
# base64_bytest = base64.b64encode(message_bytes)
# base64_message = base64_bytest.decode('ascii')

message = 'dG9rb3BlZGlhNzg5'
message_bytes = message.encode('ascii')
base64_bytest = base64.b64decode(message_bytes)
base64_message = base64_bytest.decode('ascii')

print(base64_message)