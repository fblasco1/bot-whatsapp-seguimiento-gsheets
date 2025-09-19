#!/usr/bin/env python3
"""
Módulo de códigos de área e indicativos interurbanos de Argentina
Basado en el archivo "Indicativos Interurbanos (300 A.L.).xls"
"""

# Códigos de área de Argentina (indicativos interurbanos)
# Formato: código_area: (provincia, localidad_principal)
ARGENTINA_AREA_CODES = {
    # Buenos Aires - AMBA y Gran Buenos Aires
    "11": ("Buenos Aires", "Ciudad de Buenos Aires"),
    "220": ("Buenos Aires", "Merlo"),
    "221": ("Buenos Aires", "La Plata"),
    "222": ("Buenos Aires", "Magdalena"),
    "224": ("Buenos Aires", "Coronel Brandsen"),
    "225": ("Buenos Aires", "Glew"),
    "226": ("Buenos Aires", "Alejandro Korn"),
    "227": ("Buenos Aires", "Cañuelas"),
    "228": ("Buenos Aires", "Lobos"),
    "229": ("Buenos Aires", "Juan María Gutiérrez"),
    "223": ("Buenos Aires", "Mar del Plata"),
    "2241": ("Buenos Aires", "Chascomús"),
    "2242": ("Buenos Aires", "Lezama"),
    "2243": ("Buenos Aires", "General Belgrano"),
    "2244": ("Buenos Aires", "Las Flores"),
    "2245": ("Buenos Aires", "Dolores"),
    "2246": ("Buenos Aires", "Santa Teresita"),
    "2247": ("Buenos Aires", "San Clemente del Tuyú"),
    "2254": ("Buenos Aires", "Pinamar"),
    "2255": ("Buenos Aires", "Villa Gesell"),
    "2257": ("Buenos Aires", "Mar de Ajó"),
    "2261": ("Buenos Aires", "Lobería"),
    "2262": ("Buenos Aires", "Necochea"),
    "2263": ("Buenos Aires", "La Dulce"),
    "2264": ("Buenos Aires", "Coronel Vidal"),
    "2265": ("Buenos Aires", "Balcarce"),
    "2266": ("Buenos Aires", "General Madariaga"),
    "2267": ("Buenos Aires", "Maipú"),
    "2268": ("Buenos Aires", "Monte"),
    "2269": ("Buenos Aires", "Navarro"),
    "2271": ("Buenos Aires", "Carmen de Areco"),
    "2272": ("Buenos Aires", "Carlos Spegazzini"),
    "2281": ("Buenos Aires", "Azul"),
    "2282": ("Buenos Aires", "Tapalqué"),
    "2284": ("Buenos Aires", "Olavarría"),
    "2285": ("Buenos Aires", "Laprida"),
    "2286": ("Buenos Aires", "General Lamadrid"),
    "2291": ("Buenos Aires", "Miramar"),
    "2292": ("Buenos Aires", "Benito Juárez"),
    "2293": ("Buenos Aires", "Ayacucho"),
    "2294": ("Buenos Aires", "Rauch"),
    "230": ("Buenos Aires", "Pilar"),
    "231": ("Buenos Aires", "General Pico"),
    "232": ("Buenos Aires", "Bolívar"),
    "233": ("Buenos Aires", "Daireaux"),
    "234": ("Buenos Aires", "9 de Julio"),
    "235": ("Buenos Aires", "José C. Paz"),
    "236": ("Buenos Aires", "Luján"),
    "237": ("Buenos Aires", "Mercedes"),
    "238": ("Buenos Aires", "San Andrés de Giles"),
    "239": ("Buenos Aires", "San Antonio de Areco"),
    "2317": ("Buenos Aires", "Realicó"),
    "2318": ("Buenos Aires", "Quemú Quemú"),
    "2319": ("Buenos Aires", "Eduardo Castex"),
    "2320": ("Buenos Aires", "Caleufú"),
    "2321": ("Buenos Aires", "Huinco Renanco"),
    "2322": ("Buenos Aires", "América"),
    "2323": ("Buenos Aires", "Victorica"),
    "2342": ("Buenos Aires", "Bragado"),
    "2343": ("Buenos Aires", "Norberto de la Riestra"),
    "2344": ("Buenos Aires", "Saladillo"),
    "2345": ("Buenos Aires", "25 de Mayo"),
    "2346": ("Buenos Aires", "Chivilcoy"),
    "2347": ("Buenos Aires", "Chacabuco"),
    "2353": ("Buenos Aires", "General Arenales"),
    "2354": ("Buenos Aires", "Vedia"),
    "2355": ("Buenos Aires", "Lincoln"),
    "2356": ("Buenos Aires", "General Pinto"),
    "2357": ("Buenos Aires", "Carlos Tejedor"),
    "2358": ("Buenos Aires", "Los Toldos"),
    "2362": ("Buenos Aires", "Junín"),
    "2363": ("Buenos Aires", "Moreno"),
    "2364": ("Buenos Aires", "Trenque Lauquen"),
    "2365": ("Buenos Aires", "Salazar"),
    "2366": ("Buenos Aires", "Tres Lomas"),
    "2367": ("Buenos Aires", "Carlos Casares"),
    "2368": ("Buenos Aires", "Pehuajó"),
    "2369": ("Buenos Aires", "Colón"),
    "2371": ("Buenos Aires", "Salto"),
    "2372": ("Buenos Aires", "Rojas"),
    "2373": ("Buenos Aires", "Pergamino"),
    "2374": ("Buenos Aires", "Arrecifes"),
    "249": ("Buenos Aires", "Tandil"),
    
    # Mendoza
    "260": ("Mendoza", "San Rafael"),
    "261": ("Mendoza", "Mendoza"),
    "262": ("Mendoza", "Tunuyán"),
    "2624": ("Mendoza", "Uspallata"),
    "2625": ("Mendoza", "General Alvear"),
    "2626": ("Mendoza", "La Paz"),
    "2627": ("Mendoza", "San Martín"),
    
    # San Juan
    "264": ("San Juan", "San Juan"),
    "2644": ("San Juan", "San Agustín del Valle Fértil"),
    "2645": ("San Juan", "Jáchal"),
    "2646": ("San Juan", "Calingasta"),
    "2647": ("San Juan", "San Francisco del Monte de Oro"),
    
    # San Luis
    "2651": ("San Luis", "San Luis"),
    "2652": ("San Luis", "La Toma"),
    "2653": ("San Luis", "Tilisarao"),
    "2654": ("San Luis", "Mercedes"),
    "2655": ("San Luis", "Buena Esperanza"),
    "2656": ("San Luis", "San Luis"),
    
    # Chubut
    "2965": ("Chubut", "Trelew"),
    "2964": ("Chubut", "Chubut"),
    
    # Tierra del Fuego
    "2964": ("Tierra del Fuego", "Ushuaia"),
    "2964": ("Tierra del Fuego", "Tierra del Fuego"),
    "2964": ("Tierra del Fuego", "Río Turbio"),
    
    # Santa Cruz
    "2962": ("Santa Cruz", "Santa Cruz"),
    "2963": ("Santa Cruz", "Río Mayo"),
    
    # Río Negro
    "2920": ("Río Negro", "Bahía Blanca"),
    "2920": ("Río Negro", "Viedma"),
    "2920": ("Río Negro", "Río Negro"),
    "2921": ("Río Negro", "Coronel Dorrego"),
    "2922": ("Río Negro", "Coronel Pringles"),
    "2923": ("Río Negro", "Pigüé"),
    "2924": ("Río Negro", "Darregueira"),
    "2925": ("Río Negro", "Villa Iris"),
    "2926": ("Río Negro", "Coronel Suárez"),
    "2927": ("Río Negro", "Médanos"),
    "2928": ("Río Negro", "Pedro Luro"),
    "2929": ("Río Negro", "Guaminí"),
    "2930": ("Río Negro", "Río Colorado"),
    "2931": ("Río Negro", "Punta Alta"),
    "2932": ("Río Negro", "Huanguelén Sur"),
    "2934": ("Río Negro", "San Antonio Oeste"),
    "2935": ("Río Negro", "Rivadavia"),
    "2936": ("Río Negro", "Carhué"),
    "2940": ("Río Negro", "San Carlos de Bariloche"),
    "2942": ("Río Negro", "Ingeniero Jacobacci"),
    "2944": ("Río Negro", "Zapala"),
    "2948": ("Río Negro", "Neuquén"),
    "2945": ("Río Negro", "Esquel"),
    "2946": ("Río Negro", "Choele Choel"),
    "2947": ("Río Negro", "Chos Malal"),
    "2952": ("Río Negro", "General Acha"),
    "2953": ("Río Negro", "Macachín"),
    "2954": ("Río Negro", "Santa Rosa"),
    "2962": ("Río Negro", "San Julián"),
    "2963": ("Río Negro", "Perito Moreno"),
    "2964": ("Río Negro", "Río Grande"),
    "2966": ("Río Negro", "Río Gallegos"),
    "297": ("Río Negro", "Comodoro Rivadavia"),
    "2944": ("Río Negro", "San Martín de los Andes"),
    "298": ("Río Negro", "General Roca"),
    "2982": ("Río Negro", "Orense"),
    "2983": ("Río Negro", "Tres Arroyos"),
    "2984": ("Río Negro", "López Camelo"),
    "2985": ("Río Negro", "San Pedro"),
    "3402": ("Río Negro", "San Nicolás"),
    "3406": ("Río Negro", "Rufino"),
    
    # Santa Fe
    "3400": ("Santa Fe", "San Nicolás"),
    "3401": ("Santa Fe", "Villa Constitución"),
    "3402": ("Santa Fe", "San Nicolás"),
    "3403": ("Santa Fe", "El Trébol"),
    "3404": ("Santa Fe", "Arroyo Seco"),
    "3405": ("Santa Fe", "San Carlos Centro"),
    "3406": ("Santa Fe", "San Javier"),
    "3407": ("Santa Fe", "San Jorge"),
    "3408": ("Santa Fe", "Ramallo"),
    "3409": ("Santa Fe", "San Cristóbal"),
    "341": ("Santa Fe", "Rosario"),
    "342": ("Santa Fe", "Santa Fe"),
    "343": ("Santa Fe", "Paraná"),
    "344": ("Santa Fe", "Entre Ríos"),
    "3442": ("Santa Fe", "Nogoyá"),
    "3443": ("Santa Fe", "Victoria"),
    "3444": ("Santa Fe", "La Paz"),
    "3445": ("Santa Fe", "Bovril"),
    "3446": ("Santa Fe", "Concepción del Uruguay"),
    "3447": ("Santa Fe", "Gualeguay"),
    "3448": ("Santa Fe", "Rosario del Tala"),
    "3449": ("Santa Fe", "Gualeguaychú"),
    "345": ("Santa Fe", "Colón"),
    "3460": ("Santa Fe", "Concordia"),
    "3461": ("Santa Fe", "Federal"),
    "3462": ("Santa Fe", "Villaguay"),
    "3463": ("Santa Fe", "Chajarí"),
    "3464": ("Santa Fe", "San José de Feliciano"),
    "3465": ("Santa Fe", "Santa Teresa"),
    "3466": ("Santa Fe", "Venado Tuerto"),
    "3467": ("Santa Fe", "Canals"),
    "3468": ("Santa Fe", "Casilda"),
    "3469": ("Santa Fe", "Firmat"),
    "3470": ("Santa Fe", "Barrancas"),
    "3471": ("Santa Fe", "Cruz Alta"),
    "3472": ("Santa Fe", "Corral de Bustos"),
    "3473": ("Santa Fe", "Acebal"),
    "3474": ("Santa Fe", "Cañada de Gómez"),
    "3475": ("Santa Fe", "Marcos Juárez"),
    "3476": ("Santa Fe", "San Lorenzo"),
    "3482": ("Santa Fe", "Escobar"),
    "3483": ("Santa Fe", "Reconquista"),
    "3484": ("Santa Fe", "Vera"),
    "3487": ("Santa Fe", "Zárate"),
    "3488": ("Santa Fe", "Campana"),
    "3489": ("Santa Fe", "Ceres"),
    "3491": ("Santa Fe", "Rafaela"),
    "3492": ("Santa Fe", "Sunchales"),
    "3493": ("Santa Fe", "Esperanza"),
    "3494": ("Santa Fe", "Llambi Campbell"),
    "3495": ("Santa Fe", "San Justo"),
    
    # Córdoba
    "351": ("Córdoba", "Córdoba"),
    "3521": ("Córdoba", "Deán Funes"),
    "3522": ("Córdoba", "Villa de María del Río Seco"),
    "3523": ("Córdoba", "Villa del Totoral"),
    "3524": ("Córdoba", "Jesús María"),
    "3525": ("Córdoba", "Villa María"),
    "353": ("Córdoba", "Oliva"),
    "3533": ("Córdoba", "Las Varillas"),
    "3534": ("Córdoba", "Bell Ville"),
    "3535": ("Córdoba", "Villa Carlos Paz"),
    "3536": ("Córdoba", "Salsacate"),
    "3537": ("Córdoba", "Argüello"),
    "3541": ("Córdoba", "Villa Dolores"),
    "3542": ("Córdoba", "Santa Rosa de Calamuchita"),
    "3543": ("Córdoba", "Alta Gracia"),
    "3544": ("Córdoba", "La Falda"),
    "3546": ("Córdoba", "Cruz del Eje"),
    "3547": ("Córdoba", "Morteros"),
    "3548": ("Córdoba", "Balnearia"),
    "3549": ("Córdoba", "San Francisco"),
    "3562": ("Córdoba", "Río Tercero"),
    "3563": ("Córdoba", "Río Segundo"),
    "3564": ("Córdoba", "Villa del Rosario"),
    "3571": ("Córdoba", "Río Primero"),
    "3572": ("Córdoba", "La Puerta"),
    "3573": ("Córdoba", "Arroyito"),
    "358": ("Córdoba", "Río Cuarto"),
    "3582": ("Córdoba", "Sampacho"),
    "3583": ("Córdoba", "Vicuña Mackenna"),
    "3584": ("Córdoba", "La Carlota"),
    "3585": ("Córdoba", "Adelia María"),
    
    # Chaco
    "362": ("Chaco", "Resistencia"),
    "364": ("Chaco", "Chaco"),
    "3711": ("Chaco", "Presidencia Roque Sáenz Peña"),
    "3715": ("Chaco", "Formosa"),
    "3716": ("Chaco", "Ingeniero Guillermo N. Juárez"),
    "3717": ("Chaco", "Las Lomitas"),
    "3718": ("Chaco", "Ibarreta"),
    "3719": ("Chaco", "Clorinda"),
    "3720": ("Chaco", "Charadai"),
    "3721": ("Chaco", "General José de San Martín"),
    "3722": ("Chaco", "Charata"),
    "3723": ("Chaco", "Presidencia de la Plaza"),
    "3724": ("Chaco", "Villa Ángela"),
    "3725": ("Chaco", "Bernardo de Irigoyen"),
    
    # Misiones
    "3740": ("Misiones", "Misiones"),
    "3741": ("Misiones", "Puerto Rico"),
    "3742": ("Misiones", "Eldorado"),
    "3743": ("Misiones", "Leandro N. Alem"),
    "3744": ("Misiones", "Oberá"),
    "3754": ("Misiones", "Santo Tomé"),
    "3755": ("Misiones", "Corrientes"),
    "3756": ("Misiones", "Puerto Iguazú"),
    "3757": ("Misiones", "Apostoles"),
    "3758": ("Misiones", "Posadas"),
    
    # Corrientes
    "3772": ("Corrientes", "Paso de los Libres"),
    "3773": ("Corrientes", "Mercedes"),
    "3774": ("Corrientes", "Curuzú Cuatiá"),
    "3775": ("Corrientes", "Monte Caseros"),
    "3777": ("Corrientes", "Goya"),
    "3778": ("Corrientes", "Caa Catí"),
    "3781": ("Corrientes", "Saladas"),
    "3782": ("Corrientes", "Ituzaingó"),
    
    # La Rioja
    "380": ("La Rioja", "La Rioja"),
    "381": ("La Rioja", "San Miguel de Tucumán"),
    "3821": ("La Rioja", "Tucumán"),
    "3822": ("La Rioja", "Chepes"),
    "3823": ("La Rioja", "Chilecito"),
    "3824": ("La Rioja", "Chamical"),
    "3825": ("La Rioja", "Aimogasta"),
    
    # Catamarca
    "3826": ("Catamarca", "Catamarca"),
    "3827": ("Catamarca", "Recreo"),
    "3828": ("Catamarca", "Andalgalá"),
    "3829": ("Catamarca", "Tinogasta"),
    "3831": ("Catamarca", "Santa María"),
    "3832": ("Catamarca", "Monte Quemado"),
    
    # Santiago del Estero
    "384": ("Santiago del Estero", "Santiago del Estero"),
    "3841": ("Santiago del Estero", "Quimilí"),
    "3842": ("Santiago del Estero", "Añatuya"),
    "3843": ("Santiago del Estero", "Loreto"),
    "3844": ("Santiago del Estero", "Tintina"),
    "3845": ("Santiago del Estero", "Frías"),
    "3846": ("Santiago del Estero", "Suncho Corral"),
    "3847": ("Santiago del Estero", "Ojo de Agua"),
    "3848": ("Santiago del Estero", "Bandera"),
    "3849": ("Santiago del Estero", "Termas de Río Hondo"),
    "3854": ("Santiago del Estero", "Nueva Esperanza"),
    "3855": ("Santiago del Estero", "Trancas"),
    "3856": ("Santiago del Estero", "Monteros"),
    "3857": ("Santiago del Estero", "Concepción"),
    "3862": ("Santiago del Estero", "Tafí del Valle"),
    "3868": ("Santiago del Estero", "Cafayate"),
    
    # Salta
    "387": ("Salta", "Salta"),
    "3876": ("Salta", "Ranchillos"),
    "3877": ("Salta", "Tartagal"),
    "3878": ("Salta", "Metán"),
    "3881": ("Salta", "Joaquín V. González"),
    "3882": ("Salta", "Orán"),
    "3883": ("Salta", "San Salvador de Jujuy"),
    "3884": ("Salta", "Jujuy"),
    "3885": ("Salta", "La Quiaca"),
    "3886": ("Salta", "Libertador General San Martín"),
    "3887": ("Salta", "Humahuaca"),
    "3888": ("Salta", "San Pedro"),
    "3889": ("Salta", "La Madrid"),
    "3891": ("Salta", "Amaicha del Valle"),
    "3892": ("Salta", "Burruyacú"),
}

