#coding  utf-8

age = input('entrez votre age : ')
try :
  age = int(age)
except:
  print('l\'age est incorrect ')
else:
  print('vous avez {} ans'.format(age))
finally:
  print('le programme est terminer ')


bnre1 = 130
bnre2 = input('entrez un nombre pour diviser :')

while bnre2 <= 0 or bnre2 == '':
    bnre2 = input('entrez un nombre pour diviser :')
   if bnre2 > 0 :
     try:
        bnre2 = bnre1 / int(bnre2)
     except ZeroDivisionError:
        print('impossible de diviser par ')

