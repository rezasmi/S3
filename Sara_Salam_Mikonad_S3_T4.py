a=input()
a=a.lower()
if 'h'in a and 'e' in a and 'l' in a and 'o' in a:
    vaziat=True
else:
    vaziat=False
h=a.find('h')
e=a.find('e')
l=a.find('l')
o=a.find('o')
if vaziat==True and h < e and e<l and l<o:
    vaziat='YES'
else:
    vaziat='NO'
print(vaziat)