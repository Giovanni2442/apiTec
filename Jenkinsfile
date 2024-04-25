pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Clonar el repositorio
                git 'https://github.com/Giovanni2442/apiTec.git'
            }
        }

        stage('Setup') {
            steps {
                // Configurar el entorno, por ejemplo, instalar dependencias
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
               
                sh 'pytest tests/'
            }
        }

        stage('Build') {
            steps {
                // Construir imagen Docker, si aplica
                sh 'docker build -t apitec .'
            }
        }

        stage('Deploy') {
            steps {
                // Desplegar en un entorno, por ejemplo, Docker o un servidor
                sh 'docker run -d -p 3090:3000 apitec'
            }
        }
    }

    post {
        failure {
            // Manejar fallos
            echo 'El pipeline falló'
        }
        success {
            // Acciones en caso de éxito
            echo 'El pipeline se completó con éxito'
        }
    }
}
