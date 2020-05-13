node {
    def app

    stage('Clone repository') {
        updateGitlabCommitStatus(name: 'Start Clone repository', state: 'running')
        checkout scm
        updateGitlabCommitStatus(name: 'Start Clone repository', state: 'success')
    }

    stage('Start Build gitlab') {
        echo 'Notify GitLab'
    }

    stage('Build image') {
        updateGitlabCommitStatus(name: 'Build image', state: 'running')
        app = docker.build("djangobasic:${env.BUILD_ID}")
        updateGitlabCommitStatus(name: 'Build image', state: 'success')
    }

    stage('Run Test Flake8') {
        updateGitlabCommitStatus(name: 'Run Test Flake8', state: 'running')
        app.inside {
            sh 'flake8 --select E123,W503 books_cbv/'
            sh 'flake8 --select E123,W503 books_fbv/'
        }
        updateGitlabCommitStatus(name: 'Run Test Flake8', state: 'success')
    }

    stage('Run Test Django') {
        updateGitlabCommitStatus(name: 'Run Test Django', state: 'running')
        app.inside {
            sh 'python manage.py test'
        }
        updateGitlabCommitStatus(name: 'Run Test Django', state: 'success')
    }

    stage('End Build gitlab') {
        echo 'Notify GitLab'
    }

    stage('Clear old version') {
        updateGitlabCommitStatus(name: 'Deploy', state: 'running')

        echo "Running source code in a fully containerized environment..."    
        sh 'docker-compose -f docker-compose-prod.yml down -v'
    }

    stage('Deploy Source Code') {
        echo "Running source code in a fully containerized environment..."    
        sh 'docker-compose -f docker-compose-prod.yml up -d --build'

        updateGitlabCommitStatus(name: 'Deploy', state: 'success')
    }
}