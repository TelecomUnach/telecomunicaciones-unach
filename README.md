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

## Listados de publicaciones de Google Scholar

Actualización del 22 de octubre de 2026. Se consultaron directamente en navegador los **11 perfiles enlazados en el Excel**, pulsando “Mostrar más” hasta que quedó deshabilitado. Se recuperaron **398 filas** y se agruparon las repeticiones exactas de título normalizado y año. Se conservan todos los enlaces de las entradas agrupadas en `scholarUrls`; las citas de versiones duplicadas no se suman.

Los títulos originales, autores visibles, año, medio y enlace de cada registro están en `data.js`. Se preservan los puntos suspensivos de los metadatos que Scholar presenta truncados. También se actualizaron las citas, h e i10 a partir de la tabla total visible de cada uno de los 11 perfiles, con fecha de consulta. Las cifras de los listados individuales no se usan para recalcular los índices del autor.

Las listas de Scholar pueden contener artículos, congresos, libros, tesis y otros registros; la presencia en un perfil no verifica por sí sola el tipo documental ni la revisión por pares. Los registros sin clasificación editorial corroborada se identifican como “Registros de Scholar”. Cuando una obra ya tenía DOI verificado, se conservó. Se mantuvieron como complementos editoriales las obras documentadas que no estaban en el listado del perfil.

Para los otros 10 docentes se buscaron perfiles públicos por nombre sin localizar un resultado verificable. Se mantienen sus obras verificadas y se agregan coautorías identificables en los listados consultados, sin inventar perfiles ni inferir que carecen de producción. Carmen Cobeña y Diego Ricaurte siguen sin bibliografía verificable incorporada. El listado de quienes no tienen enlace continúa siendo parcial.

Los 21 perfiles contienen **433 asociaciones de títulos a docentes** tras la incorporación de coautorías y complementos. El número no es un total de obras únicas de la carrera: una publicación compartida aparece en cada ficha correspondiente. El archivo `REVISION_PERFILES.md` detalla la cobertura por docente y los perfiles pendientes.

**ORCID confirmados por el usuario:** Luis Gonzalo Santillán: 0000-0002-4020-5110; José Luis Jínez: 0000-0002-4113-0579; Klever Torres: sin ORCID. Esta confirmación prevalece sobre las asociaciones contradictorias del Excel y de fuentes editoriales. No se modificó el Excel original.

## Pure, Scopus y Elsevier Fingerprint Engine

La estructura de referencia vigente es el perfil de Victor Herrera en el portal USFQ. **Este sitio es una implementación independiente para GitHub Pages; no es una instalación de Pure.** El pie enlaza los recursos solicitados sin afirmar que Elsevier desarrolla u opera esta página.

- **Pure:** campo opcional `pure` para la URL institucional del investigador. Para sincronizar se requiere una instancia y acceso institucional autorizados, que no se proporcionaron en esta sesión.
- **Scopus:** campo `scopus` para la URL del autor. Se enlazó el identificador de Luis Tello localizado en su ORCID. Las métricas de Scopus no se mezclan con las de Scholar. El acceso API depende de la habilitación institucional; una clave por sí sola no concede derechos de acceso.
- **Elsevier Fingerprint Engine:** la huella actual es local, basada en términos de los títulos cargados. Puede mostrarse una exportación autorizada del motor mediante `fingerprint.provider`, `fingerprint.source`, `fingerprint.date` y `fingerprint.terms` (etiquetas `label`). No se ha conectado ni ejecutado el motor comercial.

### Importar datos autorizados

`tools/importar_exportacion.py` permite importar un JSON normalizado de un export institucional de Pure, Scopus, ORCID o Fingerprint. No llama a servicios externos ni acepta credenciales; no convierte una instalación estática en Pure.

```powershell
py tools/importar_exportacion.py ID_DOCENTE "C:\ruta\exportacion_normalizada.json"
```

El JSON debe contener `provider` (Pure, Scopus, ORCID o Elsevier Fingerprint Engine), `source` (URL HTTPS verificable) y `date` (AAAA-MM-DD). Puede incluir `publications` con títulos y metadatos, `scopus`/`pure` con URLs, y `fingerprint.terms` con etiquetas. Si incorpora `orcid`, debe coincidir con el del perfil. El archivo de exportación debe corresponder al docente seleccionado; revise la autoría antes de importar. Las exportaciones JSON nativas de cada proveedor necesitan normalizarse a esta estructura; el script no interpreta todos los esquemas propietarios.

