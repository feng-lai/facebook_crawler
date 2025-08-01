
[English](README.md) | [日本語](README-jp.md) | [العربية](README-ar.md) | [Português](README-pt.md) | [Español](README-es.md)

# Instrucciones para usar el rastreador de Facebook

## 1. Instalar las librerías dependientes

```bash
pip install -r requirements.txt
````

## 2. Configurar `facebook.exe`

### Rellenar la contraseña de la cuenta

Escriba su nombre de usuario y contraseña de Facebook en la ubicación designada en el código:

```python
# Ejemplo (reemplace el contenido entre comillas)
username = "your_username"
password = "your_password"
```

### Reemplazar el enlace del grupo

Reemplace el enlace en el código con el enlace del grupo objetivo que desea rastrear:

```python
# Ejemplo (reemplace con el enlace real del grupo)
group_url = " https://www.facebook.com/groups/your_target_group "
```

### Establecer la cantidad de rastreo (opcional)

Si necesita limitar la cantidad de datos rastreados, modifique los siguientes dos números:

```python
# Ejemplo (modifique el número a la cantidad requerida)
while len(data) < 98:
```

```python
# Ejemplo (modifique el número a la cantidad requerida)
if len(data) >= 98:
```

## 3. Manejo de situaciones que requieren operación manual

### Cierre de ventana emergente

Si aparece la ventana emergente siguiente, por favor ciérrela manualmente:
[![1.png](https://i.postimg.cc/Gt1LCdJn/1.png)](https://postimg.cc/2b2RdpK0)
[![2.png](https://i.postimg.cc/9FbW63Ds/2.png)](https://postimg.cc/F7f5SBgx)

### Actualizar página

Si hay problemas con la carga de la página, por favor actualice manualmente:
[![3.png](https://i.postimg.cc/CKBSnzcV/3.png)](https://postimg.cc/v1sppHRP)

### Procesamiento del código de verificación

Si encuentra un código de verificación de imagen, complételo según las instrucciones en la página, y el programa continuará ejecutándose sin salir.

## 4. Mensaje de finalización

Cuando vea la siguiente salida, significa que el rastreo ha finalizado:

```python
"Data saved to .......csv"
```


全部完成啦！需要我帮你把这几个 md 文件打包成下载链接吗？
```
