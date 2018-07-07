name = 'Alex'
if name == 'Ola':
    print('Hey Ola!')
elif name == 'Sabrina':
    print('Hey Sabrina!')
else:
    print('Hey anonymouse!')

volume = 26
# Change the volume if it's too loud or too quiet
#if volume < 20 or volume > 80:
#    print("That's better!")
if 20 <=volume < 30:
    print("It's nice for background music")
elif 40 <= volume <60:
    print("Perfect, I can hear all the details")
elif 60 <= volume < 80:
     print("Nice for parties")
elif 80 <= volume < 100:
    print("A bit loud!")
else:
    print("My ears are hurting! :(")
if volume < 20 or volume > 60:
    print("That's better!")

def hi(name):
    print('Hi ' + name + '!')

women = ['Ana', 'Caro', 'Juliane', 'Sabrina']
for name in women:
    hi(name)

for x in range(1, 5):
    print(x)
