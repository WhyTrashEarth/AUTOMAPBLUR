# AutoMapBlur para OBS Studio

AutoMapBlur te permite aplicar automáticamente un efecto de desenfoque en tu captura de juego cada vez que se abre el mapa del juego, protegiendo información sensible y previniendo el stream sniping.

## Funcionalidades
- **Desenfoque Automático:** Presiona la tecla del mapa (por defecto: "M") para activar o desactivar el desenfoque en tu captura de juego en OBS.
- **Tecla Personalizable:** Puedes personalizar la tecla utilizada para activar el desenfoque.
- **Intensidad del Desenfoque Ajustable:** Modifica la intensidad del desenfoque según tus preferencias, de 1 (desenfoque ligero) a 20 (desenfoque fuerte).

## Instrucciones de Instalación

### Paso 1: Añadir el Script a OBS
1. Descarga el script `AutoMapBlur_OBS.py`.
2. En OBS Studio, ve a **Herramientas > Scripts**.
3. Haz clic en el botón **+** y busca el archivo `AutoMapBlur_OBS.py` en tus descargas.
4. Una vez añadido, el script aparecerá en la ventana de Scripts.

### Paso 2: Configurar el Script
1. Selecciona la **fuente** en la que deseas aplicar el desenfoque (por ejemplo, captura de juego).
   - Verás un campo de texto llamado **Nombre de la Fuente (Source Name)** en el panel de propiedades del script.
2. Ajusta la **intensidad del desenfoque** a tu gusto.
   - Usa el control deslizante de **Intensidad del Desenfoque** para seleccionar un valor entre 1 y 20.
3. Configura la **tecla del mapa** (opcional).
   - Si deseas usar una tecla diferente a la predeterminada "M", introdúcela en el campo **Tecla del Mapa (Map Key)**.

### Paso 3: Comienza a Transmitir
1. Una vez configurado, AutoMapBlur activará automáticamente el efecto de desenfoque cuando presiones la tecla del mapa durante tu transmisión.
2. Presiona nuevamente la tecla del mapa para desactivar el desenfoque.

## Tablero de Proyectos
Mantente al día con el progreso y contribuye a través de nuestro [Tablero de Proyectos de AutoMapBlur](https://github.com/users/WhyTrashEarth/projects/1).

## Repositorio en GitHub
Encuentra el código fuente completo y detalles adicionales en nuestro [Repositorio de GitHub](https://github.com/WhyTrashEarth/AUTOMAPBLUR).

## Uso
- **Alternar Desenfoque:** Presiona la tecla del mapa para aplicar el efecto de desenfoque cuando el mapa del juego esté abierto. Presiona nuevamente para eliminar el desenfoque.
- **Personalización:** Puedes modificar tanto la intensidad del desenfoque como las teclas en el panel de Propiedades del Script en OBS.

## Solución de Problemas
- Asegúrate de que el **Nombre de la Fuente (Source Name)** coincida exactamente con el nombre de tu captura de juego o la fuente deseada en OBS.
- Si el efecto de desenfoque no se activa, verifica la configuración de la tecla o aumenta la intensidad del desenfoque.
- Si el script no funciona, intenta eliminarlo y volver a agregarlo en **Herramientas > Scripts**.

## Contribuciones
Si deseas contribuir o informar problemas, visita el [Repositorio de AutoMapBlur en GitHub](https://github.com/WhyTrashEarth/AUTOMAPBLUR).

## Créditos
AutoMapBlur fue conceptualizado por [@WhyTrashEarth](https://x.com/WhyTrashEarth) y desarrollado con el apoyo de la comunidad.

## Licencia
Este proyecto está licenciado bajo **CC0 1.0 Universal (Creative Commons Zero v1.0)** Public Domain Dedication. Siéntete libre de usar, modificar y distribuir esta herramienta como desees.
