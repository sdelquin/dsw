# Algo sobre ti 👋

1. ¿Qué lenguajes de programación has manejado?
2. ¿Dónde te ves al acabar el ciclo?
3. ¿Cuál dirías que es tu mayor virtud?
4. ¿Cuál es tu comida favorita? (_muy random_ 😜)

```python
import random

chat_done = set(int(n.strip()) for n in open('chat_done.dat'))
if not(chat_left := set(range(1, 31)) - chat_done):
    print('END❗')
else:
    pick = random.choice(list(chat_left))
    open('chat_done.dat', 'a').write(f'{pick}\n')
    print(f'Student #{pick}')
```
