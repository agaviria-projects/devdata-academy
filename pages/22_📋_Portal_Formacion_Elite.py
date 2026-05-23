import streamlit as st

# =========================================================
# CONFIGURACIÓN PÁGINA
# =========================================================

st.set_page_config(
    page_title="Portal Formación Elite",
    page_icon="📋",
    layout="wide"
)

# =========================================================
# HEADER
# =========================================================

st.title("📋 Portal de Formación Elite")
st.caption("Manual de desarrollador: GitHub, Streamlit Cloud, Supabase, PostgreSQL y operación del sistema")

# =========================================================
# DOCUMENTACIÓN
# =========================================================

st.markdown("""

Manual técnico para recordar cómo funciona el ecosistema completo del proyecto.

Este documento está pensado para que, aunque pase un mes o más tiempo, pueda recordar:

- Dónde está el código
- Dónde está publicada la app
- Dónde está la base de datos
- Cómo probar localmente
- Cómo subir cambios a producción
- Qué hacer si la app no actualiza
- Qué revisar antes de una capacitación real
- Cómo operar el sistema desde el rol de administrador/formador

---

# 1. Mapa general del ecosistema

El proyecto funciona con cuatro piezas principales:

| Orden | Herramienta | Para qué sirve |
|---|---|---|
| 1 | GitHub | Guarda el código fuente |
| 2 | Streamlit Cloud | Publica la app en internet |
| 3 | Supabase | Aloja la base de datos en la nube |
| 4 | PostgreSQL | Motor real de la base de datos |

Flujo general:

    VS Code
        ↓
    Prueba local con Streamlit
        ↓
    Git commit
        ↓
    Git push a GitHub
        ↓
    Streamlit Cloud actualiza producción
        ↓
    Usuario final entra desde celular
        ↓
    Datos se guardan en Supabase / PostgreSQL
            
# Flujo correcto cuando voy a realizar ajustes

## Orden recomendado

1. Abrir VS Code
2. Modificar el código
3. Guardar archivo
4. Probar localmente:

    streamlit run app.py

5. Validar que no haya errores
6. Revisar cambios con Git:

    git status

7. Agregar cambios:

    git add .

8. Crear commit:

    git commit -m "descripcion del ajuste"

9. Subir a GitHub:

    git push origin main

10. Entrar a Streamlit Cloud
11. Revisar si hizo redeploy automático
12. Si no actualiza:

    Manage App
        ↓
    Redeploy

13. Si sigue igual:

    Clear Cache
        ↓
    Reboot App

14. Probar la app en producción desde celular
            
# Limpieza de base de datos antes de producción

Para dejar la base de datos limpia antes de producción, usar Supabase:

    Supabase
        ↓
    SQL Editor

Antes de borrar, revisar cuántos registros existen:

    SELECT COUNT(*) FROM asistencias;
    SELECT COUNT(*) FROM formaciones;
    SELECT COUNT(*) FROM empleados;

Opción recomendada para borrar registros y reiniciar IDs:

    TRUNCATE TABLE asistencias RESTART IDENTITY CASCADE;
    TRUNCATE TABLE formaciones RESTART IDENTITY CASCADE;
   

Si existen tablas de preguntas y respuestas:

    TRUNCATE TABLE respuestas RESTART IDENTITY CASCADE;
    TRUNCATE TABLE preguntas RESTART IDENTITY CASCADE;
    TRUNCATE TABLE asistencias RESTART IDENTITY CASCADE;
    TRUNCATE TABLE formaciones RESTART IDENTITY CASCADE;

Versión compacta:
Cuando quiero dejar producción limpia, pero conservar empleados cargados, debo borrar solo datos operativos:            

    TRUNCATE TABLE 
        respuestas,
        preguntas,
        asistencias,
        formaciones
    RESTART IDENTITY CASCADE;

Significado:

| Comando | Qué hace |
|---|---|
| TRUNCATE TABLE | Borra todos los registros de una tabla |
| RESTART IDENTITY | Reinicia los IDs desde 1 |
| CASCADE | Borra registros relacionados por llaves foráneas |

IMPORTANTE:

Ejecutar estas sentencias solo si estoy seguro de borrar los datos.

Antes de limpiar producción, descargar respaldo Excel o validar que los datos sean solo de prueba.
            
# Importante sobre limpieza de base de datos

La base de datos NO vive en mi PC.

La base de datos vive en Supabase/PostgreSQL en la nube.

Por eso, si ejecuto una limpieza desde Supabase SQL Editor usando mi PC personal, el cambio aplica sobre la base real del proyecto.

No necesito repetir los mismos comandos en el PC empresarial.

Flujo:

    PC personal
        ↓
    Supabase / PostgreSQL
        ↑
    PC empresarial

Ambos computadores se conectan a la misma base de datos cloud.

IMPORTANTE:

Solo debo ejecutar TRUNCATE si estoy seguro de que los datos son de prueba o ya tienen respaldo.

## Cómo volver a cargar empleados desde CSV

Si los empleados fueron borrados y ya existe un archivo CSV con la información, se pueden volver a cargar directamente desde Supabase.

Ruta:

    Supabase
        ↓
    Table Editor
        ↓
    empleados
        ↓
    Insert
        ↓
    Import data from CSV

Pasos:

1. Entrar a Supabase
2. Abrir proyecto app-capacitaciones
3. Entrar a Table Editor
4. Seleccionar tabla:

    empleados

5. Buscar opción:

    Import data from CSV

6. Seleccionar archivo CSV
7. Revisar que las columnas coincidan
8. Confirmar importación


# Consultas SQL reales del Portal Formación Elite

Estas consultas se ejecutan en:

    Supabase
        ↓
    SQL Editor

---

# 1. Ver últimas formaciones creadas

La tabla formaciones usa la columna:

    id

No usa:

    id_formacion

Consulta correcta:

    SELECT *
    FROM formaciones
    ORDER BY id DESC
    LIMIT 5;

---

# 2. Ver últimas asistencias registradas

    SELECT *
    FROM asistencias
    ORDER BY fecha_registro DESC
    LIMIT 5;

---

# 3. Buscar una formación por ID

    SELECT *
    FROM formaciones
    WHERE id = 1;

---

# 4. Buscar asistencias de una formación

    SELECT *
    FROM asistencias
    WHERE id_formacion = 1
    ORDER BY fecha_registro DESC;

---

# 5. Buscar empleado por cédula

    SELECT *
    FROM empleados
    WHERE cedula = '123456';

---

# 6. Ver empleados activos

    SELECT *
    FROM empleados
    WHERE estado = 'ACTIVO'
    ORDER BY nombre_completo ASC;

---

# 7. Ver empleados inactivos

    SELECT *
    FROM empleados
    WHERE estado = 'INACTIVO'
    ORDER BY nombre_completo ASC;

---

# 8. Activar empleado

    UPDATE empleados
    SET estado = 'ACTIVO'
    WHERE cedula = '123456';

---

# 9. Inactivar empleado

    UPDATE empleados
    SET estado = 'INACTIVO'
    WHERE cedula = '123456';

---

# 10. Validar cantidad de registros

    SELECT COUNT(*) FROM empleados;
    SELECT COUNT(*) FROM formaciones;
    SELECT COUNT(*) FROM asistencias;

---

# 11. Validar duplicado de asistencia

    SELECT *
    FROM asistencias
    WHERE cedula = '123456'
      AND id_formacion = 1;

---

# 12. Reporte general de asistencias

    SELECT 
        a.id,
        a.id_formacion,
        a.cedula,
        a.nombre_completo,
        a.cargo,
        a.proyecto,
        a.zona,
        a.formador,
        a.clasificacion_formacion,
        a.tipo_formacion,
        a.autoriza_datos,
        a.fecha_registro,
        a.puntaje
    FROM asistencias a
    ORDER BY a.fecha_registro DESC;

---

# 13. Reporte uniendo asistencias con formaciones

    SELECT 
        a.id,
        a.cedula,
        a.nombre_completo,
        a.cargo,
        a.proyecto,
        a.zona,
        f.nombre_formacion,
        f.fecha_asistencia,
        f.formador,
        a.tipo_formacion,
        a.autoriza_datos,
        a.fecha_registro,
        a.puntaje
    FROM asistencias a
    INNER JOIN formaciones f ON a.id_formacion = f.id
    ORDER BY a.fecha_registro DESC;

---

# 14. Limpiar producción sin borrar empleados

Usar cuando quiero borrar pruebas, formaciones y asistencias, pero conservar empleados cargados.

    TRUNCATE TABLE 
        asistencias,
        formaciones
    RESTART IDENTITY CASCADE;

Resultado esperado:

    empleados   = se conservan
    formaciones = 0
    asistencias = 0

---

# 15. Limpiar todo incluyendo empleados

Usar solo si quiero dejar completamente vacía la base de datos.

    TRUNCATE TABLE 
        asistencias,
        formaciones,
        empleados
    RESTART IDENTITY CASCADE;

IMPORTANTE:

Esto borra también los empleados.

---

# 16. Si existen preguntas y respuestas

Si el sistema tiene tablas de preguntas y respuestas, limpiar así:

    TRUNCATE TABLE 
        respuestas,
        preguntas,
        asistencias,
        formaciones
    RESTART IDENTITY CASCADE;

No incluir empleados si quiero conservarlos.

---

# 17. Validar columnas reales de una tabla

Cuando aparezca error como:

    column "id_formacion" does not exist

Debo revisar los nombres reales de columnas.

Consulta:

    SELECT column_name
    FROM information_schema.columns
    WHERE table_name = 'formaciones';

Para asistencias:

    SELECT column_name
    FROM information_schema.columns
    WHERE table_name = 'asistencias';

Para empleados:

    SELECT column_name
    FROM information_schema.columns
    WHERE table_name = 'empleados';

---

# 18. Regla importante

La tabla formaciones tiene:

    id

La tabla asistencias guarda la relación con formación en:

    id_formacion

Por eso el JOIN correcto es:

    asistencias.id_formacion = formaciones.id            
---

# Recomendaciones antes de importar

El archivo CSV debe tener las columnas correctas.

Ejemplo:

| cedula | nombre_completo | cargo | proyecto | zona | estado |
|---|---|---|---|---|---|

Ejemplo de estados válidos:

    ACTIVO
    INACTIVO

---

# Validación después de importar

Consultar cantidad de empleados:

    SELECT COUNT(*) FROM empleados;

Consultar algunos registros:

    SELECT *
    FROM empleados
    LIMIT 20;

Validar empleados activos:

    SELECT *
    FROM empleados
    WHERE estado = 'ACTIVO';

---

# Importante

Si la tabla empleados tiene IDs automáticos:

- Supabase puede generarlos automáticamente
- No siempre es necesario incluir id_empleado en el CSV

---

# Recomendación profesional

Antes de importar:

1. Limpiar datos en Excel
2. Revisar columnas
3. Revisar estados
4. Revisar cédulas duplicadas
5. Guardar CSV UTF-8 si es posible

Después de importar:

1. Validar cantidad de registros
2. Probar una cédula en la app
3. Confirmar que el empleado aparezca correctamente                        
---

# 2. Regla de oro como desarrollador

Guardar cambios en VS Code NO actualiza la app del usuario.

Para que el usuario vea los cambios se necesita:

    Guardar archivo
        ↓
    Probar localmente
        ↓
    Hacer commit
        ↓
    Hacer push a GitHub
        ↓
    Streamlit Cloud redeploy
        ↓
    Validar producción

---

# 3. Diferencia entre local y producción

| Ambiente | URL | Quién lo ve | Para qué sirve |
|---|---|---|---|
| Local | localhost:8501 | Solo yo | Probar cambios |
| Producción | streamlit.app | Usuarios reales | Uso real de la app |

Ejemplo local:

    http://localhost:8501

Ejemplo producción:

    https://elite-sst.streamlit.app

IMPORTANTE:

Localhost solo funciona en mi computador.  
El usuario final nunca entra por localhost.

---

# 4. GitHub

GitHub es donde se guarda el código fuente del proyecto.

En este proyecto GitHub sirve para:

- Guardar historial de cambios
- Tener respaldo del código
- Conectar el proyecto con Streamlit Cloud
- Permitir que Streamlit Cloud detecte cambios
- Controlar qué versión está en producción

---

# 5. Repositorio GitHub del proyecto

Repositorio esperado: 

    agaviria-projects

Cuenta correcta para este repositorio:

    agaviria-projects

Si Git intenta hacer push con otra cuenta, puede aparecer error de permisos.

---

# 6. Comandos Git principales

## Ver estado del proyecto

    git status

## Agregar cambios

    git add .

## Crear commit

    git commit -m "mensaje claro del cambio"

## Subir cambios

    git push origin main

## Descargar cambios desde GitHub

    git pull origin main

## Ver repositorio remoto

    git remote -v

## Ver rama actual

    git branch

---

# 7. Flujo correcto con GitHub

Cada vez que haga un ajuste debo seguir este orden:

1. Abrir VS Code
2. Editar archivo
3. Guardar cambios
4. Probar localmente
5. Ejecutar git status
6. Ejecutar git add .
7. Ejecutar git commit
8. Ejecutar git push origin main
9. Revisar Streamlit Cloud
10. Probar producción

Comandos:

    git status
    git add .
    git commit -m "actualiza documentacion portal formacion elite"
    git push origin main

---

# 8. Error común de GitHub: permiso denegado

Error posible:

    Permission to agaviria-projects/devdata-academy.git denied to elite-sst

Significa:

Git está intentando subir cambios con la cuenta incorrecta.

| Repositorio | Cuenta correcta |
|---|---|
| agaviria-projects/devdata-academy | agaviria-projects |

Si aparece elite-sst, significa que Windows, navegador o GitHub quedó autenticado con otra cuenta.

Solución general:

1. Revisar cuenta activa en GitHub
2. Cerrar sesión de la cuenta incorrecta
3. Borrar credenciales de Windows si es necesario
4. Iniciar sesión con agaviria-projects
5. Repetir:

    git push origin main

Recomendación:

Usar navegadores o perfiles separados para cada cuenta.

| Cuenta | Uso recomendado |
|---|---|
| agaviria-projects | DevData Academy |
| elite-sst | App corporativa Elite SST |

---

# 9. Streamlit Cloud / streamlit.io

Streamlit Cloud es la plataforma donde se publica la aplicación para que otras personas puedan usarla desde internet.

También puede aparecer como:

    https://share.streamlit.io

o:

    https://streamlit.io/cloud

En este proyecto sirve para:

- Publicar la app
- Conectar GitHub con producción
- Ejecutar la app en la nube
- Crear una URL pública
- Permitir acceso desde celular
- Revisar logs de errores
- Reiniciar la app
- Administrar secretos de conexión

---

# 10. Cómo ingresar a Streamlit Cloud

Pasos:

1. Entrar a:

    https://share.streamlit.io

2. Iniciar sesión con la cuenta de GitHub correcta osea elite-sst contraseña 35@El1te}5 
3. Buscar la app del proyecto : sistema-capacitaciones ∙ main ∙ app.py
4. Entrar a Manage App 

Desde Manage App puedo:

- Ver si la app está corriendo
- Ver logs
- Revisar errores
- Reiniciar la app : Reboot app
- Limpiar caché
- Forzar redeploy
- Revisar Secrets
- Revisar configuración general

---

# 11. Qué revisar en Streamlit Cloud

| Sección | Para qué sirve |
|---|---|
| Logs | Ver errores de Python, librerías o conexión |
| Reboot App | Reiniciar la app |
| Clear Cache | Limpiar memoria temporal |
| Redeploy | Forzar nuevo despliegue |
| Settings | Revisar configuración |
| Secrets | Guardar variables privadas |

---

# 12. Qué son los Secrets de Streamlit Cloud

Los Secrets son variables privadas que la app necesita para funcionar.

Ejemplos:

    DATABASE_URL
    ADMIN_PASSWORD

No se deben escribir directamente dentro del código Python.

Ruta común:

    Streamlit Cloud
        ↓
    Manage App
        ↓
    Settings
        ↓
    Secrets : esta la contraseña del usuario Elite2026

Ejemplo conceptual:

    DATABASE_URL = "postgresql://usuario:password@host:puerto/base"
    ADMIN_PASSWORD = "contraseña_de_ingreso_admin"  : osea para ingreso a la app

IMPORTANTE:

Nunca compartir públicamente:

- DATABASE_URL real
- password real
- tokens
- claves privadas
- credenciales de Supabase
DATABASE_URL contiene la conexión completa a PostgreSQL/Supabase.

Dentro de esa URL viene la contraseña de la base de datos, no la contraseña del administrador de la app.

ADMIN_PASSWORD = contraseña para entrar al panel Admin: Elite2026

DATABASE_URL = conexión técnica para que la app pueda leer y guardar datos en Supabase contraseña:formador2026
            
DATABASE_URL = conexión técnica entre Streamlit y PostgreSQL/Supabase.

La app utiliza DATABASE_URL para:

- Leer empleados
- Guardar asistencias
- Consultar formaciones
- Descargar reportes
- Ejecutar consultas SQL
- Conectarse a PostgreSQL

En palabras simples:

    Streamlit
        ↓
    DATABASE_URL
        ↓
    Supabase
        ↓
    PostgreSQL

DATABASE_URL contiene:

- usuario PostgreSQL
- contraseña PostgreSQL
- host del servidor
- puerto
- nombre de la base de datos

Ejemplo conceptual:

    DATABASE_URL = "postgresql://usuario:password@host:puerto/base"

IMPORTANTE:

DATABASE_URL NO es la contraseña del administrador de la app.

ADMIN_PASSWORD = acceso panel admin

DATABASE_URL = conexión técnica con PostgreSQL/Supabase            
---

# 13. Cómo se actualiza producción en Streamlit Cloud

Streamlit Cloud toma el código desde GitHub.

Cuando hago:

    git push origin main

Streamlit Cloud detecta el cambio y redeploya la app.

Flujo:

    GitHub
        ↓
    Streamlit Cloud
        ↓
    URL pública
        ↓
    Usuario final

---

# 14. Qué hacer si Streamlit Cloud no actualiza

Si la app no muestra cambios:

1. Confirmar que hice git push
2. Confirmar que el cambio aparece en GitHub
3. Entrar a Streamlit Cloud
4. Abrir Manage App
5. Revisar logs
6. Usar Redeploy
7. Si sigue igual, usar Clear Cache
8. Si sigue igual, usar Reboot App

Ruta común:

    Manage App
        ↓
    Redeploy

Otra opción:

    Manage App
        ↓
    Clear Cache
        ↓
    Reboot App

---

# 15. Qué hacer cuando aparece Zzzz

Cuando aparece Zzzz significa que la app está dormida.

Esto puede pasar en Streamlit Cloud gratuito por inactividad.

Qué hacer:

1. Abrir la app antes de usarla
2. Esperar que despierte
3. Navegar por los módulos
4. Probar una URL de asistencia
5. Confirmar que carga correctamente

Recomendación:

Abrir la app mínimo 10 o 15 minutos antes de una capacitación real.

---

# 16. Supabase

Supabase es la plataforma cloud donde está alojada la base de datos del proyecto.

En este sistema Supabase sirve para:

- Guardar empleados
- Guardar formaciones
- Guardar asistencias
- Consultar información
- Ejecutar SQL
- Administrar tablas
- Centralizar datos en la nube

Supabase NO es donde edito el código.

Supabase es donde administro la base de datos.

---

# 17. Cómo ingresar a Supabase

Supabase es donde está alojada la base de datos real del proyecto.

En este caso, la base de datos del Portal de Formación Elite está dentro del proyecto:

    app-capacitaciones

Y está asociada a la cuenta:

    agaviria-projects

Correo visible de referencia:

    agaviria1408@gmail.com

Dentro de Supabase debo verificar que estoy en:

| Elemento | Valor esperado |
|---|---|
| Cuenta | agaviria-projects |
| Proyecto | app-capacitaciones |
| Rama | main |
| Entorno | PRODUCTION |
| Schema | public |

Pasos para ingresar:

1. Entrar a:

    https://supabase.com

2. Iniciar sesión con la cuenta correcta:

    agaviria-projects

3. Seleccionar el proyecto:

    app-capacitaciones

4. Entrar a:

    Table Editor

5. Verificar que aparezcan las tablas principales:

    asistencias
    empleados
    formaciones

6. Para ejecutar consultas, entrar a:

    SQL Editor

7. Para revisar configuración de conexión, entrar a:

    Settings
        ↓
    Database

Importante:

Supabase NO es donde edito el código.  
Supabase es donde administro los datos reales.

El código se edita en VS Code.  
El código se guarda en GitHub.  
La app corre en Streamlit Cloud.  
Los datos se guardan en Supabase/PostgreSQL.

Nunca colocar aquí:

- Contraseñas reales
- DATABASE_URL real
- Tokens
- Claves privadas
- Password de PostgreSQL

# 18. Qué revisar en Supabase

| Sección | Para qué sirve |
|---|---|
| Table Editor | Ver registros de las tablas |
| SQL Editor | Ejecutar consultas SQL |
| Settings | Revisar configuración del proyecto |
| Database | Revisar conexión y datos técnicos |
| Logs | Diagnosticar errores si aplica |

---

# 19. PostgreSQL

PostgreSQL es el motor de base de datos relacional que usa Supabase.

En palabras simples:

- Supabase es la plataforma
- PostgreSQL es la base de datos real

PostgreSQL sirve para:

- Guardar datos estructurados
- Relacionar tablas
- Ejecutar consultas SQL
- Mantener integridad de información
- Consultar registros
- Actualizar empleados
- Revisar asistencias
- Generar reportes

---

# 20. Tablas principales del sistema

| Tabla | Función |
|---|---|
| empleados | Guarda información del personal |
| formaciones | Guarda charlas y capacitaciones |
| asistencias | Guarda registros de asistencia |
| preguntas | Guarda preguntas de capacitaciones si aplica |
| respuestas | Guarda opciones de respuesta si aplica |

---

# 21. Tabla empleados

Guarda la información del personal.

Campos comunes:

- cedula
- nombre_completo
- cargo
- proyecto
- zona
- estado

Estados posibles:

| Estado | Resultado |
|---|---|
| ACTIVO | Puede registrar asistencia |
| INACTIVO | No puede registrar asistencia |

Consulta para buscar empleado:

    SELECT cedula, nombre_completo, cargo, proyecto, zona, estado
    FROM empleados
    WHERE cedula = '123456';

Activar empleado:

    UPDATE empleados
    SET estado = 'ACTIVO'
    WHERE cedula = '123456';

Inactivar empleado:

    UPDATE empleados
    SET estado = 'INACTIVO'
    WHERE cedula = '123456';

---

# 22. Tabla formaciones

Guarda las charlas o capacitaciones.

Campos comunes:

- id_formacion
- nombre_formacion
- fecha_asistencia
- formador
- clasificacion_formacion
- tipo_formacion

Consulta para ver últimas formaciones:

    SELECT id_formacion, nombre_formacion, fecha_asistencia, formador
    FROM formaciones
    ORDER BY id_formacion DESC
    LIMIT 10;

Consulta por ID:

    SELECT *
    FROM formaciones
    WHERE id_formacion = 15;

---

# 23. Tabla asistencias

Guarda los registros realizados por empleados.

Campos comunes:

- id_asistencia
- id_formacion
- cedula
- fecha_registro
- puntaje
- respuestas

Consulta para ver asistencias recientes:

    SELECT *
    FROM asistencias
    ORDER BY fecha_registro DESC
    LIMIT 20;

Consulta de asistentes por formación:

    SELECT a.*, e.nombre_completo, e.cargo, e.proyecto, e.zona
    FROM asistencias a
    INNER JOIN empleados e ON a.cedula = e.cedula
    WHERE a.id_formacion = 15;

---

# 24. Consulta para reporte general

Ejemplo de consulta para unir asistencias, empleados y formaciones:

    SELECT 
        a.id_asistencia,
        a.cedula,
        e.nombre_completo,
        e.cargo,
        e.proyecto,
        e.zona,
        f.nombre_formacion,
        f.formador,
        f.fecha_asistencia,
        a.fecha_registro,
        a.puntaje
    FROM asistencias a
    INNER JOIN empleados e ON a.cedula = e.cedula
    INNER JOIN formaciones f ON a.id_formacion = f.id_formacion
    ORDER BY a.fecha_registro DESC;

---

# 25. Consulta para revisar duplicados

Validar si una cédula ya registró asistencia en una formación:

    SELECT *
    FROM asistencias
    WHERE cedula = '123456'
      AND id_formacion = 15;

---

# 26. Consulta para consolidado mensual

Ejemplo conceptual:

    SELECT 
        DATE_TRUNC('month', a.fecha_registro) AS mes,
        COUNT(*) AS total_asistencias
    FROM asistencias a
    GROUP BY DATE_TRUNC('month', a.fecha_registro)
    ORDER BY mes DESC;

---

# 27. Flujo correcto para hacer cambios diarios

Este es el flujo que debo seguir cuando haga ajustes en el código.

## Paso 1: Abrir VS Code

Abrir la carpeta del proyecto:

    DevData_Academy

## Paso 2: Editar archivo

Ejemplo:

    pages/22_📋_Portal_Formacion_Elite.py

## Paso 3: Probar localmente

Ejecutar:

    streamlit run app.py

Abrir:

    http://localhost:8501

## Paso 4: Validar local

Revisar:

- Que la app abra
- Que el módulo cargue
- Que no haya error rojo
- Que los botones funcionen
- Que el menú no se rompa
- Que se vea bien

## Paso 5: Revisar Git

    git status

## Paso 6: Agregar cambios

    git add .

## Paso 7: Crear commit

    git commit -m "ajustes portal formacion elite"

## Paso 8: Subir a GitHub

    git push origin main

## Paso 9: Revisar Streamlit Cloud

Entrar a:

    https://share.streamlit.io

Luego:

    Manage App
        ↓
    Logs

## Paso 10: Validar producción

Abrir la app real:

    https://elite-sst.streamlit.app

Probar desde celular si el cambio afecta usuarios.

---

# 28. Checklist antes de hacer commit

Antes de hacer commit verificar:

| Revisión | Estado |
|---|---|
| Probé localmente | Pendiente |
| No hay error rojo | Pendiente |
| Guardé el archivo | Pendiente |
| Revisé el módulo afectado | Pendiente |
| Revisé que no rompí otras páginas | Pendiente |
| Revisé que no subí claves reales | Pendiente |
| Revisé git status | Pendiente |

---

# 29. Checklist después de hacer push

Después de hacer push verificar:

| Revisión | Estado |
|---|---|
| El push terminó sin error | Pendiente |
| GitHub recibió los cambios | Pendiente |
| Streamlit Cloud redeployó | Pendiente |
| No hay errores en logs | Pendiente |
| La URL de producción abre | Pendiente |
| La app funciona desde celular | Pendiente |

---

# 30. Qué hacer si algo falla

## Si falla local

Revisar:

- Error rojo en terminal
- Archivo modificado
- Comillas mal cerradas
- Indentación
- Imports
- Variables no definidas

## Si falla GitHub

Revisar:

- Cuenta activa
- Remote
- Permisos
- Credenciales
- Rama main

Comando:

    git remote -v

## Si falla Streamlit Cloud

Revisar:

- Logs
- Secrets
- requirements.txt
- Conexión a Supabase
- Errores de importación

## Si falla Supabase

Revisar:

- Table Editor
- SQL Editor
- Nombre de tablas
- Nombre de columnas
- DATABASE_URL
- Permisos de conexión

---

# 31. Qué es el Portal de Formación Elite

El Portal de Formación Elite es una aplicación para gestionar procesos de formación empresarial.

Permite:

- Crear charlas
- Crear capacitaciones
- Registrar asistencia
- Evaluar conocimientos
- Validar empleados
- Descargar reportes
- Generar consolidado mensual
- Operar desde celular

---

# 32. Cómo ingresa el administrador o formador

El administrador entra al panel interno de la app.

Desde allí puede:

- Crear formación
- Consultar formación
- Editar preguntas
- Gestionar empleados
- Descargar reportes
- Revisar consolidado mensual

El administrador debe recordar:

Cualquier cambio realizado en producción impacta el sistema real.

---

# 33. Cómo ingresa el empleado

El empleado entra por una URL pública.

Ejemplo:

    https://elite-sst.streamlit.app/Asistencia?formacion=15

La parte importante es:

    ?formacion=15

Ese número corresponde al ID de la formación.

---

# 34. Por qué la URL no cambia

La URL depende del ID de la formación.

Ejemplo:

    formacion=15

Mientras esa formación exista, la URL seguirá funcionando.

Esto significa:

- Si cambio el nombre de la formación, la URL no cambia
- Si edito preguntas, la URL no cambia
- Si comparto nuevamente el enlace, entra a la misma formación
- Si elimino la formación, la URL puede dejar de funcionar

---

# 35. Cómo crear una charla

Una charla normalmente solo registra asistencia.

Flujo:

1. Entrar al panel administrador
2. Ir a Crear formación
3. Escribir nombre de la charla
4. Seleccionar clasificación CHARLA
5. Guardar
6. Copiar URL generada
7. Compartir al grupo

Ejemplos:

- Charla de seguridad vial
- Charla uso de EPP
- Charla trabajo seguro en alturas

---

# 36. Cómo crear una capacitación con preguntas

Una capacitación puede incluir evaluación.

Flujo:

1. Crear la formación
2. Seleccionar clasificación CAPACITACIÓN
3. Agregar preguntas
4. Agregar respuestas
5. Marcar respuesta correcta
6. Guardar
7. Copiar URL
8. Compartir con empleados

El sistema puede calcular puntaje según respuestas registradas.

---

# 37. Cómo editar preguntas y respuestas

Ruta:

    Consultar / Editar
        ↓
    Seleccionar formación
        ↓
    Editar preguntas o respuestas

Se puede modificar:

- Texto de pregunta
- Opciones de respuesta
- Respuesta correcta
- Estado o contenido de capacitación

Advertencia:

Si la formación ya fue respondida por empleados, editar preguntas puede afectar la trazabilidad histórica.

---

# 38. Registro de asistencia desde celular

Flujo del empleado:

1. Abre URL desde celular
2. Ingresa cédula
3. Sistema valida si existe
4. Sistema valida si está activo
5. Se muestran datos del empleado
6. Responde preguntas si aplica
7. Registra asistencia
8. Sistema muestra confirmación

Datos esperados:

- Cédula
- Nombre
- Cargo
- Proyecto
- Zona
- Formación
- Fecha de registro
- Puntaje si aplica

---

# 39. Qué pasa después de registrar asistencia

Después de registrar una asistencia correctamente, el sistema debe limpiar:

- Campo cédula
- Datos del empleado
- Respuestas seleccionadas
- Estado temporal del formulario

Objetivo:

Evitar que el siguiente empleado registre información con datos anteriores.

Esto es clave cuando varios empleados usan el mismo celular.

---

# 40. Mensajes esperados del sistema

| Caso | Mensaje esperado |
|---|---|
| Registro correcto | Asistencia registrada correctamente |
| Puntaje calculado | Puntaje obtenido |
| Cédula repetida | La cédula ya registró asistencia |
| Empleado inactivo | Empleado inactivo o no encontrado |
| Cédula vacía | Debe ingresar la cédula |
| Formación inválida | Formación no encontrada |

---

# 41. Reportes y descarga Excel

El administrador puede descargar reportes en Excel.

Los reportes pueden incluir:

- Asistencias registradas
- Datos del empleado
- Formación
- Fecha
- Puntaje
- Respuestas
- Clasificación
- Tipo de formación

Campos recomendados:

| Campo |
|---|
| cédula |
| nombre completo |
| cargo |
| proyecto |
| zona |
| nombre formación |
| formador |
| fecha asistencia |
| fecha registro |
| puntaje |
| estado empleado |

---

# 42. Consolidado mensual

El consolidado mensual sirve para análisis gerencial.

Permite revisar:

- Cantidad de asistencias por mes
- Capacitaciones realizadas
- Participación por zona
- Participación por proyecto
- Puntajes promedio
- Empleados capacitados
- Empleados pendientes

Útil para:

- SST
- Gestión humana
- Auditoría
- Indicadores internos

---

# 43. Recomendación antes de una capacitación real

Antes de una capacitación:

1. Abrir app de producción
2. Confirmar que no está dormida
3. Entrar al módulo Admin
4. Crear o validar formación
5. Copiar URL pública
6. Probar URL en celular
7. Registrar asistencia de prueba
8. Descargar Excel de prueba
9. Validar que el empleado aparezca correctamente
10. Compartir URL al grupo

---

# 44. Prueba mínima antes de producción

Antes de enviar la URL a empleados reales:

- Probar con una cédula activa
- Probar con una cédula inactiva
- Probar una cédula ya registrada
- Probar desde celular
- Probar desde computador
- Descargar reporte Excel
- Revisar que la formación sea correcta
- Revisar puntaje si tiene preguntas

---

# 45. Prueba con dos celulares

Se recomienda probar con:

- Un celular Android
- Un celular iPhone si es posible

Validar:

- Que el formulario cargue
- Que los campos se vean bien
- Que el botón funcione
- Que no se corte el texto
- Que el registro sea exitoso
- Que después del registro se limpien los datos

---

# 46. Buenas prácticas

- No modificar producción sin probar local
- No subir cambios sin revisar git status
- Usar mensajes de commit claros
- No guardar contraseñas en archivos Python
- No compartir DATABASE_URL
- Documentar errores encontrados
- Documentar soluciones aplicadas
- Mantener separadas las cuentas GitHub
- Probar siempre desde celular
- Descargar reporte después de pruebas importantes
- Revisar Streamlit Cloud antes de una capacitación
- Revisar Supabase si algo no guarda

---

# 47. Riesgos y recomendaciones

| Riesgo | Impacto | Recomendación |
|---|---|---|
| App dormida | Usuarios no entran rápido | Despertar app antes |
| Mala cuenta GitHub | No deja hacer push | Verificar cuenta |
| Error SQL | No guarda información | Probar consultas |
| Empleado inactivo | No permite registro | Validar estado |
| URL incorrecta | Formación equivocada | Revisar ID |
| No probar celular | Fallo en campo | Probar antes |
| Modificar preguntas usadas | Afecta trazabilidad | Evitar cambios históricos |

---

# 48. Orden correcto cuando olvide qué hacer

Si dentro de un mes no recuerdo el flujo, seguir este orden:

1. Abrir VS Code
2. Abrir carpeta del proyecto
3. Ejecutar streamlit run app.py
4. Probar local
5. Corregir lo necesario
6. Ejecutar git status
7. Ejecutar git add .
8. Ejecutar git commit -m "mensaje"
9. Ejecutar git push origin main
10. Entrar a GitHub y confirmar cambio
11. Entrar a Streamlit Cloud
12. Verificar redeploy
13. Abrir app en producción
14. Probar desde celular
15. Revisar Supabase si debe guardar datos
16. Descargar Excel si aplica

---

# 49. Frase clave para recordar

El código vive en GitHub.

La app vive en Streamlit Cloud.

Los datos viven en Supabase.

El motor de datos es PostgreSQL.

Yo desarrollo en VS Code y pruebo primero en localhost.

---
# 50. Código para el sistema-capaictaciones.main.app.py
Settings-Secrets contraseñas de la base de datos en supabase -bd postgreSQL formador2026
y Elite2026 con el que ingresa el usuario a la app
            
DATABASE_URL = "postgresql+psycopg2://postgres.oefqprhzbhajncellasi:formador2026@aws-1-us-west-
1.pooler.supabase.com:6543/postgres"

ADMIN_PASSWORD = "Elite2026"

---            
# 51. Conclusión

Este proyecto no es solo una app en Streamlit.

Es un flujo completo de desarrollo real:

- Código local
- Git
- GitHub
- Streamlit Cloud
- Supabase
- PostgreSQL
- Usuarios finales en celular
- Reportes Excel
- Operación empresarial

La documentación evita depender de la memoria y permite recordar:

- Cómo entrar
- Qué revisar
- Qué hacer primero
- Cómo probar local
- Cómo subir a producción
- Cómo corregir errores
- Cómo operar antes de una capacitación
- Cómo consultar y administrar la base de datos

---

""")