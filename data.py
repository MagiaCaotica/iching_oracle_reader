# -*- coding: utf-8 -*-

"""
Este archivo contiene los datos de los 64 hexagramas del I Ching.
Cada hexagrama se representa como un diccionario con la siguiente estructura:
- num: El número del hexagrama (1-64).
- binary: Una tupla de 6 elementos (0 para Yin, 1 para Yang) que representa las líneas de abajo hacia arriba.
- name_ch: El nombre en chino (Pinyin).
- name_es: El nombre en español.
- image: La descripción de la Imagen.
- judgement: La descripción del Juicio.
"""

HEXAGRAM_DATA = [
    {
        "num": 1, "binary": (1, 1, 1, 1, 1, 1), "name_ch": "Qian", "name_es": "Lo Creativo",
        "image": "El movimiento del cielo es poderoso. Así, el hombre superior se hace fuerte e incansable.",
        "judgement": "Lo Creativo obra elevado éxito, propiciando mediante la perseverancia."
    },
    {
        "num": 2, "binary": (0, 0, 0, 0, 0, 0), "name_ch": "Kun", "name_es": "Lo Receptivo",
        "image": "La condición de la tierra es la receptividad devota. Así, el hombre superior, con gran amplitud de carácter, carga con el mundo exterior.",
        "judgement": "Lo Receptivo obra elevado éxito, propiciando mediante la perseverancia de una yegua. Si el hombre superior emprende algo, se extravía; mas si va en seguimiento, encuentra conducción."
    },
    {
        "num": 3, "binary": (0, 1, 0, 0, 0, 1), "name_ch": "Zhun", "name_es": "La Dificultad Inicial",
        "image": "Nubes y trueno: la imagen de la Dificultad Inicial. Así el hombre superior desenreda el ovillo.",
        "judgement": "La Dificultad Inicial obra elevado éxito, propiciando mediante la perseverancia. No debe emprenderse nada. Es propicio designar ayudantes."
    },
    {
        "num": 4, "binary": (1, 0, 0, 0, 1, 0), "name_ch": "Meng", "name_es": "La Necedad Juvenil",
        "image": "Una fuente brota al pie de la montaña: la imagen de la Juventud. Así el hombre superior fomenta su carácter por medio de una minuciosa conducta.",
        "judgement": "La Necedad Juvenil tiene éxito. No soy yo quien busca al joven necio, el joven necio me busca a mí. Al primer oráculo, doy información. Si pregunta dos o tres veces, es una molestia. Cuando molesta, no doy información. La perseverancia es propicia."
    },
    {
        "num": 5, "binary": (0, 1, 0, 1, 1, 1), "name_ch": "Xu", "name_es": "La Espera",
        "image": "Nubes se elevan en el cielo: la imagen de la Espera. Así el hombre superior come y bebe, y está alegre y de buen humor.",
        "judgement": "La Espera. Si eres sincero, tienes luz y éxito. La perseverancia trae buena fortuna. Es propicio cruzar las grandes aguas."
    },
    {
        "num": 6, "binary": (1, 1, 1, 0, 1, 0), "name_ch": "Song", "name_es": "El Conflicto",
        "image": "El cielo y el agua van por caminos contrarios: la imagen del Conflicto. Así el hombre superior, en todos sus asuntos, considera cuidadosamente el principio.",
        "judgement": "El Conflicto. Eres sincero y te encuentras con oposición. Una detención cautelosa a mitad de camino trae buena fortuna. Llevar el asunto hasta el final trae desdicha. Es propicio ver al gran hombre. No es propicio cruzar las grandes aguas."
    },
    {
        "num": 7, "binary": (0, 0, 0, 0, 1, 0), "name_ch": "Shi", "name_es": "El Ejército",
        "image": "En medio de la tierra hay agua: la imagen del Ejército. Así el hombre superior aumenta sus masas por su generosidad hacia el pueblo.",
        "judgement": "El Ejército necesita perseverancia y un hombre fuerte. Buena fortuna sin culpa."
    },
    {
        "num": 8, "binary": (0, 1, 0, 0, 0, 0), "name_ch": "Bi", "name_es": "La Solidaridad",
        "image": "Sobre la tierra está el agua: la imagen de la Solidaridad. Así los antiguos reyes establecieron los diversos estados y mantuvieron relaciones amistosas con los príncipes feudales.",
        "judgement": "La Solidaridad trae buena fortuna. Indaga el oráculo una vez más, si tienes sublimidad, constancia y perseverancia. Entonces no hay culpa. Los inseguros se unen gradualmente. Quien llega demasiado tarde tiene desdicha."
    },
    {
        "num": 9, "binary": (1, 1, 1, 0, 1, 1), "name_ch": "Xiao Chu", "name_es": "La Fuerza Domesticadora de lo Pequeño",
        "image": "El viento sopla por el cielo: la imagen de la Fuerza Domesticadora de lo Pequeño. Así el hombre superior refina la forma exterior de su naturaleza.",
        "judgement": "La Fuerza Domesticadora de lo Pequeño tiene éxito. Nubes densas, sin lluvia de nuestra región occidental."
    },
    {
        "num": 10, "binary": (1, 1, 0, 1, 1, 1), "name_ch": "Lü", "name_es": "El Porte",
        "image": "Arriba el cielo, abajo el lago: la imagen del Porte. Así el hombre superior discrimina entre lo alto y lo bajo, y de este modo consolida los sentimientos del pueblo.",
        "judgement": "Pisar la cola del tigre. No muerde al hombre. Éxito."
    },
    {
        "num": 11, "binary": (0, 0, 0, 1, 1, 1), "name_ch": "Tai", "name_es": "La Paz",
        "image": "El cielo y la tierra se unen: la imagen de la Paz. Así el soberano divide y completa el curso del cielo y la tierra; fomenta y regula los dones del cielo y la tierra, y así ayuda al pueblo.",
        "judgement": "La Paz. Lo pequeño se va y lo grande se acerca. Buena fortuna. Éxito."
    },
    {
        "num": 12, "binary": (1, 1, 1, 0, 0, 0), "name_ch": "Pi", "name_es": "El Estancamiento",
        "image": "El cielo y la tierra no se unen: la imagen del Estancamiento. Así el hombre superior se retira a su valía interior para eludir las dificultades. No permite que le honren con ingresos.",
        "judgement": "El Estancamiento. Los hombres malvados no favorecen la perseverancia del hombre superior. Lo grande se va y lo pequeño se acerca."
    },
    {
        "num": 13, "binary": (1, 1, 1, 1, 0, 1), "name_ch": "Tong Ren", "name_es": "La Comunidad con los Hombres",
        "image": "Arriba el cielo, abajo el fuego: la imagen de la Comunidad con los Hombres. Así el hombre superior organiza los clanes y distingue las cosas.",
        "judgement": "Comunidad con los hombres en campo abierto: éxito. Es propicio cruzar las grandes aguas. La perseverancia del hombre superior es propicia."
    },
    {
        "num": 14, "binary": (1, 0, 1, 1, 1, 1), "name_ch": "Da You", "name_es": "La Posesión en Gran Medida",
        "image": "El fuego en lo alto del cielo: la imagen de la Posesión en Gran Medida. Así el hombre superior reprime el mal y fomenta el bien, y obedece así a la benévola voluntad del cielo.",
        "judgement": "Posesión en Gran Medida. Éxito supremo."
    },
    {
        "num": 15, "binary": (0, 0, 1, 0, 0, 0), "name_ch": "Qian", "name_es": "La Modestia",
        "image": "En medio de la tierra, una montaña: la imagen de la Modestia. Así el hombre superior reduce lo que está en exceso y aumenta lo que es deficiente, para igualar las cosas y hacerlas justas.",
        "judgement": "La Modestia crea éxito. El hombre superior lleva las cosas a su conclusión."
    },
    {
        "num": 16, "binary": (0, 0, 0, 1, 0, 0), "name_ch": "Yu", "name_es": "El Entusiasmo",
        "image": "El trueno sale rugiendo de la tierra: la imagen del Entusiasmo. Así los antiguos reyes hacían música para honrar el mérito, y la ofrecían en abundancia al Dios supremo, invitando a sus antepasados a estar presentes.",
        "judgement": "El Entusiasmo. Es propicio movilizar ejércitos y establecer príncipes."
    },
    {
        "num": 17, "binary": (1, 0, 0, 1, 1, 0), "name_ch": "Sui", "name_es": "El Seguimiento",
        "image": "El trueno en medio del lago: la imagen del Seguimiento. Así el hombre superior, al atardecer, entra a descansar y recuperarse.",
        "judgement": "El Seguimiento tiene éxito supremo. La perseverancia es propicia. Sin culpa."
    },
    {
        "num": 18, "binary": (0, 1, 1, 0, 0, 1), "name_ch": "Gu", "name_es": "El Trabajo en lo Echado a Perder",
        "image": "El viento sopla al pie de la montaña: la imagen de la Decadencia. Así el hombre superior agita al pueblo y fortalece su espíritu.",
        "judgement": "Trabajo en lo Echado a Perder. Éxito supremo. Es propicio cruzar las grandes aguas. Antes del punto de partida, tres días. Después del punto de partida, tres días."
    },
    {
        "num": 19, "binary": (0, 0, 1, 1, 0, 0), "name_ch": "Lin", "name_es": "La Aproximación",
        "image": "La tierra sobre el lago: la imagen de la Aproximación. Así el hombre superior es inagotable en su deseo de enseñar, e ilimitado en su tolerancia y protección del pueblo.",
        "judgement": "La Aproximación tiene éxito supremo. La perseverancia es propicia. Cuando llega el octavo mes, hay desdicha."
    },
    {
        "num": 20, "binary": (0, 0, 1, 1, 1, 0), "name_ch": "Guan", "name_es": "La Contemplación",
        "image": "El viento sopla sobre la tierra: la imagen de la Contemplación. Así los antiguos reyes visitaban las regiones del mundo, contemplaban al pueblo y daban instrucción.",
        "judgement": "La ablución ha sido hecha, pero aún no la ofrenda. Llenos de confianza, levantan la vista hacia él."
    },
    {
        "num": 21, "binary": (1, 0, 0, 1, 0, 1), "name_ch": "Shi He", "name_es": "La Mordedura Tajante",
        "image": "Trueno y relámpago: la imagen de la Mordedura Tajante. Así los antiguos reyes establecían las penas con claridad y hacían cumplir las leyes.",
        "judgement": "La Mordedura Tajante tiene éxito. Es propicio utilizar la justicia."
    },
    {
        "num": 22, "binary": (1, 0, 1, 0, 0, 1), "name_ch": "Bi", "name_es": "La Gracia",
        "image": "Fuego al pie de la montaña: la imagen de la Gracia. Así el hombre superior aclara los asuntos corrientes de la administración, pero no se atreve a decidir así los litigios.",
        "judgement": "La Gracia tiene éxito. En los asuntos pequeños es propicio emprender algo."
    },
    {
        "num": 23, "binary": (0, 0, 0, 0, 0, 1), "name_ch": "Bo", "name_es": "La Desintegración",
        "image": "La montaña descansa sobre la tierra: la imagen de la Desintegración. Así los de arriba sólo pueden asegurar su posición dando generosamente a los de abajo.",
        "judgement": "La Desintegración. No es propicio ir a ninguna parte."
    },
    {
        "num": 24, "binary": (1, 0, 0, 0, 0, 0), "name_ch": "Fu", "name_es": "El Retorno",
        "image": "Trueno dentro de la tierra: la imagen del Retorno. Así los antiguos reyes cerraban los pasos en el solsticio de invierno. Los mercaderes y extranjeros no viajaban, y el soberano no inspeccionaba las provincias.",
        "judgement": "El Retorno. Éxito. Saliendo y entrando sin error. Llegan amigos sin culpa. Va y viene por su camino. Al séptimo día llega el retorno. Es propicio tener un lugar a donde ir."
    },
    {
        "num": 25, "binary": (1, 1, 1, 1, 0, 0), "name_ch": "Wu Wang", "name_es": "La Inocencia",
        "image": "Bajo el cielo ruge el trueno: todas las cosas adquieren su estado natural de inocencia. Así los antiguos reyes, ricos en virtud y en armonía con el tiempo, fomentaban y nutrían a todos los seres.",
        "judgement": "La Inocencia. Éxito supremo. La perseverancia es propicia. Si alguien no es lo que debe ser, tiene desdicha, y no es propicio emprender nada."
    },
    {
        "num": 26, "binary": (1, 1, 1, 0, 0, 1), "name_ch": "Da Chu", "name_es": "La Fuerza Domesticadora de lo Grande",
        "image": "El cielo dentro de la montaña: la imagen de la Fuerza Domesticadora de lo Grande. Así el hombre superior se familiariza con muchas máximas de tiempos antiguos y hechos del pasado, para fortalecer así su carácter.",
        "judgement": "La Fuerza Domesticadora de lo Grande. La perseverancia es propicia. No comer en casa trae buena fortuna. Es propicio cruzar las grandes aguas."
    },
    {
        "num": 27, "binary": (1, 0, 0, 0, 0, 1), "name_ch": "Yi", "name_es": "Las Comisuras de la Boca",
        "image": "Al pie de la montaña, el trueno: la imagen de la Nutrición. Así el hombre superior es cuidadoso con sus palabras y moderado en el comer y el beber.",
        "judgement": "Las Comisuras de la Boca. La perseverancia trae buena fortuna. Presta atención a la nutrición y a lo que un hombre busca para llenar su propia boca."
    },
    {
        "num": 28, "binary": (0, 1, 1, 1, 1, 0), "name_ch": "Da Guo", "name_es": "La Preponderancia de lo Grande",
        "image": "El lago pasa por encima de los árboles: la imagen de la Preponderancia de lo Grande. Así el hombre superior, cuando está solo, no se preocupa, y si tiene que renunciar al mundo, no se inmuta.",
        "judgement": "La Preponderancia de lo Grande. La viga maestra se comba. Es propicio tener un lugar a donde ir. Éxito."
    },
    {
        "num": 29, "binary": (0, 1, 0, 0, 1, 0), "name_ch": "Kan", "name_es": "Lo Abismal",
        "image": "El agua fluye ininterrumpidamente: la imagen de lo Abismal repetido. Así el hombre superior camina en la virtud duradera y practica la enseñanza.",
        "judgement": "Lo Abismal repetido. Si eres sincero, tienes éxito en tu corazón, y lo que haces tiene éxito."
    },
    {
        "num": 30, "binary": (1, 0, 1, 1, 0, 1), "name_ch": "Li", "name_es": "Lo Adherente, el Fuego",
        "image": "La claridad, duplicada: la imagen del Fuego. Así el gran hombre, al continuar esta claridad, ilumina las cuatro partes del mundo.",
        "judgement": "Lo Adherente. La perseverancia es propicia. Trae éxito. Cuidar de la vaca trae buena fortuna."
    },
    {
        "num": 31, "binary": (0, 0, 1, 1, 1, 0), "name_ch": "Xian", "name_es": "La Influencia",
        "image": "Un lago en la montaña: la imagen de la Influencia. Así el hombre superior, por su receptividad, anima a los hombres a acercársele.",
        "judgement": "La Influencia. Éxito. La perseverancia es propicia. Tomar una doncella como esposa trae buena fortuna."
    },
    {
        "num": 32, "binary": (0, 1, 1, 1, 0, 0), "name_ch": "Heng", "name_es": "La Duración",
        "image": "Trueno y viento: la imagen de la Duración. Así el hombre superior se mantiene firme y no cambia de dirección.",
        "judgement": "La Duración. Éxito. Sin culpa. La perseverancia es propicia. Es propicio tener un lugar a donde ir."
    },
    {
        "num": 33, "binary": (1, 1, 1, 1, 0, 0), "name_ch": "Dun", "name_es": "La Retirada",
        "image": "Montaña bajo el cielo: la imagen de la Retirada. Así el hombre superior se mantiene a distancia del hombre inferior, no con ira, sino con reserva.",
        "judgement": "La Retirada. Éxito. En lo pequeño, la perseverancia es propicia."
    },
    {
        "num": 34, "binary": (0, 0, 0, 1, 1, 1), "name_ch": "Da Zhuang", "name_es": "El Poder de lo Grande",
        "image": "El trueno sobre el cielo: la imagen del Poder de lo Grande. Así el hombre superior no pisa caminos que no se ajustan al orden.",
        "judgement": "El Poder de lo Grande. La perseverancia es propicia."
    },
    {
        "num": 35, "binary": (1, 0, 1, 0, 0, 0), "name_ch": "Jin", "name_es": "El Progreso",
        "image": "El sol sale sobre la tierra: la imagen del Progreso. Así el hombre superior ilumina por sí mismo su brillante virtud.",
        "judgement": "El Progreso. Al príncipe poderoso se le honra con caballos en gran número. En un solo día es recibido tres veces."
    },
    {
        "num": 36, "binary": (0, 0, 0, 1, 0, 1), "name_ch": "Ming Yi", "name_es": "El Oscurecimiento de la Luz",
        "image": "La luz se ha hundido en la tierra: la imagen del Oscurecimiento de la Luz. Así el hombre superior vive con la gran multitud: vela su luz, pero sigue brillando.",
        "judgement": "El Oscurecimiento de la Luz. Es propicio ser perseverante en la adversidad."
    },
    {
        "num": 37, "binary": (1, 0, 1, 0, 1, 1), "name_ch": "Jia Ren", "name_es": "La Familia",
        "image": "El viento sale del fuego: la imagen de la Familia. Así el hombre superior tiene sustancia en sus palabras y constancia en su modo de vida.",
        "judgement": "La Familia. La perseverancia de la mujer es propicia."
    },
    {
        "num": 38, "binary": (1, 1, 0, 1, 0, 1), "name_ch": "Kui", "name_es": "La Oposición",
        "image": "Arriba el fuego, abajo el lago: la imagen de la Oposición. Así el hombre superior, en medio de la comunidad, conserva su individualidad.",
        "judgement": "La Oposición. En los asuntos pequeños, buena fortuna."
    },
    {
        "num": 39, "binary": (0, 0, 1, 0, 1, 0), "name_ch": "Jian", "name_es": "El Impedimento",
        "image": "Agua en la montaña: la imagen del Impedimento. Así el hombre superior se vuelve hacia su interior y cultiva su virtud.",
        "judgement": "El Impedimento. El sudoeste es propicio. El noreste no es propicio. Es propicio ver al gran hombre. La perseverancia trae buena fortuna."
    },
    {
        "num": 40, "binary": (0, 1, 0, 1, 0, 0), "name_ch": "Jie", "name_es": "La Liberación",
        "image": "Trueno y lluvia: la imagen de la Liberación. Así el hombre superior perdona los errores y absuelve la culpa.",
        "judgement": "La Liberación. El sudoeste es propicio. Si no hay nada a donde ir, el retorno trae buena fortuna. Si hay algo a donde ir, la prontitud trae buena fortuna."
    },
    {
        "num": 41, "binary": (1, 1, 0, 0, 0, 1), "name_ch": "Sun", "name_es": "La Disminución",
        "image": "Al pie de la montaña, el lago: la imagen de la Disminución. Así el hombre superior controla su ira y reprime sus instintos.",
        "judgement": "La Disminución, combinada con la sinceridad, trae éxito supremo sin culpa. Se puede ser perseverante en ello. Es propicio emprender algo. ¿Cómo se ha de llevar a cabo? Se pueden usar dos pequeñas vasijas para el sacrificio."
    },
    {
        "num": 42, "binary": (1, 0, 0, 0, 1, 1), "name_ch": "Yi", "name_es": "El Aumento",
        "image": "Viento y trueno: la imagen del Aumento. Así el hombre superior: si ve el bien, lo imita; si tiene faltas, las desecha.",
        "judgement": "El Aumento. Es propicio emprender algo. Es propicio cruzar las grandes aguas."
    },
    {
        "num": 43, "binary": (0, 1, 1, 1, 1, 1), "name_ch": "Guai", "name_es": "La Irrupción",
        "image": "El lago ha subido al cielo: la imagen de la Irrupción. Así el hombre superior dispensa riquezas hacia abajo y se abstiene de descansar en su virtud.",
        "judgement": "La Irrupción. Hay que proclamar el asunto resueltamente en la corte del rey. Debe anunciarse con sinceridad. Peligro. Es necesario notificar a la propia ciudad. No es propicio recurrir a las armas. Es propicio emprender algo."
    },
    {
        "num": 44, "binary": (1, 1, 1, 1, 1, 0), "name_ch": "Gou", "name_es": "El Ir al Encuentro",
        "image": "Bajo el cielo, el viento: la imagen de Ir al Encuentro. Así el príncipe difunde sus mandatos y los proclama a las cuatro partes del mundo.",
        "judgement": "Ir al Encuentro. La doncella es poderosa. No se debe tomar a tal doncella."
    },
    {
        "num": 45, "binary": (0, 0, 0, 1, 1, 0), "name_ch": "Cui", "name_es": "La Reunión",
        "image": "Sobre la tierra, el lago: la imagen de la Reunión. Así el hombre superior renueva sus armas para hacer frente a lo imprevisto.",
        "judgement": "La Reunión. Éxito. El rey se acerca a su templo. Es propicio ver al gran hombre. Esto trae éxito. La perseverancia es propicia. Ofrecer grandes sacrificios crea buena fortuna. Es propicio emprender algo."
    },
    {
        "num": 46, "binary": (0, 1, 1, 0, 0, 0), "name_ch": "Sheng", "name_es": "El Ascenso",
        "image": "Dentro de la tierra crece la madera: la imagen del Ascenso. Así el hombre superior, con devoción, acumula lo pequeño para alcanzar lo alto y lo grande.",
        "judgement": "El Ascenso. Éxito supremo. Hay que ver al gran hombre. No temas. La partida hacia el sur trae buena fortuna."
    },
    {
        "num": 47, "binary": (0, 1, 0, 1, 1, 0), "name_ch": "Kun", "name_es": "El Agotamiento",
        "image": "No hay agua en el lago: la imagen del Agotamiento. Así el hombre superior arriesga su vida para seguir su voluntad.",
        "judgement": "El Agotamiento. Éxito. La perseverancia. El gran hombre tiene buena fortuna. Sin culpa. Tener algo que decir no es creído."
    },
    {
        "num": 48, "binary": (0, 1, 1, 0, 1, 0), "name_ch": "Jing", "name_es": "El Pozo",
        "image": "Madera sobre el agua: la imagen del Pozo. Así el hombre superior anima al pueblo en el trabajo y se exhortan mutuamente a ayudarse.",
        "judgement": "El Pozo. La ciudad puede ser cambiada, pero el pozo no puede ser cambiado. No disminuye ni aumenta. Vienen y van y sacan del pozo. Si uno llega casi al agua y la cuerda no llega, o si la jarra se rompe, trae desdicha."
    },
    {
        "num": 49, "binary": (1, 0, 1, 1, 1, 0), "name_ch": "Ge", "name_es": "La Revolución",
        "image": "Fuego en el lago: la imagen de la Revolución. Así el hombre superior pone en orden el calendario y aclara las estaciones.",
        "judgement": "La Revolución. En el día en que se completa, se cree. Éxito supremo, propiciando mediante la perseverancia. El remordimiento desaparece."
    },
    {
        "num": 50, "binary": (0, 1, 1, 1, 0, 1), "name_ch": "Ding", "name_es": "El Caldero",
        "image": "Fuego sobre la madera: la imagen del Caldero. Así el hombre superior consolida su destino rectificando su posición.",
        "judgement": "El Caldero. Suprema buena fortuna. Éxito."
    },
    {
        "num": 51, "binary": (1, 0, 0, 1, 0, 0), "name_ch": "Zhen", "name_es": "Lo Suscitativo",
        "image": "Trueno sobre trueno: la imagen de lo Suscitativo. Así el hombre superior, con temor y aprensión, pone su vida en orden y se examina a sí mismo.",
        "judgement": "Lo Suscitativo. Éxito. El trueno viene: ¡ja, ja! Palabras risueñas: ¡ah, ah! El trueno asusta a cien millas, y él no deja caer la cuchara sacrificial y el cáliz."
    },
    {
        "num": 52, "binary": (0, 0, 1, 0, 0, 1), "name_ch": "Gen", "name_es": "La Quietud",
        "image": "Montañas una junto a otra: la imagen de la Quietud. Así el hombre superior no permite que sus pensamientos vayan más allá de su situación.",
        "judgement": "La Quietud. Manteniendo su espalda quieta, para que ya no sienta su cuerpo. Entra en su patio y no ve a su gente. Sin culpa."
    },
    {
        "num": 53, "binary": (0, 0, 1, 0, 1, 1), "name_ch": "Jian", "name_es": "El Desarrollo",
        "image": "En la montaña, un árbol: la imagen del Desarrollo. Así el hombre superior mora en la virtud digna para mejorar las costumbres.",
        "judgement": "El Desarrollo. La doncella es dada en matrimonio. Buena fortuna. La perseverancia es propicia."
    },
    {
        "num": 54, "binary": (0, 1, 1, 1, 0, 0), "name_ch": "Gui Mei", "name_es": "La Muchacha que se Casa",
        "image": "Trueno sobre el lago: la imagen de la Muchacha que se Casa. Así el hombre superior, por la eternidad del fin, conoce lo transitorio.",
        "judgement": "La Muchacha que se Casa. Las empresas traen desdicha. Nada que sea propicio."
    },
    {
        "num": 55, "binary": (1, 0, 1, 1, 0, 0), "name_ch": "Feng", "name_es": "La Abundancia",
        "image": "Tanto el trueno como el relámpago llegan: la imagen de la Abundancia. Así el hombre superior decide los pleitos y ejecuta los castigos.",
        "judgement": "La Abundancia tiene éxito. El rey la alcanza. No estés triste. Sé como el sol a mediodía."
    },
    {
        "num": 56, "binary": (1, 0, 0, 1, 0, 1), "name_ch": "Lü", "name_es": "El Andariego",
        "image": "Fuego en la montaña: la imagen del Andariego. Así el hombre superior es claro y cauteloso al aplicar los castigos y no retrasa los litigios.",
        "judgement": "El Andariego. Éxito a través de lo pequeño. La perseverancia trae buena fortuna al andariego."
    },
    {
        "num": 57, "binary": (0, 1, 1, 0, 1, 1), "name_ch": "Xun", "name_es": "Lo Suave",
        "image": "Vientos que se siguen uno a otro: la imagen de lo Suave. Así el hombre superior difunde sus mandatos y lleva a cabo sus empresas.",
        "judgement": "Lo Suave. Éxito a través de lo pequeño. Es propicio tener un lugar a donde ir. Es propicio ver al gran hombre."
    },
    {
        "num": 58, "binary": (0, 1, 0, 1, 1, 0), "name_ch": "Dui", "name_es": "Lo Gozoso",
        "image": "Lagos que descansan uno sobre otro: la imagen de lo Gozoso. Así el hombre superior se une a sus amigos para la discusión y la práctica.",
        "judgement": "Lo Gozoso. Éxito. La perseverancia es propicia."
    },
    {
        "num": 59, "binary": (0, 1, 0, 0, 1, 1), "name_ch": "Huan", "name_es": "La Disolución",
        "image": "El viento sopla sobre el agua: la imagen de la Disolución. Así los antiguos reyes sacrificaban al Señor y construían templos.",
        "judgement": "La Disolución. Éxito. El rey se acerca a su templo. Es propicio cruzar las grandes aguas. La perseverancia es propicia."
    },
    {
        "num": 60, "binary": (1, 1, 0, 0, 1, 0), "name_ch": "Jie", "name_es": "La Limitación",
        "image": "Agua sobre el lago: la imagen de la Limitación. Así el hombre superior crea número y medida, y examina la naturaleza de la virtud y la conducta correcta.",
        "judgement": "La Limitación. Éxito. La limitación amarga no debe ser perseverada."
    },
    {
        "num": 61, "binary": (1, 1, 0, 0, 1, 1), "name_ch": "Zhong Fu", "name_es": "La Verdad Interior",
        "image": "Viento sobre el lago: la imagen de la Verdad Interior. Así el hombre superior discute los casos penales para retrasar las ejecuciones.",
        "judgement": "La Verdad Interior. Cerdos y peces. Buena fortuna. Es propicio cruzar las grandes aguas. La perseverancia es propicia."
    },
    {
        "num": 62, "binary": (0, 0, 1, 1, 0, 0), "name_ch": "Xiao Guo", "name_es": "La Preponderancia de lo Pequeño",
        "image": "Trueno en la montaña: la imagen de la Preponderancia de lo Pequeño. Así el hombre superior en su conducta da preponderancia a la reverencia. En el duelo, da preponderancia al dolor. En el gasto, da preponderancia a la parsimonia.",
        "judgement": "La Preponderancia de lo Pequeño. Éxito. La perseverancia es propicia. Se pueden hacer cosas pequeñas, no se deben hacer cosas grandes. El pájaro volador trae el mensaje: no es bueno esforzarse hacia arriba, es bueno permanecer abajo. Gran buena fortuna."
    },
    {
        "num": 63, "binary": (1, 0, 1, 0, 1, 0), "name_ch": "Ji Ji", "name_es": "Después de la Consumación",
        "image": "Agua sobre el fuego: la imagen del estado Después de la Consumación. Así el hombre superior toma en consideración la desgracia y se arma contra ella de antemano.",
        "judgement": "Después de la Consumación. Éxito en lo pequeño. La perseverancia es propicia. Al principio, buena fortuna; al final, desorden."
    },
    {
        "num": 64, "binary": (0, 1, 0, 1, 0, 1), "name_ch": "Wei Ji", "name_es": "Antes de la Consumación",
        "image": "Fuego sobre el agua: la imagen del estado Antes de la Consumación. Así el hombre superior es cuidadoso en la discriminación de las cosas, para que cada una encuentre su lugar adecuado.",
        "judgement": "Antes de la Consumación. Éxito. Pero si el pequeño zorro, casi al completar el cruce, mete su cola en el agua, no hay nada que sea propicio."
    }
]
