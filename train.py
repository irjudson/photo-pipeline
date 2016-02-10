#!/usr/bin/env python

import os
import argparse
from projectoxford import Client

parser = argparse.ArgumentParser()
parser.add_argument('--reference', help='Directory of reference images.')
parser.add_argument('--apikey', help='Face API license key')
parser.add_argument('--persongroup', help='Person group name.', default='testgroup')

args = parser.parse_args()

client = Client.Client('9e3535b705f44c01bdc5cc7280fd570f')

person_count = 0
client.face.personGroup.createOrUpdate(args.persongroup, "Test Group")

if os.path.exists(args.reference) and os.path.isdir(args.reference):
    for dirName, subdirList, fileList in os.walk(args.reference):
        if len(fileList) != 0 and len(subdirList) == 0:
            print "Creating Person-%d from %s" % (person_count, dirName)
            person_name = "Person-%s" % person_count
            person_count += 1
            faces = []
            for fname in fileList:
                if(fname not in [".DS_Store"]):
                    fpath = os.path.join(dirName, fname)
                    try:
                        face_result = client.face.detect({'path': fpath})
                    except Exception as e:
                        print "Error finding face in image (%s)." % fpath
                    if len(face_result) > 0:
                        faces.append(face_result[0]['faceId'])

            print "Adding faces to %s (%s)." % (person_name, ", ".join(faces))
            client.face.person.createOrUpdate(args.persongroup, faces,person_name)

print "Training person group."
client.face.personGroup.trainAndPollForCompletion(args.persongroup)

print "Done training person group, ready for testing."
# client.face.personGroup.delete(args.persongroup)