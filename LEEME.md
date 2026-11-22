# Kit de datos y respaldo de AmbientIA

CoAfina 2026 · Dirección de Ambiente de Villa Yacanto · Revisión de accesos y condiciones del 22 de noviembre de 2026

Este kit ayuda a construir matches ambientales explicables entre comunidades de América Latina y el Caribe. Reúne las siete fuentes propuestas, cinco recursos adicionales y una copia pequeña de datos reales para seguir trabajando si falla un portal. Los recursos extra son opcionales y no amplían las exigencias del reto.

## Cómo empezar

Abrí datos/localidades_latam_caribe_geonames.csv para seleccionar comunidades. Contiene nombres, coordenadas y códigos administrativos. Usá NaturalEarth_paises_110m.zip como contexto continental sin depender de teselas web. Los JSON de Climate TRACE permiten ensayar la lectura de sitios documentados y sus emisiones estimadas.

La copia contiene 32.871 localidades y 15 registros de residuos repartidos entre Argentina, Ecuador, Colombia, República Dominicana y Cuba. Sirve para probar integración e interfaz; todavía deberán elegirse áreas de comparación y extraerse indicadores ambientales. Las provincias de Argentina y Ecuador son ejemplos de polígonos, no límites de las comunidades elegidas.

## Qué está efectivamente respaldado

La carpeta datos incluye los archivos que figuran en documentacion/verificacion_y_huellas.json. Ese registro conserva URL, fecha, tamaño y huella SHA256. Las comprobaciones de portales y respuestas pequeñas no equivalen a una descarga completa de todos los datos. Dynamic World está documentado, pero no se realizó una exportación autenticada de Earth Engine.

## Si algo falla

Primero usá el archivo local. Después consultá el acceso alternativo de fuentes.csv. Si cambia la fuente o el período, registralo y recalculá las comparaciones con criterios homogéneos. Una variable faltante debe mostrarse como desconocida y nunca convertirse automáticamente en cero.

# Accesos de las fuentes principales

## GeoNames para localizar comunidades

Licencia CC BY 4.0. La copia local filtra cities500 por los códigos de países y territorios detallados en documentacion/seleccion_geografica.json. La población incluida es un atributo de GeoNames y no reemplaza GHS POP para analizar evolución demográfica.

https://download.geonames.org/export/dump/cities500.zip

https://download.geonames.org/export/dump/readme.txt

## BasinATLAS para el contexto de cuenca

Licencia CC BY 4.0. Descarga global en geodatabase de aproximadamente 2,70 GB; no incluida en el ZIP. El repositorio conserva catálogo y documentación. El segundo portal orienta hacia el mismo alojamiento: si Figshare falla, ese enlace por sí solo no garantiza otra descarga. Preparar un recorte propio antes de la demostración.

https://doi.org/10.6084/m9.figshare.9890531

https://www.hydrosheds.org/hydroatlas

## GHS POP y GHS BUILT S para población y superficie construida

Ambas distribuciones declaran CC BY 4.0 en sus archivos copyright.txt. Los accesos directos específicos están en fuentes.csv: 2020 a 1 km, aproximadamente 322,29 MB y 152,53 MB respectivamente. No se incluyen esos raster globales. Las rutas usan V1-0 en la carpeta y V1_0 en el nombre del ZIP. No son espejos independientes.

https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/GHSL/GHS_POP_GLOBE_R2023A/

https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/GHSL/GHS_BUILT_S_GLOBE_R2023A/

Conservar proyección espacial, resolución, período y naturaleza del dato. En GHS POP 2025 y 2030 son proyecciones de esta edición. No tratar resultados interpolados o extrapolados como mediciones directas de cada año.

# Coberturas y residuos con acceso alternativo

## ESA WorldCover

Datos CC BY 4.0. Si Zenodo falla, existe alojamiento público de teselas COG en AWS. Se comprobó la respuesta de una tesela de Córdoba de aproximadamente 73,30 MB, sin descargarla completa. Su URL está en fuentes.csv. El repositorio oficial explica cómo seleccionar países o cajas geográficas; no se debe descargar todo el mundo por defecto.

https://zenodo.org/records/7254221

https://github.com/ESA-WorldCover/esa-worldcover-datasets

## Global Forest Change

Datos CC BY 4.0. Descarga por teselas y listas de URLs en la página oficial. Se comprobó una tesela de lossyear para el norte de Sudamérica. El visor sirve para explorar y no es otro alojamiento del archivo. La alternativa en Earth Engine requiere acceso habilitado; no se presupone que todos los equipos lo tengan.

