# File Uploader Module

This Python module uploads image and media files to AWS S3 and document files to Google Cloud Storage (GCS) from a specified directory and its subdirectories. The file types for each service can be configured as needed.

## Prerequisites

- Python 3.x
- AWS credentials with access to S3
- GCP credentials with access to GCS

## Installation

1. Clone the repository:

    
    git clone https://github.com/sachinot1/sacumentest.git
    

2. Install the required Python packages:

    
    pip install -r requirements.txt
    
3. Set the environment variables for AWS and GCP credentials:

   
    export AWS_ACCESS_KEY_ID='****************'
    export AWS_SECRET_ACCESS_KEY='****************'
    export AWS_REGION_NAME='****************'
    export S3_BUCKET_NAME='****************'
    export GCP_PROJECT_ID='****************'
    export GCS_BUCKET_NAME='****************'
   

## Usage

Run the script with the directory you want to process:

```bash
python solution.py <directory>
