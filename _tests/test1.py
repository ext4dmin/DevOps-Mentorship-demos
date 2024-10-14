import unittest
import subprocess
import os

class TestDockerCompose(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Bring up the Docker Compose services using the specified file
        cls.compose_up = subprocess.run(['docker', 'compose', '-f', '../docker-compose.core.yaml', 'up', '-d'], 
                                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # Check if the return code is 0
        if cls.compose_up.returncode != 0:
            raise RuntimeError("Failed to bring up Docker Compose services: " + cls.compose_up.stderr.decode())

    @classmethod
    def test_db_service(self):
        # Check if the PostgreSQL service is running
        result = subprocess.run(['docker', 'compose', '-f', '../docker-compose.core.yaml', 'ps'], 
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self.assertIn('db', result.stdout.decode(), "Database service is not running")

        # Check if the volume is created
        self.assertTrue(os.path.exists('/var/lib/docker/volumes/postgres-db-volume'), "PostgreSQL volume does not exist")

    def test_gitea_service(self):
        # Check if the Gitea service is running
        result = subprocess.run(['docker', 'compose', '-f', '../docker-compose.core.yaml', 'ps'], 
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self.assertIn('gitea-server', result.stdout.decode(), "Gitea service is not running")

        # Check if Gitea is accessible
        response = subprocess.run(['curl', '-I', 'http://localhost:3000'], 
                                   stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self.assertEqual(response.returncode, 0, "Gitea service is not accessible")

    def test_sonarqube_service(self):
        # Check if the SonarQube service is running
        result = subprocess.run(['docker', 'compose', '-f', '../docker-compose.core.yaml', 'ps'], 
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self.assertIn('sonarqube', result.stdout.decode(), "SonarQube service is not running")

        # Check if SonarQube is accessible
        response = subprocess.run(['curl', '-I', 'http://localhost:9000'], 
                                   stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self.assertEqual(response.returncode, 0, "SonarQube service is not accessible")

    def test_ssh_server_service(self):
        # Check if the SSH server service is running
        result = subprocess.run(['docker', 'compose', '-f', '../docker-compose.core.yaml', 'ps'], 
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self.assertIn('ssh-server', result.stdout.decode(), "SSH server service is not running")

        # Attempt to connect to the SSH server
        response = subprocess.run(['ssh', '-p', '2222', 'sshuser@localhost', 'exit'], 
                                   stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self.assertEqual(response.returncode, 0, "SSH server is not accessible")

    def test_web_beta_service(self):
        # Check if the beta web service is running
        result = subprocess.run(['docker', 'compose', '-f', '../docker-compose.core.yaml', 'ps'], 
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self.assertIn('web-beta', result.stdout.decode(), "Beta web service is not running")

        # Check if the beta web service is accessible
        response = subprocess.run(['curl', '-I', 'http://localhost'], 
                                   stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self.assertEqual(response.returncode, 0, "Beta web service is not accessible")

    def test_web_prod_service(self):
        # Check if the production web service is running
        result = subprocess.run(['docker', 'compose', '-f', '../docker-compose.core.yaml', 'ps'], 
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self.assertIn('web-prod', result.stdout.decode(), "Production web service is not running")

        # Check if the production web service is accessible
        response = subprocess.run(['curl', '-I', 'http://localhost'], 
                                   stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self.assertEqual(response.returncode, 0, "Production web service is not accessible")

    def test_reverse_proxy(self):
        # Check if the reverse proxy service is running
        result = subprocess.run(['docker', 'compose', '-f', '../docker-compose.core.yaml', 'ps'], 
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self.assertIn('r_proxy', result.stdout.decode(), "Reverse proxy service is not running")

        # Check if the reverse proxy is accessible
        response = subprocess.run(['curl', '-I', 'http://localhost'], 
                                   stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self.assertEqual(response.returncode, 0, "Reverse proxy is not accessible")
    def tearDownClass(cls):
        # Tear down the Docker Compose services
        subprocess.run(['docker', 'compose', '-f', '../docker-compose.core.yaml', 'down'], 
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE)

if __name__ == '__main__':
    unittest.main()