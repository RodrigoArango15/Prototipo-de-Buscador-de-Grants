# data.py

# Datos simulados de grants
mock_grants = [
    {
        "id": 1,
        "title": "Erasmus+ Key Action 2: Cooperation among organisations and institutions",
        "source": "Erasmus+",
        "region": "Europa",
        "type": "Educación",
        "deadline": "2026-10-15",
        "description": "Apoyo a la cooperación internacional entre universidades e institutos de educación superior y formación profesional.",
        "url": "https://erasmus-plus.ec.europa.eu/es/sitemap",
        "saved": False
    },
    {
        "id": 2,
        "title": "NSF Computer and Network Systems (CNS)",
        "source": "NSF",
        "region": "Estados Unidos",
        "type": "Investigación",
        "deadline": "2026-09-30",
        "description": "Financiamiento para investigación innovadora en sistemas informáticos y redes de comunicación.",
        "url": "https://www.nsf.gov/funding",
        "saved": False
    },
    {
        "id": 3,
        "title": "Fondo de Innovación Tecnológica LAC",
        "source": "Ministerio de Ciencia y Tecnología",
        "region": "Latinoamérica",
        "type": "Innovación",
        "deadline": "2026-11-20",
        "description": "Semilla para desarrollo de nuevas tecnologías enfocadas en resolver problemáticas locales de la región.",
        "url": "#",
        "saved": False
    },
    {
        "id": 4,
        "title": "Global Development Network - Research Grant",
        "source": "GDN",
        "region": "Global",
        "type": "Desarrollo",
        "deadline": "2026-08-01",
        "description": "Fomentar el desarrollo a través de la investigación de alta calidad en ciencias sociales a nivel global.",
        "url": "#",
        "saved": False
    },
    {
        "id": 5,
        "title": "Erasmus+ Capacity Building in Higher Education",
        "source": "Erasmus+",
        "region": "Europa/Latinoamérica",
        "type": "Educación",
        "deadline": "2027-02-15",
        "description": "Proyectos de cooperación transnacional basados en asociaciones multilaterales para el fortalecimiento de capacidades.",
        "url": "https://erasmus-plus.ec.europa.eu/opportunities/organisations/cooperation-among-organisations-and-institutions/capacity-building-in-higher-education",
        "saved": False
    },
    {
        "id": 6,
        "title": "Erasmus+ Jean Monnet Activities",
        "source": "Erasmus+",
        "region": "Global",
        "type": "Educación",
        "deadline": "2026-10-31",
        "description": "Acciones para promover la excelencia en la enseñanza y la investigación en el ámbito de los estudios sobre la Unión Europea en todo el mundo.",
        "url": "https://erasmus-plus.ec.europa.eu/opportunities/opportunities-for-organisations/jean-monnet-actions",
        "saved": False
    },
    {
        "id": 7,
        "title": "Erasmus+ Mobility of Higher Education Students and Staff",
        "source": "Erasmus+",
        "region": "Europa/Latinoamérica",
        "type": "Educación",
        "deadline": "2026-06-15",
        "description": "Fomento a la movilidad internacional entre los países del programa y países asociados para estudiantes y personal académico.",
        "url": "https://erasmus-plus.ec.europa.eu/opportunities/individuals/students/studying-abroad",
        "saved": False
    },
    {
        "id": 8,
        "title": "NSF Cyberinfrastructure for Sustained Scientific Innovation (CSSI)",
        "source": "NSF",
        "region": "Estados Unidos",
        "type": "Investigación",
        "deadline": "2026-09-01",
        "description": "Desarrollo y mantenimiento de infraestructura cibernética avanzada que permita realizar investigación científica a gran escala y simulaciones.",
        "url": "https://new.nsf.gov/funding/opportunities/cyberinfrastructure-sustained-scientific-innovation-cssi-0",
        "saved": False
    },
    {
        "id": 9,
        "title": "NSF Research Experiences for Undergraduates (REU)",
        "source": "NSF",
        "region": "Estados Unidos",
        "type": "Educación",
        "deadline": "2026-08-25",
        "description": "Financiamiento para involucrar activamente a los estudiantes de pregrado en docencia y la investigación práctica.",
        "url": "https://new.nsf.gov/funding/opportunities/research-experiences-undergraduates-reu",
        "saved": False
    },
    {
        "id": 10,
        "title": "NSF Engineering Research Centers (ERC)",
        "source": "NSF",
        "region": "Estados Unidos",
        "type": "Investigación",
        "deadline": "2026-10-10",
        "description": "Apoyo a centros interdisciplinarios enfocados en resolver problemas complejos y avanzar en tecnologías clave bajo un enfoque de ingeniería en sistemas.",
        "url": "https://new.nsf.gov/funding/opportunities",
        "saved": False
    },
    {
        "id": 11,
        "title": "Fondo FONDECYT Regular",
        "source": "ANID (Chile)",
        "region": "Latinoamérica",
        "type": "Investigación",
        "deadline": "2026-07-20",
        "description": "Promover la investigación de base científico-tecnológica de primer nivel a investigadores individuales y grupos de alta competencia.",
        "url": "https://www.anid.cl/concursos/",
        "saved": False
    },
    {
        "id": 12,
        "title": "FAPESP Research Grant - Thematic Project",
        "source": "FAPESP (Brasil)",
        "region": "Latinoamérica",
        "type": "Investigación",
        "deadline": "2026-12-01",
        "description": "Apoyo a proyectos de investigación con objetivos amplios, audaces y ejecutados por un gran equipo de investigadores.",
        "url": "https://fapesp.br/en/thematic",
        "saved": False
    },
    {
        "id": 13,
        "title": "Convocatoria I+D+i Ecosistemas de CTI",
        "source": "MINCIENCIAS (Colombia)",
        "region": "Latinoamérica",
        "type": "Innovación",
        "deadline": "2026-06-30",
        "description": "Financiamiento para proyectos conjuntos entre empresas, universidades y el estado para escalar la innovación colombiana y cierre de brechas tecnológicas.",
        "url": "https://minciencias.gov.co/convocatorias",
        "saved": False
    },
    {
        "id": 14,
        "title": "Estancias Posdoctorales y Sabáticas",
        "source": "CONAHCYT (México)",
        "region": "Latinoamérica",
        "type": "Desarrollo",
        "deadline": "2026-07-05",
        "description": "Consolidación de capacidades humanísticas, científicas, y de desarrollo posibilitando proyectos conjuntos para resolver problemas nacionales.",
        "url": "https://conahcyt.mx/convocatorias/",
        "saved": False
    },
    {
        "id": 15,
        "title": "Laboratorio de Innovación del Grupo BID (BID Lab)",
        "source": "BID",
        "region": "Latinoamérica",
        "type": "Innovación",
        "deadline": "2026-11-15",
        "description": "Iniciativas experimentales y disruptivas de gran impacto, que apoyen a emprendimientos en la inserción de nuevas tecnologías.",
        "url": "https://bidlab.org/es",
        "saved": False
    }
]

def get_all_grants():
    """Retorna todos los grants simulados."""
    return mock_grants

def get_grant_by_id(grant_id):
    """Retorna un grant específico por su ID."""
    for grant in mock_grants:
        if grant["id"] == grant_id:
            return grant
    return None

def toggle_save_grant(grant_id):
    """Alterna el estado de 'guardado' de un grant (en memoria)."""
    grant = get_grant_by_id(grant_id)
    if grant:
        grant["saved"] = not grant["saved"]
        return grant
    return None
