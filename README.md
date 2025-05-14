# 📄 AWS Document Translation Service

This project is a serverless AWS-based solution to automatically **translate documentation files** using various AWS services. It allows users to upload `.docx` documents to an S3 bucket, automatically processes and translates the content using AWS Lambda, and stores the translated documents in an output S3 bucket.

---

## 🧰 Tech Stack & AWS Services Used

- **Amazon S3** – For file storage (input/output buckets)
- **AWS Lambda** – To handle document translation logic
- **Amazon Translate** – For translating the document content
- **Amazon Cognito** – For user authentication and secure access
- **AWS IAM** – For secure role-based access control
- **AWS CloudWatch** – For monitoring and logging
  
![image](https://github.com/user-attachments/assets/5e4c49e6-7ea7-4108-9644-003e42887bde)

## 🚀 Features

- Upload `.docx` files via authenticated user
- Automatically triggers Lambda function on file upload
- Translates text using **Amazon Translate**
- Saves translated document to a separate output S3 bucket
- Fully serverless and scalable architecture

---

## 📦 S3 Bucket Structure

- **Input Bucket:** `input-translate92`
- **Output Bucket:** `output-translate92`

---

## 🔐 Authentication (Cognito)

Amazon Cognito is used to manage user authentication and permissions. Only authenticated users can upload files to the input bucket.

---

## 🛠️ How It Works

1. **User Uploads a File** to `input-translate92` bucket (e.g., `.docx` file).
2. **S3 Triggers Lambda Function** (`my-translator92`) via event.
3. **Lambda Extracts Text** from the document and translate the text.
4. **Lambda Saves Translated File** to `output-translate92` bucket.
5. **User Downloads Translated File** from the output bucket.

---

## 📋 Prerequisites

- AWS Account
- Proper IAM roles with permissions to access:
  - S3
  - Lambda
  - Translate
  - CloudWatch
- AWS CLI or AWS Console access
- Optional: Frontend app or CLI to upload/download files

---

## 📋 Setup Instructions

1. **Create S3 Buckets**:  
   - `input-translate92`
   - `output-translate92`

2. **Create IAM Role** with required policies for Lambda to access S3 and Amazon Translate.

3. **Create and Deploy Lambda Function** (`my-translator92`) with trigger on `input-translate92`.

4. **Set Up Cognito User Pool** for authentication.

5. **Test Workflow**:
   - Upload `.docx` to input bucket.
   - Check output bucket for translated document.

---

## 📈 Future Improvements

- Add UI for uploading/downloading documents
- Support for multiple file formats (PDF, TXT)
- Language selection option
- Email notifications when translation is complete
