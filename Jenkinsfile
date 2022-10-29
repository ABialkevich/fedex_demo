pipeline {
  agent any
  stages {
    stage("verify tooling") {
      steps {
        git branch: 'main', url: 'https://github.com/ABialkevich/fedex_demo.git/'
        sh '''
          docker version
          docker compose version
          curl --version
        '''
      }
    }
    stage('Prune Docker data') {
      steps {
        sh 'docker system prune -a --volumes -f'
      }
    }
    stage('Start services') {
      steps {
        sh 'docker compose -f docker-compose.yml up -d --no-color --wait'
        sh 'docker compose ps'
      }
    }
    stage('Run tests against the container') {
      steps {
        sh 'docker exec -t app pytest --alluredir=allure-results --localrun false tests/test_assitant_chat.py'
      }
    }
    stage('Copying Allure Results') {
      steps {
        sh 'docker cp app:/src/allure-results .'
      }
    }
    stage('Generate Allure Report') {
      steps {
        allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
      }
    }
  }
  post {
    always {
      sh 'docker compose down --remove-orphans -v'
      sh 'docker compose ps'
      cleanWs()
    }
  }
}