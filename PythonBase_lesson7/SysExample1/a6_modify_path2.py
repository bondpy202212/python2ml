
import sys
import os.path

current_path = os.path.dirname( os.path.abspath(__file__))
parent_path = os.path.dirname( current_path )
#print(current_path)
#print()
#print(parent_path)
#print()


module_path = os.path.join(parent_path, 'PythonBase_lesson7')
#module_path = os.path.join('..', 'PythonBase_lesson7')
sys.path.append(module_path)
#print(sys.path)
#print(__file__)

import a1_def_fibonacci
print()
print(a1_def_fibonacci.nth_fibonacci(10))
print()

