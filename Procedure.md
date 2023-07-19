# **CLIPPy**
## **Clasificación de Imágen-Texto con CLIP en Python**

***GITHUB [CLIPPy](https://github.com/Alden1320/clippy)***

CLIPPy es una web app que mediante un servidor Flask en Python sirve a un Frontend en HTML para realizar una CLASIFICACIÓN DE IMÁGENES contrastándolas contra uno o más términos. Para realizar la inferencia se utiliza el modelo de código abierto de OPENAI llamado [CLIP VIT](https://github.com/openai/CLIP)

___
***CLIPPy*** *Developer* -   Alden Sathyananda Cecchetti Taboada
___

### ***CLIPPy v1.0 (19-07-2023)*** 

#### **REQUISITOS**

##### **-SERVIDOR-**

###### **a) HARDWARE**
Utilizaremos un servidor VPS:
- 8 _NÚCLEOS_
- 8 _GB RAM_

###### **b) SOFTWARE**
1. UBUNTU - LINUX - _22.04_
2. NGINX - _1.18.0_
3. ANACONDA - _23.5.2_
4. PYTHON - _FULL_ - _3.11.4_
5. PIP - _23.1.2_

###### **- DEPENDENCIAS -**
1. Flask - _2.2.5_
2. Flask-Cors - _4.0.0_
3. ftfy - _6.1.1_
4. pyngrok - _6.0.0_
5. regex - _2022.10.31_
6. tqdm - _4.65.0_
7. torchvision - _0.15.2_
8. gunicorn - _21.1.0_
9. [openai-clip](https://github.com/openai/CLIP.git)

___
### **PROCESO**
#### **INSTALACIÓN**
##### **SERVIDOR**
###### **ACTUALIZACIÓN DE SERVIDOR**
Empezamos por actualizar el repositorio de paquetes de Ubuntu

```linux
    sudo apt update
```

Actualizamos todo desde el repositorio de paquetes de Ubuntu

```linux
    sudo apt upgrade -y
```
###### **INSTALACIÓN DE PAQUETES**
**NGINX**
Instalamos el servidor NGINX

**ANACONDA**

Descargamos [Anaconda](https://www.anaconda.com/download)

```linux
    wget https://repo.anaconda.com/archive/Anaconda3-2023.07-1-Linux-x86_64.sh
```

Instalamos Anaconda

```linux
    bash https://repo.anaconda.com/archive/Anaconda3-2023.07-1-Linux-x86_64.sh
```

Creamos Entorno Clippy

```linux
    conda create --name clippy
```

Activamos el Entorno Clippy

```linux
    conda activate clippy
```

