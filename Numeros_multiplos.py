a, b = input().split()
a = int(a)
b = int(b)
#if (a + b) % 2 == 0:   #São as duas formas de se fazer. 
if a % b == 0 or b % a == 0:
    print('Sao Multiplos')
else:
    print('Nao são Multiplos')


