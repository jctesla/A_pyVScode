# love='ILoveFinxter';print('n'.join([''.join([(love[(x-y)%len(love)] if ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3<=0 else' ') for x in range(-30,30 )]) for y in range(15, -15, -1)]))
love='ILoveFinxter'
corazon = 'n'.join([''.join([(love[(x-y)%len(love)] if ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3<=0 else' ') for x in range(-30,30 )]) for y in range(15, -15, -1)])
print('type = ',type(corazon))
print(corazon)

f=open('corazon_ascii.txt', 'w')
space = ""
for i in corazon:
  if i==chr(10):
    f.writelines(space + chr(10) + chr(13) )      # + '\n\r''
    space=""
  space += i
f.close()

