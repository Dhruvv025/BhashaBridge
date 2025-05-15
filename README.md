# 📄 AWS Document Processing Service

This project is a serverless, AWS-based solution for automatically processing `.txt` documentation files. 
Users securely upload documents using an AWS Transfer Family web endpoint. 
A Lambda function is triggered upon file upload to process the document, and the result is stored in an output S3 bucket.

---

## 🧰 Tech Stack & AWS Services Used

- **Amazon S3** – For file storage (input/output)
- **AWS Lambda** – Executes document processing logic
- **AWS Transfer Family (Web Access)** – For secure file uploads
- **AWS IAM** – Manages access control
- **Amazon CloudWatch** – Monitors execution and logs

---

## 🚀 Features

- Upload `.txt` files via AWS Transfer Family Web Interface
- Auto-triggers Lambda on file upload to the input bucket
- Lambda handles file processing logic
- Stores results in an output S3 bucket
- Fully serverless architecture (scalable and low-maintenance)

---

## 📦 S3 Bucket Structure

- **Input Bucket:** `input-translate92`
- **Output Bucket:** `output-translate92`

---

## 🔐 User Access via Transfer Family

Users interact with the system via an AWS Transfer Family Web Endpoint. Each user is mapped to a scoped IAM role with permission to upload files only to the input bucket.

---
## 🔐 Architecture
![image](https://github.com/user-attachments/assets/c49827e7-58c8-474b-af8a-f2f63e38e924)

## Screenshots

![Screenshot 2025-05-15 111153](https://github.com/user-attachments/assets/8ddb6430-4580-4792-9bb9-348da08c659e)

![Screenshot 2025-05-15 111726](https://github.com/user-attachments/assets/3bc90c15-d3d9-4b0a-9bff-50b74d89cc0a)

![WhatsApp Image 2025-05-15 at 11 21 08_0e24b3f4](https://github.com/user-attachments/assets/feecbb07-3c8c-403c-b26c-79123ef045c1)

## 🛠️ How It Works

1. User uploads a `.txt` file to the input bucket via Transfer Family Web
2. The S3 upload triggers the `my-translator92` Lambda function
3. Lambda processes the document (e.g., extracts/edits content)
4. Lambda writes the processed file to the output bucket
5. User accesses the output via Transfer Family or another interface

---

## 📋 Prerequisites

- AWS Account
- Two S3 Buckets:
  - `input-translate92`
  - `output-translate92`
- IAM Roles:
  - For Lambda (access to both buckets)
  - For Transfer Family user access (input bucket only)
- Lambda function configured with S3 trigger
- AWS Transfer Family server (web enabled)

---

## ⚙️ Setup Instructions

1. **Create S3 Buckets**
   - `input-translate92`
   - `output-translate92`

2. **Set Up IAM Roles**
   - Lambda role: S3 access for input/output buckets
   - Transfer Family role: limited access to input bucket

3. **Deploy Lambda Function**
   - Name: `my-translator92`
   - Trigger: S3 event on `input-translate92`

4. **Configure AWS Transfer Family**
   - Set up Web-enabled server
   - Create user and link to IAM role and input bucket

5. **Test Workflow**
   - Upload a `.txt` file via Transfer Family Web
   - Monitor processing in CloudWatch Logs
   - Download processed file from output bucket

---

## 📈 Future Improvements

- UI for monitoring and file management
- Support for more file formats (e.g., PDF, DOCX)
- Language selection or configuration support
- Notification system (e.g., SNS or email on completion)
