# **CLIPPy**
## **Clasificación de Imágen-Texto con CLIP en Python**

***GITHUB [CLIPPy](https://github.com/Alden1320/clippy)***

CLIPPy es una web app que mediante un servidor Flask en Python sirve a un Frontend en HTML para realizar una CLASIFICACIÓN DE IMÁGENES contrastándolas contra uno o más términos. Para realizar la inferencia se utiliza el modelo de código abierto de OPENAI llamado [CLIP VIT](https://github.com/openai/CLIP.git)

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
### **INSTALACIÓN**
#### **ACTUALIZACIÓN DE SERVIDOR**
Empezamos por actualizar el repositorio de paquetes de Ubuntu

```linux
    sudo apt update
```

Actualizamos todo desde el repositorio de paquetes de Ubuntu

```linux
    sudo apt upgrade -y
```

#### **ACTUALIZACIÓN DE PYTHON**
Actualizamos Python

```linux
    sudo apt install python3-full
```

#### **INSTALACIÓN DE NGINX**  
Instalamos el servidor NGINX

```linux
    apt install nginx
```

[Creamos un bloque de servidor](https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-ubuntu-18-04) y asignamos permisos

```linux
    sudo mkdir -p /var/www/alluxion.com/html
    sudo chown -R $USER:$USER /var/www/alluxion.com/html
    sudo chmod -R 755 /var/www/alluxion.com
```

#### **INSTALACIÓN DE PIP**
Instalamos el gestor de paquetes de Python, pip

```linux
    sudo apt install python3-pip
```

#### **INSTALACIÓN DE FLASK Y GUNICORN**
Instalamos Flask y Gunicorn

```linux
    pip install wheel flask gunicorn
```

#### **CONFIGURACIÓN DE NGINX PARA SERVIR LA APLICACIÓN FLASK**
Creamos un bloque de servidor para alluxion.com y creamos un enlace simbólico a sites-enabled

```linux
    sudo nano /etc/nginx/sites-available/alluxion.com
```

En este archivo, agregamos la siguiente configuración:

```nginx
server {
    listen 80;
    listen [::]:80;

    root /var/www/alluxion.com/html;
    index index.html index.htm index.nginx-debian.html;

    server_name alluxion.com www.alluxion.com;

    location / {
        try_files $uri $uri/ =404;
    }

    location /clippy {
        proxy_pass http://0.0.0.0:8000/;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;    
    }
}
```

Guardamos y cerramos el archivo, luego creamos el enlace simbólico:

```linux
    sudo ln -s /etc/nginx/sites-available/alluxion.com /etc/nginx/sites-enabled/
```

#### **CREACIÓN DE LA APLICACIÓN FLASK**
Creamos un archivo hello.py en /var/www/alluxion.com/html/clippy con el siguiente contenido:

```python
from flask import Flask, send_from_directory
app = Flask(__name__)

@app.route("/")
def hello():
    return send_from_directory('/var/www/alluxion.com/html/clippy/content', 'index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0')
```

#### **CREACIÓN DEL ARCHIVO WSGI**
Creamos un archivo wsgi.py en /var/www/alluxion.com/html/clippy con el siguiente contenido:

```python
from hello import app

if __name__=="__main__":
    app.run()
```

#### **INICIO DE LA APLICACIÓN FLASK CON GUNICORN**
Iniciamos la aplicación Flask con Gunicorn

```linux
    cd /var/www/alluxion.com/html/clippy
    gunicorn --bind 0.0.0.0:8000 wsgi:app
```

#### **REINICIO DE NGINX**
Finalmente, reiniciamos Nginx para que los cambios surtan efecto

```linux
    sudo systemctl restart nginx
```

#### **CREACIÓN DE LA CARPETA DE CONTENIDO Y ARCHIVO INDEX.HTML**
Creamos la carpeta de contenido y el archivo index.html en /var/www/alluxion.com/html/clippy/content

```linux
    mkdir -p /var/www/alluxion.com/html/clippy/content
    echo "Hello World!" > /var/www/alluxion.com/html/clippy/content/index.html
```

#### **INSTALACIÓN DE ANACONDA**  
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

#### **INSTALACIÓN DE PYTORCH**
Instalamos Pytorch a través de ANACONDA

```linux
    conda install pytorch torchvision torchaudio cpuonly -c pytorch
```