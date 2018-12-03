print('''
++++++++++++++++++++++++++++++++++++++++++++++++++
+     Benvenuto nella calcolatrice creata da     +
+                  -Tefanso97-                   +
+ Scegli un dei numeri associati all'operazione. +
++++++++++++++++++++++++++++++++++++++++++++++++++
+                                                +
+              - Per uscire, ESC;                +
+              - Addizione, 1;                   +
+              - Sottrazione, 2;                 +
+              - Moltiplicazione, 3;             +
+              - Elevazione, 4;                  +
+              - Quoziente, 5;                   +
+                                                +
++++++++++++++++++++++++++++++++++++++++++++++++++''')

while True:
    associa = input('Inserisci il numero dell\'operazione che vuoi svolgere \n-> ')
    if associa == '1':
        print('\nHai scelto di Addizionare\n')
        x = float(input('Inserisci il primo numero -> '))
        y = float(input('Inserisci il secondo numero -> '))
        print('Il risultato è: ' + str(x + y))
    elif associa == '2':
        print('\nHai scelto di Sottrarre\n')
        x = float(input('Inserisci il primo numero -> '))
        y = float(input('Inserisci il secondo numero -> '))
        print('Il risultato è: ' + str(x - y))
    elif associa == '3':
        print('\nHai scelto di Moltiplicare\n')
        x = float(input('Inserisci il primo numero -> '))
        y = float(input('Inserisci il secondo numero -> '))
        print('Il risultato è: ' + str(x * y))
    elif associa == '4':
        print('\nHai scelto di Elevare\n')
        x = float(input('Inserisci il primo numero -> '))
        y = float(input('Inserisci il secondo numero -> '))
        print('Il risultato è: ' + str(x ** y))
    elif associa == '5':
        print('\nHai scelto il Quoziente\n')
        x = float(input('Inserisci il primo numero -> '))
        y = float(input('Inserisci il secondo numero -> '))
        print('Il risultato è: ' + str(x // y))
    elif associa == 'ESC'or associa == 'esc':
        print('\nProgramma è stato arrestato.\n')
        break
    elif associa > '5'or associa < '0':
        print('\nIl numero digitato non è valido.\nErrore!\n')
    elif ciclo != 'S' or ciclo != 's':
        print('\nErrore!!\n')
    elif ciclo != 'N' or ciclo != 'n':
        print('Errore!!')
        continue
    ciclo = input('\nVuoi continuare? S/N ')
    if ciclo == 'S' or ciclo == 's':
        print('Torno al menù di scelta.')
    elif ciclo == 'N' or ciclo == 'n':
        print('\nOk!\n')
        break


'''
Il sorgente è stato aggiornato il 30/11/2018 - 13:53.
Implementazione: Adesso quando se si decide di uscire dal programma, invece di tornare al menù di scelta, stamparà (OK!) e chiuderà il programma.
Inoltre è stato modificato l'errore del carattere non uguale a (S, s -N, n).
'''
