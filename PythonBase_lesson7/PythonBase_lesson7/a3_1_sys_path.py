
import sys
import os.path

m_path = os.path.join('..', 'le')
print(str(sys.path))
sys.path.append(m_path)
print()
print(str(sys.path))
print()

print(__name__)
print(__file__)
print()

print('1 ---')
print(os.path.dirname(__file__))
print('2 ---')
print(os.path.basename(__file__))
print('3 ---')
print(os.path.abspath(__file__))
print()