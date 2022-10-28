pipeline {
  agent any
  stages {
    stage("verify tooling") {
      steps {
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
        sh 'docker compose up -d --no-color --wait'
        sh 'docker compose ps'
      }
    }
    stage('Register project in Allure') {
      steps {
        sleep(5)
        sh 'docker exec -t app python3 allure_main.py reg_project fedex-demo'
      }
    }
    stage('Run tests against the container') {
      steps {
        sh 'docker exec -t app pytest --localrun false --workers 2 tests/test_assitant_chat.py'
      }
    }
    stage('Publish Allure Report') {
      steps {
        steps {
            allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
        }
//         sh 'docker exec -t app python3 allure_main.py gen_results fedex-demo'
      }
    }
  }
  post {
    always {
      sh 'docker compose down --remove-orphans -v'
      sh 'docker compose ps'
    }
  }
}