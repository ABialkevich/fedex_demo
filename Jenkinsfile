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
    /* stage('Register project in Allure') {
      steps {
        sleep(5)
        sh 'docker exec -t app python3 allure_main.py reg_project fedex-demo'
      }
    } */
    stage('Run tests against the container') {
      steps {
        sh 'docker exec -t app pytest --alluredir=allure-results --localrun false tests/test_assitant_chat.py'
      }
    }
    stage('Copying Allure Results') {
      steps {
          dir("${env.WORKSPACE}@tmp"){
            sh 'docker cp app:/src/allure-results .'
          }
      }
    }
    stage('Generate Allure Report') {
      steps {
        allure includeProperties: false, jdk: '', results: [[path: 'tmp/allure-results']]
        // needed for docker as service
        // sh 'docker exec -t --user root app python3 allure_main.py gen_results fedex-demo'
      }
    }
  }
  post {
    always {
      sh 'docker compose down --remove-orphans -v'
      sh 'docker compose ps'
      dir("${env.WORKSPACE}@script@tmp") {
        sh 'rm -rf allure-results'
      }
    }
  }
}