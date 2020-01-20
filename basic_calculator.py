def calculator(num1, operator, num2):
   if operator == '/' and num2  == 0:
       return "Cant devide by 0!"
   return eval('num1' + operator + 'num2')