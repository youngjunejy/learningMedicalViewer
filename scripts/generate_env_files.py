import subprocess

def generate_requirements_txt():
    try:
        # Execute the conda list --export command and redirect output to requirements.txt
        with open('requirements.txt', 'w') as f:
            subprocess.run(['conda', 'list', '--export'], stdout=f, check=True)
        print("requirements.txt generated successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error generating requirements.txt: {e}")

def generate_environment_yml():
    try:
        # Execute the conda env export command and redirect output to environment.yml
        with open('environment.yml', 'w') as f:
            subprocess.run(['conda', 'env', 'export'], stdout=f, check=True)
        print("environment.yml generated successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error generating environment.yml: {e}")

if __name__ == "__main__":
    generate_requirements_txt()
    generate_environment_yml()