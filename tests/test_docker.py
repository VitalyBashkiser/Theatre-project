def test_docker_compose_up():
    import subprocess
    result = subprocess.run(["docker-compose", "up", "-d"], capture_output=True, text=True)
    assert "Starting" in result.stdout or "Up" in result.stdout
    subprocess.run(["docker-compose", "down"], capture_output=True, text=True)
