# Task 4.7*

# Run the module modules/mod_a.py . Check its result. Explain why does this happen.

## Sequencing

1. Сreated a module **mod_c.py** and a global variable **c**.
2. Assigned a value to variable **5**.
3. Сreated a module **mod_b.py** and a global variable **c**
4. Called module **mod_c.py** inside and changed the value of the variable  to **42**.
5. Сreated a module **mod_a.py**.
6. Called module **mod_c.py** and **mod_b.py** inside.
7.  Printed the value of the variable and got **42**.

## Explanation

In the **mod_a.py** file, we connect two modules, one of which calls the **mod_a.py** module in itself and changes the value of the variable, which is why we get **42** at the output.

```python

import mod_c
import mod_b

print(mod_c.x)

```

If we leave the code like this, we get the result **5**:

```python

import mod_c
#import mod_b

print(mod_c.x)

```