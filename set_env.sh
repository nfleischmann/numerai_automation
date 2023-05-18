# Ask for environment variables
read -p "Enter BUCKET_NAME: " bucket_name
export BUCKET_NAME=$bucket_name

read -p "Enter NUMERAI_PUBLIC_ID: " public_id
export NUMERAI_PUBLIC_ID=$public_id

read -p "Enter NUMERAI_SECRET_KEY: " secret_key
export NUMERAI_SECRET_KEY=$secret_key