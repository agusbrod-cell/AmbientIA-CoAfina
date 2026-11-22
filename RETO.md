# Qué construir en AmbientIA

## Objetivo

Desarrollar una solución digital reproducible que permita seleccionar una comunidad de América Latina y el Caribe, descubrir comunidades ambientalmente afines en otros países y explorar los resultados mediante mapas y comparaciones comprensibles. Puede integrar plataforma web, dashboard, API y otras herramientas elegidas por el equipo.

## Recorrido esperado

1. Elegir una comunidad de origen.
2. Consultar un perfil territorial construido con indicadores de fuentes abiertas.
3. Obtener comunidades recomendadas de otros países.
4. Abrir una comparación que explique las variables que sostienen el match, las diferencias y la información ausente.
5. Identificar las fuentes, períodos y limitaciones de los datos usados.

No basta con recomendar la comunidad más cercana geográficamente. El equipo debe justificar qué entiende por afinidad ambiental y cómo representa características, transformaciones y presiones del territorio.

## Trabajo de datos

Definan primero la unidad de comparación: un radio alrededor de la localidad, un polígono administrativo u otra unidad justificada. GeoNames ofrece puntos, no límites municipales. Una subcuenca no es lo mismo que un municipio.

Seleccionen variables disponibles y comparables. Normalicen escalas cuando corresponda y documenten pesos y tratamiento de faltantes. Eviten que una dimensión aparezca repetida a través de varios indicadores y domine el ranking sin justificación.

Los sitios de residuos documentados son una presión posible, no una variable obligatoria para cada comunidad. No conviertan ausencia de registros en cero residuos. Distancias o presencia cercana tampoco demuestran impacto sobre una población.

## Método y explicación

Pueden usar similitud, agrupamiento o sistemas de recomendación. Si incorporan IA, indiquen su función y comparen resultados con una referencia sencilla. No hace falta entrenar un modelo grande ni usar un modelo de lenguaje.

Mostrá, por ejemplo, un ranking explicable con las variables utilizadas y el grado de información disponible. Un match con pocos datos requiere cautela y no debería aparentar la misma solidez que uno bien documentado. Una recomendación no certifica equivalencia entre comunidades ni transferibilidad de una solución ambiental.

## Entrega sugerida

- Prototipo consultable y demostración de un match entre países.
- Código e instrucciones de ejecución con dependencias y requisitos de acceso.
- Fuentes, licencias y transformaciones documentadas.
- Explicación del método y comparación con una referencia sencilla.
- Limitaciones y forma de incorporar nuevos territorios.

Los recursos y ejemplos de este repositorio son apoyo opcional. Las orientaciones oficiales de CoAfina rigen la modalidad, los plazos y la entrega del evento.

## Criterios de evaluación

Se considerará el acercamiento al reto y el uso fundamentado de datos abiertos, la funcionalidad y el diseño de la solución, la creatividad y la comunicación. Se valorarán comparaciones ambientalmente pertinentes, explicaciones comprensibles y documentación que permita reproducir y ampliar el trabajo. No se agregan porcentajes ni se exige usar las doce fuentes del catálogo.

## Comunidad y territorio

El propósito es abrir conexiones fundamentadas que permitan a comunidades de LATAM y el Caribe investigar desafíos compartidos e intercambiar experiencias. El prototipo descubre afinidades; las personas y los territorios dan sentido a las futuras colaboraciones.
