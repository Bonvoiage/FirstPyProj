from mod1 import modul1
from mod1.func1 import func_module1

from mod1.mod2 import modul2
from mod1.mod2.func2 import func_module2

from mod1.mod2.mod3 import modul3
from mod1.mod2.mod3.func3 import func_module3


print('Импорт из глубокой директории модуля сидящего в корне проекта')
from mod1.mod2.mod3 import import_modul1


print('Импорт модулей из папок разной глубины вложенности')

func_module1()
func_module2()
func_module3()
