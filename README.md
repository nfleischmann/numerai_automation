# EC2 Instance Setup

This guide outlines the steps required to set up an EC2 instance and run the `setup.sh` script within the `numerai_automation` folder.

## Prerequisites

- An EC2 instance running Amazon Linux.
- Internet access from the EC2 instance.

## Setup Steps

1. **Update package lists:**

   Connect to your EC2 instance via SSH and run the following command:

   ```bash
   sudo yum update -y
   ```

2. **Install git:**

   Run the following command to install git:

   ```bash
   sudo yum install -y git
   ```

3. **Clone the repository:**

   Run the following command to clone this repository:

   ```bash
   git clone https://github.com/nfleischmann/numerai_automation.git
   ```

4. **Run the `setup.sh` script:**

   This script installs the necessary dependencies and configures the environment variables:
   First, navigate to the repository's directory:
    ```bash
    cd numerai_automation
    ```
    Next, grant the necessary permissions:
   ```bash
   chmod +x setup.sh
   ```
   Finally, run the script:
   ```bash
   ./setup.sh
   ```

5. **Start the Flask server:**

   The setup process is complete. You can start the Flask server by running the following command:

   ```bash
   flask run --host=0.0.0.0 --port=80
   ```