def get_area_code_info(area_code):
    """
    Obtiene información sobre un código de área argentino
    
    Args:
        area_code (str): Código de área (ej: "11", "261", "351")
    
    Returns:
        tuple: (provincia, localidad_principal) o None si no existe
    """
    return ARGENTINA_AREA_CODES.get(area_code)

def is_valid_argentina_area_code(area_code):
    """
    Verifica si un código de área es válido para Argentina
    
    Args:
        area_code (str): Código de área a verificar
    
    Returns:
        bool: True si es válido, False en caso contrario
    """
    return area_code in ARGENTINA_AREA_CODES

def get_all_area_codes():
    """
    Obtiene todos los códigos de área de Argentina
    
    Returns:
        list: Lista de códigos de área
    """
    return list(ARGENTINA_AREA_CODES.keys())

def normalize_argentina_phone(phone_number):
    """
    Normaliza un número de teléfono argentino al formato E.164 estándar (+54XXXXXXXXXX)
    Basado en la documentación oficial de Sent.dm y especificaciones ENACOM.
    
    Reglas E.164 para Argentina:
    - Código de país: +54
    - Código de área: 2-4 dígitos
    - Número local: 6-8 dígitos
    - Total: Siempre 10 dígitos (excluyendo +54)
    - Móviles: +54 9 XX XXXXXXXXX (el 9 es obligatorio)
    - Fijos: +54 XX XXXXXXXXX (sin el 9)
    
    Args:
        phone_number (str): Número de teléfono en cualquier formato
    
    Returns:
        str: Número normalizado en formato E.164 o None si no es válido
    """
    import re
    
    # Limpiar el número (mantener solo dígitos y +)
    cleaned = re.sub(r'[^\d+]', '', str(phone_number))
    
    # Remover el + inicial si existe
    if cleaned.startswith('+'):
        cleaned = cleaned[1:]
    
    # Remover 0 inicial si existe (trunk code nacional)
    if cleaned.startswith('0'):
        cleaned = cleaned[1:]
    
    # Remover 15 inicial si existe (prefijo móvil obsoleto)
    if cleaned.startswith('15'):
        cleaned = cleaned[2:]
    
    # Si ya tiene el prefijo 54, procesar
    if cleaned.startswith('54'):
        without_country = cleaned[2:]
        
        # Validar que tenga 10 o 11 dígitos (regla E.164 con casos especiales)
        if len(without_country) not in [10, 11]:
            return None
        
        # Casos especiales para números especiales
        if without_country.startswith('800'):
            # Toll-free: +54 800 XXXXXXX
            return f"+54{without_country}"
        elif without_country.startswith('600'):
            # Premium: +54 600 XXXXXXX
            return f"+54{without_country}"
        
        # Números móviles: empiezan con 9
        if without_country.startswith('9'):
            # Formato móvil: 9 + código de área (2-4 dígitos) + número local (6-8 dígitos)
            # Total: 10 dígitos
            if len(without_country) == 10:
                return f"+54{without_country}"
            elif len(without_country) == 11:
                # Caso especial: números con 11 dígitos (9 + código de área + número local)
                # Ejemplo: 91153770592 -> +541153770592 (quitar el 9)
                return f"+54{without_country[1:]}"
        
        # Números fijos: no empiezan con 9
        # Verificar que el código de área sea válido
        for area_code in sorted(ARGENTINA_AREA_CODES.keys(), key=len, reverse=True):
            if without_country.startswith(area_code):
                remaining_digits = without_country[len(area_code):]
                
                # Validar longitud según código de área
                if len(area_code) == 2 and len(remaining_digits) == 8:
                    return f"+54{area_code}{remaining_digits}"
                elif len(area_code) == 3 and len(remaining_digits) == 7:
                    return f"+54{area_code}{remaining_digits}"
                elif len(area_code) == 4 and len(remaining_digits) == 6:
                    return f"+54{area_code}{remaining_digits}"
    
    # Si no tiene prefijo 54, intentar detectar código de área
    if len(cleaned) == 10:
        # Números fijos sin prefijo 54
        for area_code in sorted(ARGENTINA_AREA_CODES.keys(), key=len, reverse=True):
            if cleaned.startswith(area_code):
                remaining_digits = cleaned[len(area_code):]
                
                # Validar longitud según código de área
                if len(area_code) == 2 and len(remaining_digits) == 8:
                    return f"+54{area_code}{remaining_digits}"
                elif len(area_code) == 3 and len(remaining_digits) == 7:
                    return f"+54{area_code}{remaining_digits}"
                elif len(area_code) == 4 and len(remaining_digits) == 6:
                    return f"+54{area_code}{remaining_digits}"
    
    elif len(cleaned) == 11 and cleaned.startswith('9'):
        # Números móviles sin prefijo 54
        return f"+54{cleaned}"
    
    return None

