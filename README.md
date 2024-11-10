# Ambien de desarrollo
## Variables de entorno
```.env
PORT=
DATABASE_URL=postgresql://postgres:admin@database-ma:5432/memoria_artistica
JWT_SECRET=
```

> PORT y JWT_SECRET son a elección del desarrollador


## Comando de ejecucion docker

1. Primero levantamos la base de datos
```yml
docker-compose -f docker-compose.dev.yml up database-ma
```

2. Luego levantamos todo los servicios
```yml
docker-compose -f docker-compose.dev.yml up
```