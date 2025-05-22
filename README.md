# API Color Game – Backend para el Juego de Colorear Tangram

## Índice

1. [Descripción](#descripción)  
2. [Características principales](#características-principales)  
3. [Tecnologías y herramientas](#tecnologías-y-herramientas)  
4. [Instalación y arranque](#instalación-y-arranque)  
5. [Endpoints principales](#endpoints-principales)  
6. [Calidad de Software](#calidad-de-software)  
   - [Control de versiones y ramas](#control-de-versiones-y-ramas)  
   - [Estándares de commits](#estándares-de-commits)  
   - [Análisis estático con SonarQube](#análisis-estático-con-sonarqube)  
 7. [Estructura del proyecto](#estructura-del-proyecto) 



## Descripción

Este repositorio contiene el **backend** de la aplicación Color Game, una API REST desarrollada en Python con FastAPI que gestiona:

- Autenticación y autorización de doctores y pacientes  
- Creación y gestión de perfiles de usuario  
- Registro y consulta de sesiones de juego (aciertos, errores, tiempos)  
- Persistencia en base de datos PostgreSQL  
- Control de sesión mediante middlewares

> **Repositorio Backend**: https://github.com/JeffersonDaviid/api-color-game  



## Características principales

- **Autenticación**: JWT para doctores y pacientes  
- **Gestión de perfiles**: CRUD de usuarios (doctor/paciente)  
- **Sesiones de juego**: Registro de aciertos, errores y tiempo  
- **Historial**: Consultas por paciente y rangos de fecha  
- **Middlewares**: Verificación de sesión y validación de roles  
- **Docke­rización**: Contenedores Docker para API y base de datos  



## Tecnologías y herramientas

- **Lenguaje y framework**  
  - Python 3.10+  
  - FastAPI (async, documentación automática via OpenAPI)  
- **Base de datos**  
  - PostgreSQL  
  - Peewee  
- **Contenerización**  
  - Docker & Docker Compose  
- **Calidad de código**  
  - SonarQube (análisis estático)  
- **Control de versiones**  
  - Git con GitFlow (`main`, `develop`, `feature/*`, `bugfix/*`, `release/*`)  


## Instalación y arranque

### Variables de entorno
```.env
PORT=
DATABASE_URL=postgresql://postgres:admin@database-ma:5432/memoria_artistica
JWT_SECRET=
```

> PORT y JWT_SECRET son a elección del desarrollador


### Comando de ejecucion docker

1. Primero levantamos la base de datos
```yml
docker-compose -f docker-compose.dev.yml up database-ma
```

2. Luego levantamos todo los servicios
```yml
docker-compose -f docker-compose.dev.yml up
```



## Endpoints principales

| Ruta                      | Método | Descripción                                           |
| ------------------------- | ------ | ----------------------------------------------------- |
| `POST /auth/login`        | POST   | Login de doctor/paciente → devuelve JWT               |
| `POST /users/doctor`      | POST   | Crear perfil de doctor                                |
| `POST /users/patient`     | POST   | Crear perfil de paciente                              |
| `GET /sessions/{id}`      | GET    | Obtener datos de una sesión por su ID                 |
| `POST /sessions/`         | POST   | Registrar nueva sesión de juego (aciertos, errores…)  |
| `GET /sessions/user/{id}` | GET    | Listar sesiones de un paciente, opcional rango fechas |

> Para la documentación completa de endpoints y modelos, revisa `/docs` en ejecución o el archivo `openapi.json`.

---

## Calidad de Software

### Control de versiones y ramas

Se sigue **GitFlow**:

* `main`: código en producción
* `develop`: integración de nuevas funcionalidades
* `feature/<descripción>`: desarrollo de features
* `bugfix/<descripción>`: corrección de errores
* `release/<versión>`: preparación de nueva versión

### Estándares de commits

Commit messages siguiendo **Conventional Commits**:

```
feat(auth): añadir endpoint de refresco de token
fix(session): corregir cálculo de tiempo en sesiones
docs: actualizar documentación de usuario
```

### Análisis estático con SonarQube

* Métricas de cobertura, bugs y code smells
 
---

## Estructura del proyecto

```
api-color-game/
├── alembic/                  # Migraciones de base de datos
├── app/
│   ├── api/                  # Routers y controladores
│   ├── core/                 # Configuración (settings, JWT)
│   ├── db/                   # Modelos SQLAlchemy, session maker
│   ├── schemas/              # Pydantic models
│   ├── services/             # Lógica de negocio
│   ├── middlewares/          # Verificación de sesión y roles
│   └── main.py               # Punto de entrada FastAPI
├── tests/                    # Tests unitarios e integración
├── .env.example              # Ejemplo de variables de entorno
├── docker-compose.yml        # Definición de servicios Docker
├── Dockerfile                # Imagen de la API
├── requirements.txt          # Dependencias de Python
├── alembic.ini               # Configuración de Alembic
└── sonar-project.properties  # Configuración SonarQube
```

 
 