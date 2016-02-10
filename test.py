#!/usr/bin/env python

import os
import argparse
from projectoxford import Client

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='Directory of test images.')
parser.add_argument('--apikey', help='Face API license key')
parser.add_argument('--persongroup', help='Person group name.', default='testgroup')

args = parser.parse_args()

client = Client.Client('')

person_count = 0
client.face.personGroup.createOrUpdate(args.persongroup, "Test Group")

if os.path.exists(args.input) and os.path.isdir(args.input):
    for dirName, subdirList, fileList in os.walk(args.input):
        if len(fileList) != 0 and len(subdirList) == 0:
            for fname in fileList:
                if(fname not in [".DS_Store"]):
                    fpath = os.path.join(dirName, fname)
                    print "Test file: %s" % fpath

                    # Detect faces in the test image
                    face_result = client.face.detect({'path': fpath})
                    faces = [ x['faceId'] for x in face_result]
                    
                    if len(faces) > 0:
                        identifyResults = client.face.identify(args.persongroup, faces)
                        for result in identifyResults:
                            for candidate in result['candidates']:
                                confidence = candidate['confidence']
                                personData = client.face.person.get(args.persongroup, candidate['personId'])
                                name = personData['name']
                                print('identified {0} with {1}% confidence'.format(name, str(float(confidence) * 100)))
                    else:
                        print "No faces detected in %s" % fpath
