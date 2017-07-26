import pprint
import boto3

SIMILARITY_THRESHOLD = 85.0

client = boto3.client('rekognition')

with open('D:\PythonProjects\Actor3.jpg', 'rb') as target_image:
    target_bytes = target_image.read()
    
response = client.compare_faces(
    SourceImage={
        #'Bytes': b'bytes',
        'S3Object': {
            'Bucket': 'raspiefacerecognition',
            'Name': 'andrew.jpg',
         
        }
    },

    TargetImage={ 'Bytes': target_bytes},
    #TargetImage={
     #   'Bytes': b'bytes',
      #  'S3Object': {
       #     'Bucket': 'raspie-facerecognition',
        #    'Name': 'andrew.jpg',
            #'Version': 'string'
       # }
    #},
    SimilarityThreshold = SIMILARITY_THRESHOLD
)

pprint.pprint(response) 
