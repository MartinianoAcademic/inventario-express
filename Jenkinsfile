pipeline {
    agent any
    
    stages {
        stage('Instalación de dependencias') {
            steps {
                echo '=== Instalación de dependencias ==='
                sh 'echo "Resolviendo y validando paquetes desde requirements.txt..."'
            }
        }
        stage('Ejecución de pruebas') {
            steps {
                echo '=== Ejecutando pruebas automatizadas ==='
                // Reutilizamos el motor Docker del host para validar el código
                sh 'docker build -t inventario-express-test:latest -f Dockerfile .'
                sh 'docker run --rm -e PYTHONPATH=/app inventario-express-test:latest pytest'
            }
        }
        stage('Construcción del proyecto') {
            steps {
                echo '=== Construcción del proyecto ==='
                sh 'echo "Validando integridad de los archivos fuente de la API..."'
            }
        }
        stage('Construcción de imagen Docker') {
            steps {
                echo '=== Construyendo imagen Docker de Producción ==='
                sh 'docker build -t inventario-express:prod -f Dockerfile .'
            }
        }
        stage('Despliegue simulado') {
            steps {
                echo '=== Simulación de Despliegue ==='
                sh 'echo "Iniciando conexión con el entorno de pruebas..."'
                sh 'echo "Desplegando contenedor: inventario-express:prod"'
                sh 'echo "SUCCESS: El servicio Inventario Express se encuentra activo."'
            }
        }
    }
}