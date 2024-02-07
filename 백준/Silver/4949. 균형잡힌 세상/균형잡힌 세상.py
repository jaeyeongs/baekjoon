while True:
  a=input()
  s=[]
  if a==".":
    break
  flag=True
  for i in a:
    if a[0]==')' or a[0]==']':
      flag=False
      break
    if i=='(':
      s.append(')')
    elif i=='[':
      s.append(']')
    elif i==')':
      if len(s)==0 or s[-1]!=')':
        flag=False
        break
      s.pop()
    elif i==']':
      if len(s)==0 or s[-1]!=']':
        flag=False
        break
      s.pop()
  if len(s)==0 and flag==True:
    print("yes")
  else:
    print("no")