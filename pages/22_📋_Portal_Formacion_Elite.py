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
st.caption("Documentación técnica y operativa del sistema de capacitaciones")

# =========================================================
# DOCUMENTACIÓN
# =========================================================

st.markdown("""

# 📋 Portal de Formación Elite

---

# 1. Objetivo del sistema

El Portal de Formación Elite fue desarrollado para:

- Gestionar capacitaciones internas y externas
- Registrar asistencia desde celular
- Validar empleados activos
- Aplicar evaluaciones automáticas
- Generar reportes Excel
- Llevar trazabilidad de formaciones
- Centralizar información de capacitación

El sistema está orientado a procesos empresariales reales y operación en campo.

---

# 2. Arquitectura general

| Componente | Función |
|---|---|
| Streamlit | Frontend y lógica visual |
| Supabase | Backend en la nube |
| PostgreSQL | Base de datos relacional |
| Streamlit Cloud | Hosting de la aplicación |
| GitHub | Versionamiento |
| SQLAlchemy | Conexión Python ↔ PostgreSQL |

---

# 3. Tecnologías utilizadas

## Backend

- Python
- Streamlit
- SQLAlchemy
- psycopg2

## Base de datos

- PostgreSQL
- Supabase

## Despliegue

- Streamlit Cloud
- GitHub

## Reportería

- pandas
- openpyxl

---

# 4. Cómo ingresa el administrador / formador

El administrador ingresa desde:

- Panel Admin
- Sidebar principal
- Módulo de gestión

Funciones disponibles:

- Crear formación
- Consultar formaciones
- Editar preguntas
- Descargar reportes
- Gestionar empleados

---

# 5. Cómo ingresa el empleado por URL pública

El empleado NO necesita usuario ni contraseña.

Ingresa mediante URL pública generada automáticamente.

Ejemplo:

    https://app-capacitaciones.streamlit.app/Asistencia?formacion=15

La URL llega por:

- WhatsApp
- Teams
- Correo
- QR
- Grupo operativo

---

# 6. Cómo crear una charla

Flujo:

1. Ingresar a Admin
2. Crear formación
3. Seleccionar:
   - Clasificación: CHARLA
4. Guardar
5. Generar URL pública

Las charlas normalmente:

- No llevan preguntas
- Solo registran asistencia

---

# 7. Cómo crear una capacitación con preguntas

Flujo:

1. Crear formación
2. Seleccionar:
   - Clasificación: CAPACITACIÓN
3. Agregar preguntas
4. Agregar respuestas
5. Definir respuesta correcta
6. Guardar

El sistema luego:

- Evalúa respuestas
- Calcula puntaje
- Guarda resultados

---

# 8. Cómo editar preguntas y respuestas

Ruta:

Consultar / Editar → Formación

Desde allí se puede:

- Editar preguntas
- Cambiar respuestas
- Corregir opciones
- Agregar nuevas preguntas

IMPORTANTE:

Si la formación ya fue utilizada, modificar preguntas puede alterar trazabilidad histórica.

---

# 9. Explicación de la URL

La URL NO cambia.

Depende del ID interno de la formación.

Ejemplo:

    ?formacion=15

Mientras exista el ID:

- La URL seguirá funcionando
- Puede reutilizarse
- Puede compartirse nuevamente

---

# 10. Registro de asistencia desde celular

Flujo empleado:

1. Abrir URL
2. Ingresar cédula
3. Validación automática
4. Mostrar datos:
   - Nombre
   - Cargo
   - Proyecto
   - Zona
5. Responder preguntas
6. Registrar asistencia

Todo funciona desde navegador móvil.

---

# 11. Limpieza automática después del registro

Después de registrar asistencia:

- Se limpia la cédula
- Se limpian respuestas
- Se limpian datos cargados
- Se reinicia formulario

Objetivo:

Evitar registros duplicados por el siguiente empleado.

---

# 12. Reportes y descarga Excel

El administrador puede descargar:

- Asistencias
- Puntajes
- Consolidado
- Históricos

Formato:

- Excel .xlsx

Incluye:

| Campo |
|---|
| Cédula |
| Nombre |
| Cargo |
| Proyecto |
| Zona |
| Formación |
| Fecha |
| Puntaje |

---

# 13. Consolidado mensual

El sistema permite:

- Consolidar capacitaciones por mes
- Revisar cumplimiento
- Validar participación
- Exportar información gerencial

Ideal para:

- SST
- Gestión humana
- Auditoría
- Indicadores

---

# 14. Gestión empleados activos e inactivos

Cada empleado posee estado:

| Estado | Resultado |
|---|---|
| Activo | Puede registrar asistencia |
| Inactivo | Bloqueado |

Validación automática:

- Evita registros inválidos
- Controla personal retirado

---

# 15. ¿Qué es Supabase?

Supabase es una plataforma cloud que permite:

- Crear bases de datos PostgreSQL
- Gestionar autenticación
- Crear APIs
- Almacenar información

En este proyecto se usa como:

- Backend principal
- Hosting de base de datos

---

# 16. ¿Qué es PostgreSQL?

PostgreSQL es una base de datos relacional profesional.

Ventajas:

- Alta estabilidad
- Escalable
- Compatible con SQL
- Excelente rendimiento
- Muy usada empresarialmente

---

# 17. Cómo ingresar a Supabase

Pasos:

1. Ir a:

    https://supabase.com

2. Iniciar sesión
3. Seleccionar proyecto
4. Entrar a:
   - Table Editor
   - SQL Editor
   - Settings

IMPORTANTE:

Nunca compartir:

- Passwords
- DATABASE_URL reales
- Claves SECRET

---

# 18. Tablas principales

## empleados

Información del personal.

Campos comunes:

- cedula
- nombre
- cargo
- zona
- proyecto
- activo

## formaciones

Información de capacitaciones.

Campos:

- id
- nombre
- fecha
- clasificacion

## asistencias

Registros realizados por empleados.

Campos:

- cedula
- id_formacion
- fecha_registro
- puntaje

---

# 19. Flujo correcto para cambios

## Desarrollo recomendado

1. Trabajar localmente
2. Probar cambios
3. Hacer commit
4. Hacer push
5. Esperar despliegue cloud
6. Validar producción

Nunca modificar directamente en producción.

---

# 20. Comandos Git principales

## Inicializar

    git init

## Revisar cambios

    git status

## Agregar archivos

    git add .

## Crear commit

    git commit -m "ajustes portal formacion"

## Subir cambios

    git push origin main

## Descargar cambios

    git pull origin main

---

# 21. Cómo probar localmente

Ejecutar:

    streamlit run app.py

Luego abrir:

    http://localhost:8501

Ventajas:

- Pruebas rápidas
- Sin afectar producción
- Más fácil depurar errores

---

# 22. Cómo subir cambios a la nube

Flujo:

1. Guardar cambios
2. Commit
3. Push GitHub
4. Streamlit Cloud detecta cambios
5. Redeploy automático

---

# 23. Qué hacer si Streamlit Cloud no actualiza

Opciones:

- Clear Cache
- Reboot App
- Redeploy

Ruta:

Manage App → Settings

También validar:

- Que el push sí llegó a GitHub
- Que no existan errores Python

---

# 24. Qué hacer cuando aparece Zzzz

Significa:

La app está dormida.

Ocurre en planes gratuitos.

Solución:

- Abrir la app unos minutos antes
- Navegar entre módulos
- Esperar reactivación

---

# 25. Recomendación antes de una capacitación

Antes de iniciar:

✅ Abrir app  
✅ Probar URL  
✅ Registrar prueba  
✅ Verificar internet  
✅ Confirmar base de datos  
✅ Validar exporte Excel  

---

# 26. Prueba mínima antes de producción

Realizar:

- Registro completo
- Validación de empleado
- Validación puntaje
- Descarga Excel
- Revisión celular

---

# 27. Prueba con dos celulares

Recomendado:

- Android
- iPhone

Objetivo:

- Validar responsive
- Detectar errores visuales
- Confirmar compatibilidad

---

# 28. Mensajes esperados del sistema

## Registro exitoso

    ✅ Asistencia registrada correctamente

## Puntaje

    🎯 Puntaje obtenido: 80%

## Cédula repetida

    ⚠️ La cédula ya registró asistencia

## Empleado inactivo

    ❌ Empleado inactivo o no encontrado

---

# 29. Buenas prácticas

✅ Probar local primero  
✅ Usar nombres claros  
✅ Mantener respaldos  
✅ Validar datos antes de guardar  
✅ Evitar borrar históricos  
✅ Documentar cambios importantes  

---

# 30. Riesgos y recomendaciones

## Riesgos

- Mala conexión internet
- App dormida
- Datos duplicados
- Cambios sin pruebas
- Eliminación accidental

## Recomendaciones

- Probar siempre antes
- Tener respaldo Excel
- Hacer pruebas móviles
- Mantener GitHub actualizado
- No modificar producción directamente

---

# 31. Conclusión

Portal Formación Elite permite:

- Digitalizar capacitaciones
- Automatizar asistencia
- Centralizar información
- Mejorar trazabilidad
- Generar reportes empresariales

La arquitectura Streamlit + Supabase + PostgreSQL permite un sistema:

- Flexible
- Escalable
- Moderno
- Accesible desde celular
- Fácil de mantener

---

# 📌 Resumen rápido operativo

| Acción | Responsable |
|---|---|
| Crear formación | Administrador |
| Compartir URL | Formador |
| Registrar asistencia | Empleado |
| Descargar Excel | Administrador |
| Validar pruebas | Equipo TI |

---

# 🚀 Estado del proyecto

Portal actualmente preparado para:

- Operación empresarial
- Registro móvil
- Reportería
- Evaluaciones
- Escalabilidad futura

""")