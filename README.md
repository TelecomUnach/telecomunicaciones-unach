# Portal Académico y Científico — Ingeniería en Telecomunicaciones

Prototipo web estático inspirado en la organización de portales de perfiles académicos. **No es un sitio oficial de la UNACH**. Los registros de docentes, publicaciones y proyectos son ejemplos para pruebas; no deben presentarse como información institucional verificada.

## Archivos

- `index.html`: estructura y secciones del portal.
- `styles.css`: apariencia adaptable a móvil y escritorio.
- `data.js`: datos editables de docentes, publicaciones y proyectos.
- `script.js`: buscadores, filtros, fichas individuales y menú móvil.

## Probar localmente

Abre `index.html` en Chrome, Firefox o Edge. No requiere instalar paquetes ni configurar una base de datos.

## Publicar gratis con GitHub Pages

1. Crea una cuenta en https://github.com si no tienes una.
2. En GitHub selecciona **New repository** y asigna un nombre, por ejemplo `telecomunicaciones-unach`. Elige **Public** (en GitHub Free, Pages para repositorios personales requiere un repositorio público).
3. Selecciona **Add file → Upload files**, sube los cuatro archivos `index.html`, `styles.css`, `data.js` y `script.js` a la raíz del repositorio y confirma con **Commit changes**.
4. Abre **Settings → Pages**. En **Build and deployment**, elige **Deploy from a branch**. Selecciona `main` y `/ (root)` y pulsa **Save**.
5. Espera la publicación y abre la dirección que aparezca en Pages, normalmente `https://TU-USUARIO.github.io/telecomunicaciones-unach/`.
6. Para que la dirección sea `https://TU-USUARIO.github.io/`, crea un repositorio llamado exactamente `TU-USUARIO.github.io` y sube los archivos a su raíz.

**Importante:** `telecomunicaciones-unach.github.io` solo puede ser tu dominio si el nombre de tu cuenta u organización GitHub es `telecomunicaciones-unach` y está disponible. El nombre de repositorio por sí solo no determina el subdominio.

## Actualizar contenidos

Edita `data.js`. Cada perfil contiene `id`, `name`, `role`, `area`, `initials`, `bio`, `interests`, `education`, `email`, `orcid`, `scholar` y `publications` (lista de IDs de publicaciones). Para crear un perfil nuevo, duplica un objeto y cambia todos los campos necesarios, manteniendo un `id` único. Haz lo mismo con `publications` y `projects`.

Si agregas una publicación real, registra título, autores, año, tipo, fuente y DOI verificados. El campo `doi` debe contener el identificador, no la URL completa. Los enlaces de ORCID y Scholar deben empezar con `https://`.

## Antes del lanzamiento institucional

- Solicitar autorización para uso del nombre, logotipo, identidad visual y datos institucionales.
- Obtener consentimiento o confirmar la base jurídica correspondiente para publicar fotografías, biografías y datos de contacto de docentes.
- Verificar los datos académicos y científicos.
- Sustituir los textos y perfiles de demostración y retirar el aviso de prototipo solo cuando el sitio tenga aprobación institucional.
- Definir responsables de actualización, revisión de contenido y accesibilidad.

## Límites de esta versión

Es un sitio estático, sin inicio de sesión, base de datos ni panel administrativo. Las actualizaciones se hacen editando `data.js` y subiendo cambios a GitHub. No incluye formularios que recolecten información personal.


## Actualización de identidad y fuente institucional
- `identidad-telecomunicaciones.png`: imagen proporcionada por el usuario; no modificar ni sustituir sin autorización.
- Se añadieron datos generales, misión, visión y perfil de egreso sintetizados de https://www.unach.edu.ec/ingenieria-en-telecomunicaciones/ (consultado el 15-10-2026).
- La lista de docentes, publicaciones y proyectos continúa siendo demostrativa: editar `data.js` antes de publicación oficial.
- Para GitHub Pages, subir el **contenido** de esta carpeta a la raíz del repositorio (no la carpeta contenedora).
