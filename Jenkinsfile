node {
    def app

    stage('Run test') {
        sh 'echo "success"'
    }
    
    stage('Clone repository') {
        /* Let's make sure we have the repository cloned to our workspace */

        checkout scm
    }

}