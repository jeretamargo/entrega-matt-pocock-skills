# Inscripciones UNTDF

Dominio de la demo docente: alumnos que reservan cupos en actividades y docentes que las habilitan.

## Language

**Actividad**:
Un encuentro ofrecido a la comunidad universitaria, con fecha de inicio, capacidad y estado de habilitación.
_Avoid_: Evento, curso, clase

**Inscripción**:
Vínculo entre un alumno y una actividad que reserva un cupo mientras está vigente. Cada alumno tiene como máximo una inscripción por actividad; puede volver a estar vigente después de una cancelación.
_Avoid_: Registro, reserva, alta

**Cancelación**:
Decisión del alumno de renunciar a su inscripción dentro de la ventana de cancelación. La inscripción deja de ocupar cupo y cada cancelación, junto con el instante en que se decidió, se conserva en su historial.
_Avoid_: Baja, anulación, borrado, desinscripción

**Reinscripción**:
Reactivación de una inscripción cancelada del mismo alumno en la misma actividad. Requiere que la actividad esté habilitada, no haya comenzado y tenga cupo disponible; el historial de cancelaciones anteriores se conserva.
_Avoid_: Nueva inscripción

**Ventana de cancelación**:
Período en el que el alumno puede cancelar: desde que se inscribe hasta 24 horas antes del inicio de la actividad.
_Avoid_: Plazo de baja, fecha límite

**Cupo disponible**:
Cantidad de lugares que una actividad todavía puede ofrecer: su capacidad menos las inscripciones vigentes.
_Avoid_: Vacante, lugar, disponibilidad (como sinónimo de cantidad)

**Alumno**:
Persona autenticada que se inscribe y cancela sus propias inscripciones.
_Avoid_: Estudiante, usuario

**Docente**:
Persona con acceso a la administración; habilita actividades y consulta inscripciones, pero no inscribe ni cancela por otros.
_Avoid_: Profesor, administrador
