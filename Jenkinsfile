node {
    def app

    stage('Clone repository') {
        checkout scm
    }

    stage('gitlab') {
        steps {
            echo 'Notify GitLab'
            updateGitlabCommitStatus name: 'build', state: 'pending'
            updateGitlabCommitStatus name: 'build', state: 'success'
        }
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

    stage('Clear old version') {
        echo "Running source code in a fully containerized environment..."    
        sh 'docker-compose -f docker-compose-prod.yml down -v'
    }

    stage('Deploy Source Code') {
        echo "Running source code in a fully containerized environment..."    
        sh 'docker-compose -f docker-compose-prod.yml up -d --build'
    }
}