def get_phone_variants_for_search(phone_number):
    """
    Genera variantes de un número de teléfono para búsqueda en base de datos
    
    Args:
        phone_number (str): Número de teléfono original
    
    Returns:
        list: Lista de variantes para búsqueda
    """
    import re
    
    variants = []
    cleaned = re.sub(r'[^\d+]', '', str(phone_number))
    
    # Remover + inicial
    if cleaned.startswith('+'):
        cleaned = cleaned[1:]
    
    # Variante 1: Número completo
    variants.append(cleaned)
    
    # Variante 2: Sin prefijo 54
    if cleaned.startswith('54'):
        variants.append(cleaned[2:])
    
    # Variante 3: Solo código de área + número local
    # Caso especial: números que empiezan con 549 (móviles de Buenos Aires)
    if cleaned.startswith('549') and len(cleaned) == 13:
        variants.append(cleaned[2:])  # Sin 54: 91153770592
        variants.append(cleaned[3:])  # Sin 549: 1153770592
        variants.append(cleaned[5:])  # Solo número local: 53770592
    else:
        for area_code in sorted(ARGENTINA_AREA_CODES.keys(), key=len, reverse=True):
            if cleaned.startswith(f"54{area_code}"):
                variants.append(cleaned[2:])  # Sin 54
                variants.append(cleaned[2+len(area_code):])  # Solo número local
                break
            elif cleaned.startswith(area_code):
                variants.append(cleaned[len(area_code):])  # Solo número local
                break
    
    # Variante 4: Sin 0 inicial si existe
    if cleaned.startswith('0'):
        variants.append(cleaned[1:])
    
    # Variante 5: Sin 15 inicial si existe (para móviles)
    if cleaned.startswith('15'):
        variants.append(cleaned[2:])
    
    # Caso especial: números que empiezan con 9 (móviles)
    if cleaned.startswith('9') and len(cleaned) == 11:
        # Agregar variante sin el 9 inicial (asumiendo código 11)
        variants.append(cleaned[1:])
    
    # Remover duplicados y vacíos
    variants = list(set([v for v in variants if v and len(v) >= 6]))
    
    return variants

