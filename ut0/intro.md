---
author: "DSW-2DAW"
date: "DD/MM/YYYY"
paging: "%d/%d"
---

# Algo sobre mi 👨‍💻

- Sergio Delgado Quintero.
- Estudié **Ingeniería Informática** en la _Universidad de La Laguna_.
- Casi 20 años programando (y enseñando) Python.
- Cofundador de https://pythoncanarias.es
- Muchos proyectos desarrollados 🏃‍♂️

## Contacto

- `sdelqui@gobiernodecanarias.org` ✉️
- 621 336 832 ☎️

---

# Desarrollo Web en entorno servidor (DSW)

- CFGS Desarrollo de Aplicaciones Web (DAW)
- 7 horas semanales
- Lenguaje de programación: **Python** 🐍
- Framework web: **Django** 🦄
- Aula virtual: https://peq.es/dsw
- Contenidos: https://aprendepython.es
- Máquina virtual: **VirtualBox**
- Marco legislativo: https://www.boe.es/buscar/act.php?id=BOE-A-2022-5139
- Ordenación: https://www.boe.es/diario_boe/txt.php?id=BOE-A-2023-13221
- Currículo: https://www.boe.es/diario_boe/txt.php?id=BOE-A-2010-17329
- ¡Programar es super divertido! ✌️

---

# Sistema de evaluación (1/2)

Por evaluación...

```
Pruebas objetivas [PO] (60%)
    Pruebas objetivas teóricas [POT] (25%)
    Pruebas objetivas prácticas [POP] (75%) 🔒
Tareas evaluables [TE] (40%) 👫
    Tareas evaluables: Investigación [TEI] (30%)
    Tareas evaluables: Proyectos [TEP] (70%)
```

**POP/TEI** → 70% TESTS + 30% CÓDIGO

---

# Sistema de evaluación (2/2)

Por curso...

|      | 1ªEV | 2ªEV | 3ªEV |
| ---- | ---- | ---- | ---- |
| 1ªEV | 100% | -    | -    |
| 2ªEV | 30%  | 70%  | -    |

---

# Resultados de aprendizaje (1/2)

- **RA1**: Selecciona las arquitecturas y tecnologías de programación web en entorno servidor, analizando sus capacidades y características propias.
- **RA2**: Escribe sentencias ejecutables por un servidor web reconociendo y aplicando procedimientos de integración del código en lenguajes de marcas.
- **RA3**: Escribe bloques de sentencias embebidos en lenguajes de marcas, seleccionando y utilizando las estructuras de programación.
- **RA4**: Desarrolla aplicaciones web embebidas en lenguajes de marcas analizando e incorporando funcionalidades según especificaciones.
- **RA5**: Desarrolla aplicaciones web identificando y aplicando mecanismos para separar el código de presentación de la lógica de negocio.

---

# Resultados de aprendizaje (2/2)

- **RA6**: Desarrolla aplicaciones web de acceso a almacenes de datos, aplicando medidas para mantener la seguridad y la integridad de la información.
- **RA7**: Desarrolla servicios web reutilizables y accesibles mediante protocolos web, verificando su funcionamiento.
- **RA8**: Genera páginas web dinámicas analizando y utilizando tecnologías y frameworks del servidor web que añadan código al lenguaje de marcas.
- **RA9**: Desarrolla aplicaciones web híbridas seleccionando y utilizando tecnologías, frameworks servidor y repositorios heterogéneos de información.

---

# Unidades de trabajo

- **UT1**: Introducción a la programación web.
- **UT2**: Django básico.
- **UT3**: Django intermedio.
- **UT4**: Django avanzado.
- **UT5**: Django especializado.

---

# Relación UT/RA

|     | UT1 | UT2  | UT3 | UT4  | UT5  |
| --- | --- | ---- | --- | ---- | ---- |
| RA1 | 90% | 10%  |     |      |      |
| RA2 |     | 100% |     |      |      |
| RA3 |     | 20%  | 30% | 40%  | 10%  |
| RA4 |     |      | 30% | 40%  | 30%  |
| RA5 |     |      | 40% | 40%  | 20%  |
| RA6 |     | 15%  | 25% | 30%  | 30%  |
| RA7 |     |      |     |      | 100% |
| RA8 |     |      |     | 100% |      |
| RA9 |     |      |     |      | 100% |

---

# Material

**Material obligatorio:**

- Cuaderno 📔
- Bolígrafo ✍️
- Disco duro externo USB 💾

---

# Horario

|               | L   | M   | X   | J   | V   |
| ------------- | --- | --- | --- | --- | --- |
| 14:30 - 15:25 | DSW | DSW |     |     | DSW |
| 15:25 - 16:20 | DSW | DSW |     |     | DSW |
| 16:20 - 17:15 |     |     |     |     |     |
| 17:15 - 17:45 | === | === | === | === | === |
| 17:45 - 18:40 |     |     | DSW |     |     |
| 18:40 - 19:35 |     |     |     |     |     |
| 19:35 - 20:30 |     |     |     |     |     |

---

# Respeta y valora

- **Respeta y valora** a tu profe.
- **Respeta y valora** a tus compañeros/as.
- **Respeta y valora** el material que se te ha dado.
- **Respeta y valora** lo que aprendes.
- **Respeta y valora** lo que escuchas.
- **Respeta y valora** lo que haces/dices.

---

# Algo sobre ti 👋

1. ¿Qué lenguajes de programación has manejado?
2. ¿Dónde te ves al acabar el ciclo?
3. ¿Cuál es tu hobby?
4. ¿Cuál es tu artista/grupo favorito de música?
5. ¿Cómo quieres que te llamen?

---

# ¡Te toca!

```python
import random

intro_done = set(int(n.strip()) for n in open('intro_done.dat'))
if not(intro_left := set(range(1, 31)) - intro_done):
    print('END❗')
else:
    pick = random.choice(list(intro_left))
    open('intro_done.dat', 'a').write(f'{pick}\n')
    print(f'👉 Student #{pick}')
```
