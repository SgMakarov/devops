pipeline {
  agent any
  stages {
    stage('Test') {
      steps {
        echo 'Testing..'
        sh '''
          echo "Building test image..."
          docker build -t test:latest -f app_python/Dockerfile.test app_python/
          echo "Runnint tests..."
          docker run test:latest
          '''
      }
    }

    stage('Build') {
      steps {
        echo 'Building..'
        script {
            pythonImage = docker.build("sgmakarov/devops", '-t latest ./app_python')
        }

      }
    }

    stage('Push to registry') {
      environment {
        registryCredentialSet = 'dockerhub'
      }
      steps {
        echo 'Publishing....'
        script {
          docker.withRegistry('', registryCredentialSet){
            pythonImage.push("${env.GIT_COMMIT}")
            pythonImage.push("latest")
          }
        }

      }
    }

    // stage('Deploy') {
    //   environment {
    //     ansibleInventoryFile = credentials('ansible-inventory-web')
    //     productionEnvfile = credentials('production-envfile')
    //   }
    //   steps {
    //     echo 'Deploying...'
    //     ansiblePlaybook(
    //       playbook: "deploy_web.yml",
    //       inventory: "$ansibleInventoryFile",
    //       extras: '-e envfilePath=$productionEnvfile'
    //     )
    //   }
    // }

  }
}
