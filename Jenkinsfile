pipeline {
  agent {
    docker {
      image 'debian:jessie'
    }

  }
  stages {
    stage('Print Something') {
      steps {
        echo 'hello'
      }
    }
    stage('Deploy') {
      steps {
        sleep 5
      }
    }
  }
}