El importador conserva copia de seguridad. Las citas de otros proveedores se guardan por separado (`providerCitations` y `externalMetrics`) para no presentarlas como Scholar. Nunca guarde claves, tokens o contraseñas en los archivos que publica en GitHub.

## Marca y fuentes

- Manual de identidad institucional, actualización septiembre 2026: páginas 8 (logotipo institucional), 12 (tipografía), 13 (azules institucionales), 25 (naranja Ingeniería) y 27 (aplicaciones de carrera). Los PNG se extrajeron directamente del manual conservando proporciones. No se redibujó ni tradujo la marca UNACH.
- El manual presenta la denominación “Electrónica y Telecomunicaciones” en un ejemplo; aquí se emplea “Ingeniería en Telecomunicaciones” por el nombre solicitado y el directorio institucional.
- Directorio: https://www.unach.edu.ec/ingenieria-en-telecomunicaciones/
- Referente estructural vigente: https://research.usfq.edu.ec/es/persons/victor-herrera/ (cabecera de investigador, métricas, perfil personal, huella temática, producción por año, proyectos y colaboraciones). Se adapta su estructura a UNACH sin copiar datos del investigador de referencia ni utilizar sus cifras.
- La huella temática se genera mediante coincidencias de términos seleccionados en los títulos cargados. No utiliza Elsevier Fingerprint Engine, no infiere pesos bibliométricos y no representa toda la producción del docente. Los botones filtran publicaciones.
- El gráfico anual se muestra solo si existen publicaciones con años conocidos; el contador indica registros cargados. Las colaboraciones no se inventan: pueden incorporarse como listas de texto en `collaborations.es` y `collaborations.en`. ORCID es opcional mediante `orcid`, con una URL verificada.
- Scholar Carlos Peñafiel: https://scholar.google.com/citations?user=n3_SsRYAAAAJ
- Scholar Luis Tello: https://scholar.google.com/citations?user=Kwx5-b8AAAAJ
- Scholar Daniel Haro: https://scholar.google.com/citations?user=qYCdO_MAAAAJ
- Scholar Ciro Radicelli: https://scholar.google.com/citations?user=hs5uiJ8AAAAJ
- Scholar Pedro Escudero: https://scholar.google.com/citations?user=s21t0BsAAAAJ
- Scholar Luis Santillán: https://scholar.google.com/citations?user=uRKQJX8AAAAJ

## Verificación

Sintaxis JavaScript y estructura de los datos revisadas. Se comprobaron los 21 perfiles en ambos idiomas, búsqueda, filtro de 11 Scholar, coautorías, fuentes y rechazo de importaciones con un ORCID diferente. La revisión en navegador no pudo realizarse porque el entorno denegó la apertura de la vista previa. Compruebe el aspecto en su navegador de escritorio y móvil antes de publicar.

## Navegación por pestañas

Se añadieron ocho secciones bilingües: La carrera; Formación y objetivos; Campo profesional; Titulación; Malla curricular; Prácticas y vinculación; Docentes; Investigación. La página inicial abre La carrera. Las rutas `#seccion/...` se pueden copiar y compartir; el navegador permite regresar y avanzar entre ellas.

Las síntesis académicas proceden de https://www.unach.edu.ec/ingenieria-en-telecomunicaciones/ (consulta 22/10/2026). Los requisitos de titulación se presentan como información publicada; confirme procedimientos aplicables a cada cohorte con la Dirección. La traducción al inglés es informativa. Se enlaza directamente la malla a la que remite la fuente institucional: https://www.unach.edu.ec/wp-content/Facultades/Ingenier%C3%ADa/Mallas_academicas_2024/telecomunicaciones.jpg . Su imagen necesita conexión a Internet y puede abrirse en tamaño completo.

El directorio conserva la nómina del Excel y las correcciones confirmadas; no se sustituyó por el directorio público, que puede incluir adscripciones de otros períodos. Las publicaciones, métricas, ORCID y fuentes de las fichas se preservan. La sección Investigación calcula títulos distintos cargados por su título normalizado; no representa un indicador bibliométrico oficial.
