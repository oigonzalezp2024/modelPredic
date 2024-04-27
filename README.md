
# ModelPredic 
Marco básico de aprendizaje de redes neuronales
en programación orientada a objetos.

## Documentación técnica

### Configuración del entorno de desarrollo.
| Paso   | Descripción                       | comando                             |
| :----  | :----                             | :---                                |
| Paso 1 |  Crear el entorno de trabajo.     | python -m venv env                  |
| Paso 2 | Activar el entorno de trabajo.    | ./env/Scripts/activate              |
| Paso 3 | Actualizar el gestor de paquetes. | python -m pip install --upgrade pip |
| Paso 4 | Prepare la receta de librerías.   | pip install -r requirements.txt     |

### Librerías del proyecto.
| librería | Descripción | Comando |
| :----    | :---        | :---    |
| tensorflow | Permite trabajar con redes neuronales | pip install tensorflow |
| matplotlib | Permite usar graficos de lineas       | pip install matplotlib |

### Demo
El modo de uso es bastante simple, la única recomendación por ahora, es respetar la ubicación de los archivos. 
```python
from modelPredic import ModelPredic

redNeuronal = ModelPredic()
redNeuronal.setDataX([-40, -10, 0, 8, 15, 22, 38])
redNeuronal.setDataY([-40, 14, 32, 46, 59, 72, 100])
redNeuronal.setX(100.0)
redNeuronal.modelPredict()
prediction = redNeuronal.getOutput()
print(prediction)
```
Resultado:
```CMD
{
    "output": "211.7478"
}
```

### Realice sus pruebas, actualizaciones o modificaciones.
Puedes actualizar, contribuir y mejorar el presente software, es libre. Licencia GNU v3.  
No esta permitido modificar la licencia de trabajos derivados de este proyecto.  
Por norma internacional debes conservar el mismo tipo de licencia.

#### Actualizar la receta.

Si agregas nuevas librerías al proyecto, no olvides actualizar la receta.

``` CMD
pip freeze > requirements.txt
```

---

#### Comprobar que todo está en orden.
| Paso   | Descripción                                   | comando                               |
| :----  | :----                                         | :---                                  |
| Paso 1 | Desactive el entorno de trabajo.              | deactivate                            |
| Paso 2 | Elimine el entorno anterior.                  | rm -R env                             |
| Paso 3 | Cree un entorno de python.                    | python -m venv env                    |
| Paso 4 | Active el entorno de trabajo.                 | ./env/Scripts/activate                |
| Paso 5 | Actualice el gestor de paquetes.              | python -m pip install --upgrade pip   |
| Paso 6 | Instale las librerías necesarias para operar. | pip install -r requirements.txt       |
| Paso 7 | Realice pruebas de rutina.                    | py demo.py |
| Paso 8 | Finalice su gestión.                          | deactivate                            |

