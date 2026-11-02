# La inscripción se conserva y puede reactivarse

Una inscripción cancelada conserva su historial y puede ser reactivada por el mismo alumno mediante una reinscripción, siempre que la actividad esté habilitada, no haya comenzado y tenga cupo disponible. Se conserva una única inscripción por alumno y actividad y cada cancelación se registra por separado: así se permite volver a ocupar un cupo sin perder las decisiones anteriores ni duplicar la inscripción.

## Considered Options

- **Borrar la fila.** No queda rastro de las cancelaciones y una reinscripción sería indistinguible de una primera inscripción.
- **Conservar una única fecha de cancelación en la inscripción.** Es simple, pero al reinscribir y cancelar nuevamente se perdería el historial anterior.
- **Conservar una inscripción reactivable y registrar cada cancelación en su historial.** Elegida: mantiene la unicidad de la inscripción, permite varios períodos vigentes y conserva cada decisión de cancelación.

## Consequences

- El `UniqueConstraint(student, activity)` sigue significando "una inscripción por alumno y actividad". Reinscribirse reactiva esa inscripción; no crea una segunda.
- La reinscripción requiere actividad habilitada, no iniciada y con cupo disponible. Puede ocurrir hasta antes del inicio; la ventana de cancelación de 24 horas no la limita.
- Cada cancelación se registra por separado. Volver a cancelar una reinscripción aplica la ventana vigente (hasta 24 horas antes del inicio), incluso si la actividad está deshabilitada.
- El historial de cancelaciones es visible para el alumno en el detalle y en "Mis inscripciones", y para el docente en el detalle de la actividad.
- Todo cálculo de ocupación debe filtrar canceladas: disponibilidad, validación de capacidad del docente y cualquier conteo futuro.
- `seed_demo` no recrea canceladas porque ya verifica existencia sin filtrar estado; esa propiedad queda cubierta por una prueba.
- La ventana de cancelación es inclusiva en su borde (a las 24:00:00 exactas todavía se puede), al revés que el inicio de la actividad, que rechaza el instante exacto. La asimetría es deliberada: el límite pertenece al lado que rechaza, y en la cancelación el rechazo empieza después de las 24 h.
