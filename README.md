# EC2 Instance Setup

This guide outlines the steps required to set up an EC2 instance and run the `setup.sh` script within the `numerai_automation` folder.

## Prerequisites

- An EC2 instance running Amazon Linux.
- Internet access from the EC2 instance.
- The EC2 instance needs full access to S3

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

   Execute the `setup.sh` script to install dependencies and configure the environment variables:

   ```bash
   cd numerai_automation
   ./setup.sh
   ```

   This script will prompt you to enter values for the required environment variables.

   - `BUCKET_NAME`: Enter the desired bucket name.
   - `NUMERAI_PUBLIC_ID`: Enter your Numerai public ID.
   - `NUMERAI_SECRET_KEY`: Enter your Numerai secret key.

   Note: Make sure to have the necessary permissions and credentials to access the specified S3 bucket.

5. **Start the Flask server:**

   The setup process is complete. You can start the Flask server by running the following command:

   ```bash
   nohup flask run --host=0.0.0.0 --port=80 &
   ```

   The server will run in the background, allowing you to access it using the public IP or domain name of your EC2 instance.

   **Note:** Ensure that the necessary security groups and firewall rules are configured to allow incoming traffic on port 80.

