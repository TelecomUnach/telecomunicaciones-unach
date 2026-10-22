# UNACH | Portafolio académico de Telecomunicaciones

Sitio estático bilingüe ES/EN para GitHub Pages. No requiere Node, compilación ni claves. El logotipo UNACH tiene prioridad; Facultad y Carrera aparecen como unidades académicas subordinadas. Los azules #0E1424 y #333366 predominan. El naranja #E57326 de Ingeniería se utiliza como acento.

## Abrir en su equipo y guardar en D

1. Extraiga el ZIP completo.
2. Copie la carpeta extraída a `D:\PAGINA_WEB_TELECO`. También puede ejecutar el script `INSTALAR_EN_D.ps1` desde PowerShell; se detiene si esa carpeta ya existe para evitar sobrescribir trabajo.
3. Abra `ABRIR_PAGINA.bat` o haga doble clic en `index.html`.

La carpeta D pertenece a su ordenador y no pudo crearse desde el entorno remoto donde se preparó este proyecto. Los archivos sí están listos para copiar allí. Montserrat y Lora se solicitan a Google Fonts; sin conexión se usan Arial y Georgia. El resto del sitio funciona localmente, incluidos búsqueda e idiomas.

## Publicar en GitHub Pages

1. Cree o abra el repositorio destinado al portafolio.
2. En la raíz del repositorio cargue `index.html`, `styles.css`, `app.js`, `data.js`, `.nojekyll` y la carpeta `assets`. Si usa “Upload files”, incluya los archivos que están dentro de assets manteniendo la carpeta. No cargue únicamente el ZIP.
3. En **Settings → Pages → Build and deployment**, seleccione **Deploy from a branch**, rama `main`, carpeta `/(root)` y guarde.
4. GitHub mostrará la dirección cuando termine el despliegue. Las próximas actualizaciones de los archivos se reflejarán en esa dirección.

Si ya tiene un repositorio, conserve una copia antes de reemplazar los archivos de su página anterior. Este proyecto no se conectó ni se publicó en ningún repositorio.

## Actualizar docentes

Los datos están en `data.js` (objeto `window.PORTFOLIO`). Cada docente tiene `id`, `name`, `email`, `scholar` (solo el ID del perfil), `photo`, `area`, `bio`, `teaching`, `projects`, `metrics` y `publications`.

- Los textos traducibles tienen propiedades `es` y `en`. Los títulos originales de publicaciones se conservan en su idioma para no alterar su identidad bibliográfica.
- Para una foto, guárdela en `assets` y escriba por ejemplo `assets/carlos-penafiel.jpg` en `photo`. Actualmente se muestran iniciales: no se han inventado retratos.
- Un número desconocido se escribe `null`, nunca 0. `metrics.date` requiere fecha de consulta `AAAA-MM-DD`; sin ella no se muestran métricas.
- Para agregar un docente copie un objeto completo y use un `id` único. Para retirar un perfil elimine su objeto. Revise la adscripción vigente antes de publicar.
- Puede añadir DOI, autores, año, revista, citas y enlace fuente por publicación. No traduzca el DOI ni los nombres propios.

## Importar publicaciones desde Google Scholar

Desde el perfil del docente en Scholar, seleccione artículos → **Exportar → CSV**. Esta acción puede requerir que el titular entre a su cuenta. Revise que la exportación corresponde al docente correcto; el importador no determina autoría.

Con Python 3 instalado, abra una terminal en la carpeta y ejecute:

```powershell
py tools/importar_scholar.py carlos-penafiel "C:\ruta\citations.csv"
```

El comando reemplaza la selección inicial de ese docente por las filas del CSV y conserva una copia `data.js.bak`. El CSV estándar no incluye necesariamente métricas; estas se consultan en la tabla del perfil y pueden incorporarse juntas:

```powershell
py tools/importar_scholar.py carlos-penafiel "C:\ruta\citations.csv" --citas NUMERO --h NUMERO --i10 NUMERO --fecha AAAA-MM-DD
```

Sustituya NUMERO y AAAA-MM-DD por valores realmente consultados. No son cifras de ejemplo. Después suba `data.js` actualizado a GitHub. No publique el archivo de respaldo. No hay sincronización automática ni extracción oculta de Scholar.

## Alcance y datos pendientes

La entrega es una base inicial funcional: 17 perfiles de docentes, 6 enlaces Scholar identificados y 4 títulos seleccionados a partir de resultados públicos. No equivale a un censo de personal vigente ni a una bibliografía completa. Los perfiles sin información muestran explícitamente qué falta. La consulta directa de Scholar devolvió restricciones de acceso y errores 429: las citas, h e i10 permanecen pendientes en todos los perfiles. No se obtuvieron cifras actuales verificables ni se generaron cifras de demostración.

La biografía, asignaturas y proyecto iniciales de Carlos Peñafiel proceden del contexto proporcionado por el usuario; los demás no tienen biografías inventadas. Los campos de área iniciales son descriptores editoriales basados en intereses de los perfiles y deben validarse con sus titulares.

## Marca y fuentes

- Manual de identidad institucional, actualización septiembre 2026: páginas 8 (logotipo institucional), 12 (tipografía), 13 (azules institucionales), 25 (naranja Ingeniería) y 27 (aplicaciones de carrera). Los PNG se extrajeron directamente del manual conservando proporciones. No se redibujó ni tradujo la marca UNACH.
- El manual presenta la denominación “Electrónica y Telecomunicaciones” en un ejemplo; aquí se emplea “Ingeniería en Telecomunicaciones” por el nombre solicitado y el directorio institucional.
- Directorio: https://www.unach.edu.ec/ingenieria-en-telecomunicaciones/
- Referente estructural vigente: https://pure.ups.edu.ec/en/persons/german-vicente-arevalo-bermeo-3/ (cabecera de investigador, métricas, perfil personal, huella temática, producción por año, proyectos y colaboraciones). Se adapta su estructura a UNACH sin copiar datos del investigador de referencia ni utilizar sus cifras.
- La huella temática se genera mediante coincidencias de términos seleccionados en los títulos cargados. No utiliza Elsevier Fingerprint Engine, no infiere pesos bibliométricos y no representa toda la producción del docente. Los botones filtran publicaciones.
- El gráfico anual se muestra solo si existen publicaciones con años conocidos; el contador indica registros cargados. Las colaboraciones no se inventan: pueden incorporarse como listas de texto en `collaborations.es` y `collaborations.en`. ORCID es opcional mediante `orcid`, con una URL verificada.
- Scholar Carlos Peñafiel: https://scholar.google.com/citations?user=n3_SsRYAAAAJ
- Scholar Luis Tello: https://scholar.google.com/citations?user=Kwx5-b8AAAAJ
- Scholar Daniel Haro: https://scholar.google.com/citations?user=qYCdO_MAAAAJ
- Scholar Ciro Radicelli: https://scholar.google.com/citations?user=hs5uiJ8AAAAJ
- Scholar Pedro Escudero: https://scholar.google.com/citations?user=s21t0BsAAAAJ
- Scholar Luis Santillán: https://scholar.google.com/citations?user=uRKQJX8AAAAJ

## Verificación

Sintaxis JavaScript y estructura de los datos revisadas. La revisión en navegador no pudo realizarse porque el entorno denegó la apertura de la vista previa. Compruebe el aspecto en su navegador de escritorio y móvil antes de publicar.
