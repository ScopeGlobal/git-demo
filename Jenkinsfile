pipeline {
  agent any
  stages {
    stage('Clone Git') {
      steps {
        git 'https://github.com/ScopeGlobal/git-demo.git'
      }
    }
    stage('Build Code') {
      steps {
        sh "chmod u+x Prog.py"
        sh "./Prog.py"
      }
    }
    stage('Test Code') {
      steps {
        sh "chmod u+x Test.py"
        sh "./Test.py"
      }
    }
  }
}