def validate_argentina_phone_e164(phone_number):
    """
    Valida un número de teléfono argentino según estándares E.164 y ENACOM
    Basado en la documentación oficial de Sent.dm
    
    Args:
        phone_number (str): Número de teléfono a validar
    
    Returns:
        dict: Resultado de validación con detalles
    """
    import re
    
    result = {
        'is_valid': False,
        'type': None,
        'normalized': None,
        'error': None
    }
    
    # Limpiar el número
    cleaned = re.sub(r'[^\d+]', '', str(phone_number))
    
    # Verificar formato básico
    if not cleaned.startswith('+54') and not cleaned.startswith('54'):
        result['error'] = 'No es un número argentino (falta código de país +54)'
        return result
    
    # Normalizar
    normalized = normalize_argentina_phone(phone_number)
    if not normalized:
        result['error'] = 'No se pudo normalizar el número'
        return result
    
    result['normalized'] = normalized
    
    # Extraer componentes
    without_country = normalized[3:]  # Quitar +54
    
    # Determinar tipo de número
    if without_country.startswith('800'):
        result['type'] = 'toll_free'
        result['is_valid'] = len(without_country) == 10
    elif without_country.startswith('600'):
        result['type'] = 'premium'
        result['is_valid'] = len(without_country) == 10
    elif without_country.startswith('9'):
        result['type'] = 'mobile'
        result['is_valid'] = len(without_country) == 10
    else:
        # Verificar si es un número móvil que fue normalizado (quitando el 9)
        # Si el número original tenía 11 dígitos y empezaba con 9, es móvil
        original_cleaned = re.sub(r'[^\d+]', '', str(phone_number))
        if original_cleaned.startswith('+'):
            original_cleaned = original_cleaned[1:]
        if original_cleaned.startswith('54'):
            original_without_country = original_cleaned[2:]
            if len(original_without_country) == 11 and original_without_country.startswith('9'):
                result['type'] = 'mobile'
            else:
                result['type'] = 'landline'
        else:
            result['type'] = 'landline'
        result['is_valid'] = len(without_country) == 10
    
    if not result['is_valid']:
        result['error'] = f'Longitud incorrecta para tipo {result["type"]}'
    
    return result

