#!/usr/bin/env python

import os
import argparse
from projectoxford import Client

parser = argparse.ArgumentParser()
parser.add_argument('--source', help='Directory of source images.')
parser.add_argument('--persongroup', help='Person group name.', default='testgoup')

args = parser.parse_args()

client = Client.Client('')

face_count = 0
face_lists = []


if os.path.exists(args.source) and os.path.isdir(args.source):
    for dirName, subdirList, fileList in os.walk(args.source):
        if len(fileList) != 0 and len(subdirList) == 0:
            # Find faces
            for fname in fileList:
                if(fname not in [".DS_Store"]):
                    fpath = os.path.join(dirName, fname)
                    try:
                        face_result = client.face.detect({'path': fpath})
                    except Exception as e:
                        print "Error finding face in image (%s)." % fpath

                    # Go through each face
                    for face in face_result:
                        similar_faces = []
                        for face_list in face_lists:
                            client.face.
                    
                        # Check each face list for similar faces
            
            # Do something with the similar faces
            
            print "Creating Person-%d from %s" % (person_count, dirName)
            person_name = "Person-%s" % person_count
            person_count += 1
            faces = []
            

            print "Adding faces to %s (%s)." % (person_name, ", ".join(faces))
            client.face.person.createOrUpdate(args.persongroup, faces,person_name)

print "Training person group."
client.face.personGroup.trainAndPollForCompletion(args.persongroup)

print "Done training person group, ready for testing."
# client.face.personGroup.delete(args.persongroup)