# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 12:40:19 2017

@author: issguest
"""

import boto3
s3 = boto3.resource('s3')
bucket = s3.Bucket('raspiefacerecognition')
targetBucket = "raspiefacerecognition"
#srcBucket = A source bucket may not be required for my thing. 

#--------------------- Upload your Target Images ------------------------------ 

end = ''
while(end != 'END'):
    uploadedImage = input("Enter Filename. If no files to add, type [END]: ")
    if(uploadedImage == 'END'):
        break 
    s3.meta.client.upload_file(uploadedImage, "raspiefacerecognition", uploadedImage)
    end = input("End now or add more files? Type [END] for end, [ADD] for add]: ")

    
Target_List = [] #A list of all the people who are in your collection. 

for key in bucket.objects.all():
    Target_List.append(key.key)
       
length_target_list = len(Target_List)
print(length_target_list)
