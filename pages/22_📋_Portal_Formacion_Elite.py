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
st.caption("Manual técnico, operativo y de despliegue del sistema de capacitaciones")

# =========================================================
# DOCUMENTACIÓN
# =========================================================

st.markdown("""

# 📋 Portal de Formación Elite

---

# 1. Objetivo del sistema

El Portal de Formación Elite fue creado para gestionar procesos de formación, charlas y capacitaciones empresariales desde una aplicación web construida en Streamlit.

El sistema permite:

- Crear charlas
- Crear capacitaciones con preguntas
- Generar URL pública para empleados
- Registrar asistencia desde celular
- Validar empleados activos e inactivos
- Calcular puntajes
- Descargar reportes en Excel
- Consultar consolidado mensual
- Administrar información desde una base de datos en la nube

Este módulo dentro de DevData Academy funciona como manual técnico para recordar cómo operar, mantener y desplegar el sistema.

---

# 2. Arquitectura general

El sistema funciona con esta arquitectura:

| Componente | Función |
|---|---|
| VS Code | Desarrollo local del código |
| Streamlit | Interfaz web de la aplicación |
| Supabase | Plataforma cloud donde está la base de datos |
| PostgreSQL | Motor de base de datos |
| Git | Control de versiones |
| GitHub | Repositorio del código |
| Streamlit Cloud | Despliegue en producción |
| Celular del empleado | Registro de asistencia |

Flujo general:

    VS CODE
        ↓
    STREAMLIT LOCAL
        ↓
    GIT COMMIT
        ↓
    GITHUB PUSH
        ↓
    STREAMLIT CLOUD
        ↓
    USUARIO FINAL

---

# 3. Regla de oro como desarrollador

## LOCAL NO ES PRODUCCIÓN

| Ambiente | Qué significa |
|---|---|
| localhost | Prueba en mi computador |
| GitHub | Repositorio donde guardo el código |
| Streamlit Cloud | Aplicación publicada para usuarios |
| Supabase | Base de datos real del sistema |

Guardar un archivo en VS Code NO actualiza automáticamente la app en producción.

Para que el usuario vea los cambios se necesita:

1. Guardar archivo
2. Probar local
3. Hacer commit
4. Hacer push
5. Esperar redeploy en Streamlit Cloud
6. Validar desde la URL real

---

# 4. Tecnologías utilizadas

| Tecnología | Uso |
|---|---|
| Python | Lenguaje principal |
| Streamlit | Construcción de la app |
| Supabase | Base de datos cloud |
| PostgreSQL | Motor relacional |
| SQLAlchemy | Conexión Python con PostgreSQL |
| pandas | Reportes y manejo de datos |
| openpyxl | Exportación Excel |
| Git | Versionamiento |
| GitHub | Repositorio |
| Streamlit Cloud | Despliegue web |

---

# 5. Cómo ingresar como administrador o formador

El administrador ingresa desde el panel interno de la app.

Desde allí puede:

- Crear formaciones
- Crear charlas
- Crear capacitaciones con preguntas
- Consultar formaciones
- Editar preguntas
- Gestionar empleados
- Descargar reportes
- Revisar consolidados

El administrador debe tener claro que cualquier cambio realizado en producción impacta el sistema real.

---

# 6. Cómo ingresa el empleado

El empleado no necesita usuario ni contraseña.

Ingresa por una URL pública generada por el sistema.

Ejemplo:

    https://elite-sst.streamlit.app/Asistencia?formacion=15

La parte importante es:

    ?formacion=15

Ese número corresponde al ID de la formación.

---

# 7. Por qué la URL no cambia

La URL depende del ID de la formación.

Ejemplo:

    formacion=15

Mientras esa formación exista en la base de datos, la URL seguirá funcionando.

Esto significa:

- Si se edita el nombre de la formación, la URL no cambia
- Si se editan preguntas, la URL no cambia
- Si se comparte nuevamente, entra a la misma formación
- Si se elimina la formación, la URL deja de funcionar correctamente

---

# 8. Cómo crear una charla

Una charla normalmente solo registra asistencia.

Flujo recomendado:

1. Entrar al panel administrador
2. Ir a Crear formación
3. Escribir el nombre de la charla
4. Seleccionar tipo o clasificación CHARLA
5. Guardar
6. Copiar la URL generada
7. Compartir al grupo operativo

Ejemplo de uso:

    Charla de seguridad vial
    Charla de uso de EPP
    Charla de trabajo seguro en alturas

---

# 9. Cómo crear una capacitación con preguntas

Una capacitación puede incluir evaluación.

Flujo recomendado:

1. Crear la formación
2. Seleccionar clasificación CAPACITACIÓN
3. Agregar preguntas
4. Agregar respuestas
5. Marcar la respuesta correcta
6. Guardar
7. Copiar la URL
8. Compartir con los empleados

El sistema puede calcular puntaje según las respuestas registradas.

---

# 10. Cómo editar preguntas y respuestas

Ruta recomendada:

    Consultar / Editar
        ↓
    Seleccionar formación
        ↓
    Editar preguntas o respuestas

Se puede modificar:

- Texto de la pregunta
- Opciones de respuesta
- Respuesta correcta
- Estado o contenido de la capacitación

Advertencia:

Si la formación ya fue respondida por empleados, editar preguntas puede afectar la trazabilidad del análisis histórico.

---

# 11. Registro de asistencia desde celular

Flujo del empleado:

1. Abre la URL desde el celular
2. Ingresa la cédula
3. El sistema valida si existe
4. El sistema valida si está activo
5. Se muestran los datos del empleado
6. Responde preguntas si aplica
7. Registra asistencia
8. El sistema muestra mensaje de confirmación

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

# 12. Qué pasa después de registrar asistencia

Después de registrar una asistencia correctamente, el sistema debe limpiar:

- Campo cédula
- Datos del empleado
- Respuestas seleccionadas
- Estado temporal del formulario

Objetivo:

Evitar que el siguiente empleado registre información con datos anteriores.

Esto es muy importante cuando varios empleados usan el mismo celular.

---

# 13. Mensajes esperados del sistema

| Caso | Mensaje esperado |
|---|---|
| Registro correcto | Asistencia registrada correctamente |
| Puntaje calculado | Puntaje obtenido |
| Cédula repetida | La cédula ya registró asistencia |
| Empleado inactivo | Empleado inactivo o no encontrado |
| Cédula vacía | Debe ingresar la cédula |
| Formación inválida | Formación no encontrada |

---

# 14. Reportes y descarga Excel

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

# 15. Consolidado mensual

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

# 16. Gestión de empleados activos e inactivos

Los empleados deben tener un estado.

Ejemplo:

| Estado | Resultado |
|---|---|
| ACTIVO | Puede registrar asistencia |
| INACTIVO | No puede registrar asistencia |

Ejemplo SQL para activar empleado:

    UPDATE empleados
    SET estado = 'ACTIVO'
    WHERE cedula = '123456';

Ejemplo SQL para inactivar empleado:

    UPDATE empleados
    SET estado = 'INACTIVO'
    WHERE cedula = '123456';

Ejemplo SQL para consultar empleado:

    SELECT cedula, nombre_completo, cargo, estado
    FROM empleados
    WHERE cedula = '123456';

---

# 17. Qué es Supabase

Supabase es una plataforma en la nube que permite crear y administrar bases de datos PostgreSQL.

En este proyecto se usa para:

- Guardar empleados
- Guardar formaciones
- Guardar asistencias
- Consultar reportes
- Mantener datos centralizados

Supabase es como el backend de datos del sistema.

---

# 18. Qué es PostgreSQL

PostgreSQL es un motor de base de datos relacional.

Se usa porque permite:

- Guardar datos estructurados
- Consultar con SQL
- Relacionar tablas
- Mantener integridad
- Escalar mejor que archivos planos

En este proyecto PostgreSQL almacena la información real del sistema.

---

# 19. Cómo ingresar a Supabase

Pasos:

1. Entrar a:

    https://supabase.com

2. Iniciar sesión con la cuenta correspondiente
3. Seleccionar el proyecto correcto
4. Entrar a Table Editor para ver tablas
5. Entrar a SQL Editor para ejecutar consultas
6. Entrar a Settings si se requiere revisar conexión

Nunca guardar contraseñas reales dentro del código.

No compartir:

- DATABASE_URL real
- password
- tokens
- claves secretas

---

# 20. Tablas principales

## empleados

Guarda la información del personal.

Campos comunes:

- cedula
- nombre_completo
- cargo
- proyecto
- zona
- estado

## formaciones

Guarda las charlas o capacitaciones.

Campos comunes:

- id_formacion
- nombre_formacion
- fecha_asistencia
- formador
- clasificacion_formacion
- tipo_formacion

## asistencias

Guarda los registros de asistencia.

Campos comunes:

- id_asistencia
- id_formacion
- cedula
- fecha_registro
- puntaje
- respuestas

---

# 21. Flujo correcto para hacer cambios

Este es el flujo más importante como desarrollador.

## Paso 1: Abrir VS Code

Abrir la carpeta del proyecto.

Ejemplo:

    DevData_Academy

## Paso 2: Editar archivo

Modificar el archivo necesario.

Ejemplo:

    pages/22_📋_Portal_Formacion_Elite.py

## Paso 3: Probar localmente

Ejecutar:

    streamlit run app.py

Abrir en navegador:

    http://localhost:8501

## Paso 4: Validar

Revisar:

- Que la app abra
- Que el módulo cargue
- Que no haya errores rojos
- Que se vea bien en pantalla
- Que no se rompa el menú

## Paso 5: Revisar Git

Ejecutar:

    git status

## Paso 6: Agregar cambios

Ejecutar:

    git add .

## Paso 7: Crear commit

Ejecutar:

    git commit -m "actualiza documentacion portal formacion elite"

## Paso 8: Subir a GitHub

Ejecutar:

    git push origin main

## Paso 9: Esperar Streamlit Cloud

Streamlit Cloud detecta cambios desde GitHub.

## Paso 10: Validar producción

Abrir la URL real desde navegador o celular.

---

# 22. Comandos Git principales

## Ver estado

    git status

## Agregar todos los cambios

    git add .

## Crear commit

    git commit -m "mensaje claro del cambio"

## Subir cambios

    git push origin main

## Descargar cambios

    git pull origin main

## Ver repositorio remoto

    git remote -v

## Ver rama actual

    git branch

---

# 23. Error común: permiso denegado en GitHub

Error:

    Permission to agaviria-projects/devdata-academy.git denied to elite-sst

Significa:

Git está intentando subir cambios con una cuenta que no tiene permisos.

Ejemplo:

| Repositorio | Cuenta correcta |
|---|---|
| agaviria-projects/devdata-academy | agaviria-projects |

Si aparece elite-sst, significa que Windows o GitHub quedó autenticado con otra cuenta.

Solución general:

1. Revisar cuenta activa en GitHub
2. Cerrar sesión de la cuenta incorrecta
3. Borrar credenciales de Windows si es necesario
4. Volver a iniciar sesión con la cuenta correcta
5. Repetir git push origin main

---

# 24. Cómo probar localmente

Comando:

    streamlit run app.py

URL local:

    http://localhost:8501

Importante:

La URL local solo funciona en mi computador.

Un usuario externo no puede entrar a localhost.

Localhost sirve para probar antes de subir a producción.

---

# 25. Diferencia entre localhost y producción

| Ambiente | URL | Quién lo ve |
|---|---|---|
| Local | localhost:8501 | Solo yo |
| Producción | streamlit.app | Usuarios reales |

Ejemplo local:

    http://localhost:8501

Ejemplo producción:

    https://elite-sst.streamlit.app

---

# 26. Cómo subir cambios a la nube

Para subir cambios:

1. Guardar archivo
2. Probar local
3. Ejecutar git status
4. Ejecutar git add .
5. Ejecutar git commit
6. Ejecutar git push
7. Esperar Streamlit Cloud
8. Validar en producción

Comandos:

    git status
    git add .
    git commit -m "ajustes portal formacion"
    git push origin main

---

# 27. Qué hacer si Streamlit Cloud no actualiza

Si la app no muestra cambios:

1. Confirmar que el push llegó a GitHub
2. Entrar a Streamlit Cloud
3. Abrir Manage App
4. Revisar logs
5. Usar Reboot App
6. Usar Clear Cache si aplica
7. Usar Redeploy si aplica

Ruta común:

    Manage App
        ↓
    Reboot App

O también:

    Manage App
        ↓
    Clear Cache
        ↓
    Reboot App

---

# 28. Qué hacer cuando aparece Zzzz

Cuando aparece Zzzz significa que la app está dormida.

Esto puede pasar en Streamlit Cloud gratuito.

Qué hacer:

1. Abrir la app antes de la capacitación
2. Esperar que despierte
3. Navegar por los módulos
4. Probar una URL de asistencia
5. Confirmar que carga correctamente

No esperar hasta el último minuto.

---

# 29. Recomendación antes de una capacitación real

Antes de una capacitación:

1. Abrir app de producción
2. Confirmar que no está dormida
3. Abrir módulo Admin
4. Crear o validar formación
5. Copiar URL pública
6. Probar URL en celular
7. Registrar asistencia de prueba
8. Descargar Excel de prueba
9. Validar que el empleado aparezca correctamente
10. Compartir URL al grupo

---

# 30. Prueba mínima antes de producción

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

# 31. Prueba con dos celulares

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

# 32. Buenas prácticas como desarrollador

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

---

# 33. Riesgos del sistema

| Riesgo | Impacto |
|---|---|
| App dormida | Usuarios no pueden entrar rápido |
| Mala cuenta GitHub | No deja hacer push |
| Error SQL | No guarda información |
| Empleado inactivo | No permite registro |
| URL incorrecta | Entra a formación equivocada |
| No probar celular | Puede fallar en operación real |
| Modificar preguntas usadas | Puede afectar trazabilidad |

---

# 34. Recomendaciones técnicas

- Mantener una documentación dentro de DevData Academy
- Guardar comandos importantes
- Tener claro qué cuenta GitHub usa cada proyecto
- Revisar Streamlit Cloud antes de eventos reales
- Validar Supabase si algo no guarda
- Usar reportes Excel como respaldo operativo
- Hacer pruebas pequeñas antes de pruebas masivas

---

# 35. Checklist rápido de operación

Antes de capacitación:

| Paso | Validado |
|---|---|
| App despierta | Pendiente |
| Formación creada | Pendiente |
| URL copiada | Pendiente |
| Celular probado | Pendiente |
| Cédula activa probada | Pendiente |
| Reporte Excel probado | Pendiente |
| Base de datos responde | Pendiente |
| Mensajes correctos | Pendiente |

---

# 36. Checklist rápido de despliegue

Antes de subir cambios:

| Paso | Validado |
|---|---|
| Probé localmente | Pendiente |
| No hay error rojo | Pendiente |
| Guardé archivo | Pendiente |
| Ejecuté git status | Pendiente |
| Ejecuté git add . | Pendiente |
| Ejecuté git commit | Pendiente |
| Ejecuté git push | Pendiente |
| Validé Streamlit Cloud | Pendiente |
| Probé producción | Pendiente |

---

# 37. Orden correcto cuando olvide qué hacer

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
10. Entrar a Streamlit Cloud
11. Verificar redeploy
12. Abrir app en producción
13. Probar desde celular
14. Descargar Excel si aplica

---

# 38. Frase clave para recordar

Guardar en VS Code no actualiza la app del usuario.

El usuario solo ve cambios cuando:

    código guardado
        ↓
    commit realizado
        ↓
    push a GitHub
        ↓
    Streamlit Cloud redeploy
        ↓
    producción validada

---

# 39. Conclusión

Este sistema no es solo una app en Streamlit.

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

Por eso esta documentación debe mantenerse actualizada dentro de DevData Academy.

La documentación evita depender de la memoria y permite recordar en el futuro:

- Cómo entrar
- Qué revisar
- Qué hacer primero
- Cómo probar
- Cómo desplegar
- Cómo corregir errores
- Cómo operar el sistema antes de una capacitación

---

""")