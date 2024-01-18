p = '/Users/blackwings/Downloads/com.blackwings.autotouch_8.0.11_iphoneos-arm64e'

import os
for root, _, files in os.walk(p):
   for name in files:
       fn = os.path.join(root, name)
       if fn.endswith('.DS_Store'):
           print(fn)
           os.remove(fn)
   # for name in dirs:
   #    print(os.path.join(root, name))