def format_argentina_phone_display(phone_number, format_type='local'):
    """
    Formatea un número argentino para visualización local
    Basado en la documentación oficial de Sent.dm
    
    Args:
        phone_number (str): Número en formato E.164
        format_type (str): 'local', 'international', 'mobile'
    
    Returns:
        str: Número formateado para visualización
    """
    if not phone_number or not phone_number.startswith('+54'):
        return phone_number
    
    without_country = phone_number[3:]  # Quitar +54
    
    if format_type == 'local':
        if without_country.startswith('9'):
            # Móvil: 9 XX XXXX-XXXX
            if len(without_country) == 10:
                return f"9 {without_country[1:3]} {without_country[3:7]}-{without_country[7:]}"
        elif without_country.startswith('800'):
            # Toll-free: 800 XXX-XXXX
            return f"800 {without_country[3:6]}-{without_country[6:]}"
        elif without_country.startswith('600'):
            # Premium: 600 XXX-XXXX
            return f"600 {without_country[3:6]}-{without_country[6:]}"
        else:
            # Fijo: XX XXXX-XXXX
            if len(without_country) == 10:
                return f"{without_country[:2]} {without_country[2:6]}-{without_country[6:]}"
    
    elif format_type == 'international':
        # +54 9 XX XXXX-XXXX o +54 XX XXXX-XXXX
        if without_country.startswith('9'):
            return f"+54 9 {without_country[1:3]} {without_country[3:7]}-{without_country[7:]}"
        else:
            return f"+54 {without_country[:2]} {without_country[2:6]}-{without_country[6:]}"
    
    return phone_number

