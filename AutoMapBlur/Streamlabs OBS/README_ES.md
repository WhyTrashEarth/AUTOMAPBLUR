# AutoMapBlur para Streamlabs OBS

AutoMapBlur te permite aplicar automáticamente un efecto de desenfoque en tu captura de juego cada vez que se abre el mapa del juego, protegiendo la información sensible y evitando el stream sniping.

## Funcionalidades
- **Alternar Desenfoque:** Presiona la tecla del mapa (predeterminada: "M") para activar o desactivar el desenfoque en tu captura de juego en Streamlabs OBS.
- **Tecla Personalizable:** Puedes personalizar la tecla utilizada para activar el desenfoque.
- **Intensidad del Desenfoque Ajustable:** Modifica la intensidad del desenfoque según tus preferencias, de 1 (desenfoque ligero) a 20 (desenfoque fuerte).

## Instrucciones de Instalación

### Paso 1: Configurar WebSocket en Streamlabs OBS
1. Asegúrate de que **WebSocket** esté habilitado en Streamlabs OBS.
   - Ve a **Configuración > Control Remoto** y habilita WebSocket.
   - Establece una contraseña para el WebSocket (la necesitarás para conectar el script).

### Paso 2: Añadir el Script a Streamlabs OBS
1. Descarga el script `AutoMapBlur_Streamlabs.py`.
2. En Streamlabs OBS, ve a **Herramientas > Scripts**.
3. Haz clic en el botón **+** y selecciona el archivo `AutoMapBlur_Streamlabs.py` desde tus descargas.
4. Una vez añadido, el script aparecerá en la ventana de Scripts.

### Paso 3: Configurar el Script
1. Selecciona la **fuente** a la que deseas aplicar el desenfoque (por ejemplo, captura de juego).
   - En el panel de configuración del script, encontrarás un campo de texto llamado **Nombre de la Fuente**.
2. Ajusta la **intensidad del desenfoque** según tu preferencia.
   - Utiliza el control deslizante de **Intensidad del Desenfoque** para elegir un valor entre 1 y 20.
3. Configura la **Tecla del Mapa** (opcional).
   - Si deseas usar una tecla diferente a la predeterminada "M", ingrésala en el campo **Tecla del Mapa**.

### Paso 4: Comienza a Transmitir
1. Una vez configurado, AutoMapBlur activará automáticamente el efecto de desenfoque cuando presiones la tecla del mapa durante tu transmisión.
2. Presiona la tecla del mapa nuevamente para eliminar el desenfoque.

## Tablero de Proyectos
Sigue nuestro progreso y contribuye a través de nuestro [Tablero de Proyectos de AutoMapBlur](https://github.com/users/WhyTrashEarth/projects/1).

## Repositorio en GitHub
Encuentra el código fuente completo y más detalles en nuestro [Repositorio de GitHub](https://github.com/WhyTrashEarth/AUTOMAPBLUR).

## Uso
- **Alternar Desenfoque:** Presiona la tecla del mapa para aplicar el efecto de desenfoque cuando el mapa del juego esté abierto. Presiona nuevamente para quitar el desenfoque.
- **Personalización:** Puedes modificar la intensidad del desenfoque y las teclas en el panel de configuración del script en Streamlabs OBS.

## Solución de Problemas
- Asegúrate de que el **Nombre de la Fuente** coincida exactamente con el nombre de tu captura de juego o la fuente deseada en Streamlabs OBS.
- Si el efecto de desenfoque no se activa, verifica la configuración de la tecla o aumenta la intensidad del desenfoque.
- Si el script no funciona, intenta eliminarlo y agregarlo nuevamente en **Herramientas > Scripts**.

## Contribuciones
Si deseas contribuir o informar problemas, visita el [Repositorio de AutoMapBlur en GitHub](https://github.com/WhyTrashEarth/AUTOMAPBLUR).

## Créditos
AutoMapBlur fue conceptualizado por [@WhyTrashEarth](https://x.com/WhyTrashEarth) y desarrollado con el apoyo de la comunidad.

## Licencia
Este proyecto está bajo la licencia **CC0 1.0 Universal (Creative Commons Zero v1.0)** Public Domain Dedication. Siéntete libre de usar, modificar y distribuir esta herramienta.
