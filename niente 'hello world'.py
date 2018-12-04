'''
Tefanso.
Questo è il mio primo programma, è una roba banale lo so, ma oltre all'ormai obbligatorio
'Hello world!', ho voluto creare un mini dialogo con i primi argomenti che ho trattato;
print, variabili,input,stringa, numeri interi e a virgola mobile (int, float).
'''

scelta = input('\nCiao sono Python!\nTu: ')
nome = input('\nPython: Come ti chiami?\nTu: ')
print('\nPython: OK ' + nome + '. Mi fa piacere conoscerti!')
print('\nPython: Inserisci due numeri per moltiplicarli tra loro.')
x = int(input('Primo numero: '))
y = int(input('Secondo numero: '))
print('Il risultato è', str(x * y))
print('Python: Ti ringrazio!')

'''
Nota: Nella variabile possono essere aggiunti solo numeri interi (int) altrimenti darà un errore.

Se si vuole insere un numere non intero quindi (float)
basta togliere dalla variabile x e y 'int' e inserire 'float' e sarà possibile inserire entrambi anche se un numero intero lo darà con virgola es: 21.0.

'''
