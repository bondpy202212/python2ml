
import sys
import os.path

module_path = os.path.join('..', 'PythonBase_lesson7')
sys.path.append(module_path)
#print(sys.path)
print(__file__)
print(__name__)

import a1_def_fibonacci
print()
print(a1_def_fibonacci.nth_fibonacci(10))
print()

