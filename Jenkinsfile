pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git branch: 'main', 
                    url: 'https://github.com/Hritikraj8804/devops-python-app.git'
            }
        }
        stage('Build') {
            steps {
                bat 'echo Building app on Windows...'
            }
        }

        stage('Setup Environment') {
            steps {
                bat '''
                python3 -m venv venv
                . venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }


        stage('Build Docker Image') {
            steps {
                bat 'docker build -t devops-python-app:latest .'
            }
        }

        stage('Docker Login & Push') {
            steps {
                    withCredentials([usernamePassword(credentialsId: 'docker-hub-cred',
                                                  usernameVariable: 'DOCKER_USER',
                                                  passwordVariable: 'DOCKER_PASS')]) {
                        bat """
                            echo %DOCKER_PASS% | docker login -u %DOCKER_USER% --password-stdin
                            docker build -t devops-python-app:latest .
                            docker tag devops-python-app:latest %DOCKER_USER%/devops-python-app:latest
                            docker push %DOCKER_USER%/devops-python-app:latest
                        """
                    }
            }
        }

        stage('Deploy Application') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-hub-cred',
                                                  usernameVariable: 'DOCKER_USER',
                                                  passwordVariable: 'DOCKER_PASS')]) {
                    bat """
                    docker run -d -p 5000:5000 --name devops-python-app --rm %DOCKER_USER%/devops-python-app:latest
                    """
                }
            }
        }
    }
}