def get_phone_type_info(phone_number):
    """
    Obtiene información detallada sobre el tipo de número argentino
    Basado en la documentación oficial de Sent.dm
    
    Args:
        phone_number (str): Número de teléfono
    
    Returns:
        dict: Información del tipo de número
    """
    validation = validate_argentina_phone_e164(phone_number)
    
    if not validation['is_valid']:
        return {'error': validation['error']}
    
    without_country = validation['normalized'][3:]  # Quitar +54
    
    info = {
        'type': validation['type'],
        'normalized': validation['normalized'],
        'area_code': None,
        'local_number': None,
        'is_mobile': False,
        'is_toll_free': False,
        'is_premium': False,
        'is_landline': False
    }
    
    if validation['type'] == 'mobile':
        info['is_mobile'] = True
        # Para números móviles normalizados, el código de área está en las primeras posiciones
        # Determinar código de área (2-4 dígitos)
        for area_code in sorted(ARGENTINA_AREA_CODES.keys(), key=len, reverse=True):
            if without_country.startswith(area_code):
                info['area_code'] = area_code
                info['local_number'] = without_country[len(area_code):]
                break
    elif validation['type'] == 'toll_free':
        info['is_toll_free'] = True
        info['area_code'] = '800'
        info['local_number'] = without_country[3:]
    elif validation['type'] == 'premium':
        info['is_premium'] = True
        info['area_code'] = '600'
        info['local_number'] = without_country[3:]
    else:  # landline
        info['is_landline'] = True
        # Determinar código de área (2-4 dígitos)
        for area_code in sorted(ARGENTINA_AREA_CODES.keys(), key=len, reverse=True):
            if without_country.startswith(area_code):
                info['area_code'] = area_code
                info['local_number'] = without_country[len(area_code):]
                break
    
    # Agregar información de ubicación si es posible
    if info['area_code'] and info['area_code'] in ARGENTINA_AREA_CODES:
        location_info = ARGENTINA_AREA_CODES[info['area_code']]
        info['province'] = location_info[0]
        info['city'] = location_info[1]
    
    return info