https://storage.googleapis.com/earthenginepartners-hansen/GFC-2025-v1.13/download.html

## Climate TRACE

Licencia general CC BY 4.0 con excepciones identificadas en los términos. Conservar procedencia, subsector, gas, año y unidad de cada registro. La API beta se respalda con el portal de descargas y con las muestras locales efectivamente obtenidas. Los ejemplos consultan tres fuentes por país: no son una muestra estadística ni un inventario completo.

https://climatetrace.org/data

https://climatetrace.org/terms

Consulta real de ejemplo: https://api.climatetrace.org/v7/sources?year=2024&subsectors=solid-waste-disposal&gadmId=ARG&limit=3

No agrupar rellenos sanitarios y basurales como si fueran equivalentes. assetType ayuda a distinguir las categorías, pero no certifica su estado legal ni su situación actual.

# Recursos adicionales de territorio

## geoBoundaries gbOpen

Útil para definir áreas de agregación cuando se necesitan polígonos administrativos. El proyecto ofrece gbOpen como compatible con CC BY 4.0, pero cada respuesta conserva la licencia de origen. Se comprobó que Argentina ADM1 declara CC BY 2.5 y Ecuador ADM1 CC0. Esos metadatos se incluyen junto con las geometrías que se hayan descargado. No atribuir automáticamente una única licencia a todos los archivos.

https://www.geoboundaries.org/api.html

https://www.geoboundaries.org/api/current/gbOpen/ECU/ADM1/

La API devuelve enlaces versionados a GitHub. Para otro país, cambiar el ISO3 y comprobar el nivel disponible. ADM1 identifica provincias o equivalentes; no asumir que ADM2 significa municipio en todos los países. Revisar año, nombres y correspondencia antes de unir localidades y polígonos.

## Natural Earth

Datos en dominio público. Incluimos el ZIP de países a escala 1:110 millones, de unos 215 KB, para disponer de un mapa de contexto sin internet. Se carga como vector en QGIS y puede convertirse a GeoJSON. No requiere teselas web ni credenciales. No sirve para delimitar un área local ni representar exhaustivamente pequeñas islas del Caribe.

https://www.naturalearthdata.com/downloads/110m-cultural-vectors/110m-admin-0-countries/

https://www.naturalearthdata.com/about/terms-of-use/

Estos dos recursos ayudan a dibujar y delimitar territorios, pero no sustituyen los atributos hidroambientales de BasinATLAS. Si se usa un radio alrededor de una localidad como unidad de análisis, documentar el radio y calcular superficies en una proyección adecuada; no medir distancias como si grados fueran metros.

# Recursos adicionales de ambiente e infraestructura

## OpenStreetMap y Geofabrik

Datos bajo ODbL 1.0. Pueden aportar caminos, instalaciones de reciclaje y sitios etiquetados como landfill. Geofabrik ofrece descargas por regiones; para Caribe y Centroamérica usar el selector global. El esquema de formatos varía por país. El ejemplo consultas_residuos_overpass.txt está preparado para una zona pequeña y no se ha ejecutado: no promete encontrar sitios.

https://download.geofabrik.de/

https://www.openstreetmap.org/copyright

La base de datos, las teselas y el servicio de consultas son cosas distintas. No descargar masivamente teselas de tile.openstreetmap.org. Si el servidor cartográfico falla, mostrar el vector local. Una base derivada distribuida puede quedar sujeta a compartir bajo ODbL; separar el código propio y documentar la integración.

## Dynamic World V1

Datos CC BY 4.0, nueve categorías de cobertura a 10 m desde 2015. Es una ampliación avanzada para analizar períodos recientes, no un reemplazo directo de WorldCover. Su uso analítico mediante Earth Engine requiere proyecto habilitado, registro y permisos. No hay exportación autenticada incluida en este kit.

https://developers.google.com/earth-engine/datasets/catalog/GOOGLE_DYNAMICWORLD_V1

## JRC Global Surface Water

El productor indica condiciones Copernicus, acceso gratuito y reconocimiento de la fuente; no lo rotulamos automáticamente CC BY 4.0. La documentación vigente describe V1.5 y actualización hasta 2024. Se comprobó la respuesta del servicio WMTS 2024. Es visualización, no una descarga de valores para análisis. El acceso raster está en el portal; revisar las notas de corrección y consistencia temporal.

https://global-surface-water.appspot.com/download

Puede aportar presencia y persistencia de agua superficial. No equivale a calidad del agua, caudal, disponibilidad potable o peligro de inundación.

# Licencias y atribuciones listas para usar

