pipeline {
  agent any
  stages {
    stage('Build test image') {
      steps {
        echo "Building test image..."
        script {
            testImage = docker.build("test", '-t latest -f ./app_python/Dockerfile.test ./app_python')
        }
      }
    }
    stage('Run tests') {
      steps {
        sh '''
            echo "Running tests..."
            docker run "test:latest"
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
