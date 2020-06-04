# Snake-Game

I have tried to create my first game using python but unfortunately am stuck with a problem which i am not able to ovecome.
The problem is whenever i run the code the game starts but after when the snake eats its 2nd food a error appears.
i am unable to solve this>

Can anyone help???

The error is
[Running] python -u "f:\Linux\Programs\Python\snake_game.py"
Traceback (most recent call last):
  File "f:\Linux\Programs\Python\snake_game.py", line 97, in <module>
    wn.update()
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.8_3.8.1008.0_x64__qbz5n2kfra8p0\lib\turtle.py", line 1304, in update
    t._drawturtle()
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.8_3.8.1008.0_x64__qbz5n2kfra8p0\lib\turtle.py", line 3008, in _drawturtle
    shape = self._polytrafo(self._getshapepoly(tshape))
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.8_3.8.1008.0_x64__qbz5n2kfra8p0\lib\turtle.py", line 2961, in _polytrafo
    return [(p0+(e1*x+e0*y)/screen.xscale, p1+(-e0*x+e1*y)/screen.yscale)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.8_3.8.1008.0_x64__qbz5n2kfra8p0\lib\turtle.py", line 2961, in <listcomp>
    return [(p0+(e1*x+e0*y)/screen.xscale, p1+(-e0*x+e1*y)/screen.yscale)
TypeError: unsupported operand type(s) for +: 'method' and 'float'

[Done] exited with code=1 in 9.75 seconds

.
.
.
.

.
.
.
.
.
. 
Please do comment.
