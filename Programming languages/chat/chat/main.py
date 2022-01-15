import lexer as lexyboii
import worker as workyboii
with open("Demo.cht", 'r') as f:
    code=f.readlines()
workyboii.workofy(lexyboii.lexofy(code), {})