node {
    def app

    stage('Clone repository') {
        checkout scm
    }

    stage('Build image') {
        app = docker.build("djangobasic:${env.BUILD_ID}")
    }

    stage('Run Test Flake8') {
        app.inside {
            sh 'flake8 --select E123,W503 books_cbv/'
            sh 'flake8 --select E123,W503 books_fbv/'
        }
    }

    stage('Run Test Django') {
        app.inside {
            sh 'python manage.py test'
        }
    }

}