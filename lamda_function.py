import json
import boto3

# Create S3 and Translate client
s3_client = boto3.client(service_name='s3')
translate = boto3.client(service_name='translate')

def translate_text(text, lang_code):
    result = translate.translate_text(
        Text=text,
        SourceLanguageCode='auto',
        TargetLanguageCode=lang_code
    )
    return result['TranslatedText']

def lambda_handler(event, context):
    # Extract file name and bucket name from event
    file_name = event['Records'][0]['s3']['object']['key']
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    output_bucket = 'output-translate92'  # Change this if using another bucket

    print("Event details: ", event)
    print("Input File Name: ", file_name)
    print("Input Bucket Name: ", bucket_name)

    # Get the S3 object (text file)
    result = s3_client.get_object(Bucket=bucket_name, Key=file_name)

    # Read file content and translate line by line
    final_document = ""
    for line in result["Body"].read().splitlines():
        each_line = line.decode('utf-8')
        print("Input Line: ", each_line)
        if each_line.strip() != '':
            translated = translate_text(each_line, 'gu')  # Gujarati language code
            print("Translated Line: ", translated)
            final_document += translated + '\n\n'

    # Put translated content to output S3 bucket
    s3_client.put_object(Body=final_document, Bucket=output_bucket, Key=file_name)
    print("Translation completed and uploaded to:", output_bucket)