Que una página deje de responder no elimina por sí mismo una licencia ya otorgada. CC BY 4.0 establece que las libertades concedidas no son revocables mientras se cumplan sus términos. Esto no subsana un error de licencia de origen ni concede derechos sobre material de terceros. Conservar la versión descargada, su procedencia y las condiciones aplicables.

https://creativecommons.org/licenses/by/4.0/

## Registro mínimo por fuente

Guardar nombre y versión, URL de descarga, autor o proveedor, licencia y su enlace, fecha de acceso, período representado, resolución, extensión territorial, transformaciones y limitaciones. Separar licencia del código, de los datos y de servicios externos. fuentes.csv es un catálogo; completar además registro_derivados.csv con los productos de cada equipo.

## Créditos para adaptar

GeoNames — CC BY 4.0. Selección y transformación para AmbientIA. Consulta: 22 de noviembre de 2026.

BasinATLAS v1.0 — Linke et al. 2019, HydroATLAS. CC BY 4.0. DOI 10.1038/s41597-019-0300-6. Indicar recorte e indicadores utilizados.

GHS POP y GHS BUILT S R2023A — European Commission, Joint Research Centre. CC BY 4.0. Añadir la cita específica de cada producto y los períodos usados.

© ESA WorldCover project 2021 / Contains modified Copernicus Sentinel data (2021) processed by ESA WorldCover consortium. Añadir Zanaga et al. 2022 y DOI 10.5281/zenodo.7254221.

Global Forest Change — Source: Hansen/UMD/Google/USGS/NASA. CC BY 4.0. Indicar v1.13 y citar Hansen et al. 2013.

Climate TRACE — Climate TRACE Emissions Inventory, versión y fecha de consulta de la descarga. CC BY 4.0 salvo excepciones aplicables. No inventar la versión de una respuesta API que no la informa.

Natural Earth — dominio público. Crédito opcional: Made with Natural Earth. OSM: © OpenStreetMap contributors, con enlace a copyright y ODbL. geoBoundaries: citar proyecto y metadatos originales del archivo.

Dynamic World exige el crédito específico publicado en su catálogo. JRC Global Surface Water solicita Source: EC JRC/Google y la cita de Pekel et al. 2016. Los enlaces de respaldo se conservan en fuentes.csv.

# Plan de contingencia y mensaje para los equipos

## Si falla una descarga o un servicio

Portal inaccesible: usar la copia local y conservar su fecha. API inaccesible: leer los JSON descargados y señalar el modo de demostración. Earth Engine sin acceso: trabajar con archivos descargables de otras fuentes y omitir Dynamic World. Teselas caídas: mostrar Natural Earth o polígonos propios en el mapa sin fondo remoto.

Si falta una variable en algunos territorios, calcular similitud solo con variables comparables, mostrar cobertura de información y evitar que pocos datos produzcan matches aparentemente perfectos. Si cambia una fuente, recalcular esa variable para todas las comunidades del grupo o explicar por qué no son comparables.

## Alcance viable

Comenzar con pocas comunidades de al menos dos países, variables justificadas y un método sencillo. Ampliar después. No es obligatorio integrar todas las fuentes. Los datos adicionales son oportunidades para mejorar la propuesta y no nuevos criterios de evaluación. No se garantiza un conjunto homogéneo y exhaustivo para cada localidad de LATAM y el Caribe.

## Texto para publicar en Discord

¡Hola, equipo! Les compartimos el kit de apoyo de AmbientIA: accesos a las fuentes, condiciones de uso, alternativas y pequeñas muestras reales para que puedan empezar. Incluye localidades de LATAM y el Caribe, ejemplos de sitios de disposición de residuos y cartografía de contexto. No tienen que usar todo: elijan lo que aporte a su propuesta y expliquen por qué. Si un servicio falla, usen las copias incluidas y registren la versión. Detrás de cada match tiene que poder verse qué conecta a las comunidades, qué las diferencia y qué información falta. ¡Nos encontramos en el canal del reto para acompañar ese proceso!

## Antes de la demostración

Abrir la solución sin depender de consultas en vivo. Revisar atribuciones visibles y README. Confirmar que otra persona pueda ejecutar el proyecto. Mostrar un match con datos faltantes y explicar el resultado. Actualizar solo las fuentes que cambien y conservar la copia usada para la entrega.

Verificar el kit: ejecutar python verificar_copias.py desde la carpeta descomprimida. Requiere Python 3 y no instala paquetes. Repite los hashes de las copias incluidas, no certifica contenido, vigencia jurídica ni disponibilidad futura.
