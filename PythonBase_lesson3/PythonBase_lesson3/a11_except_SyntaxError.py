
#eval('@#$ + 6')
#exec('prnt("456")')

try:
    eval('@#$+ 6')    
except SyntaxError:
    print('syntax error')
    
