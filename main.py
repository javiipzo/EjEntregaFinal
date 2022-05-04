# Importar módulo de tiempo
import time
import random
# Importar módulo de hilo
from threading import Thread
# Importar módulo de cola
from queue import Queue
# Crear cola
q = Queue(10)  # Producción inicial de bollos del chef
maxBollos=random.randint(1,100)
# Definir productor
def producer(name):
    count = 1  # Cuenta los bollos producidos
    # Siempre produce bollos
    parar=True
  
    while parar:
        q.join() # join esperará aquí hasta que task_done () envíe una señal, luego suelte
        q.put(count)
        print('Producer %  s está produciendo el% d bollo'%(name,count))
        count+=1
        time.sleep(0.1)
        if(count==maxBollos):
          q.join() # join esperará aquí hasta que task_done () envíe una señal, luego suelte
          q.put(count)
          print('Producer %  s está produciendo el% d bollo'%(name,count))
          count+=1
          time.sleep(0.1)
          parar=False
        
# Definir consumidor
def customer(name):
    count = 1 # Cuenta los bollos comidos por los consumidores
    # Sigue recibiendo bollos
    parar=True
    while parar:
        bao_zi = q.get() # Consigue los bollos en la cola del chef
        print('El consumidor %  s está comiendo el bollo% d'%(name,bao_zi))
        count +=1
        q.task_done() # Pon y consigue una vez, envía una señal para unirte después de tomar el bollo
        time.sleep(0.1)
        if(count==maxBollos):
          bao_zi = q.get() # Consigue los bollos en la cola del chef
          print('El consumidor %  s está comiendo el bollo% d'%(name,bao_zi))
          print('El consumidor esta lleno')
          #print('El consumidor % s esta lleno y no puede más '%(name,bao_zi))
          count +=1
          parar=False

if __name__ == '__main__':
    # Establecer hilo t1
    
    t1 = Thread(target=producer,args=('Master Chef Liu',))
    # Establecer hilo t2
    t2 = Thread(target=customer,args=('Cuihua',))
    # Iniciar hilo
    t1.start()
    t2.start()