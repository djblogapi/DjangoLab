import face_recognition

from user.models import User


def encode_img(user_id):
    user = User.objects.get(pk=user_id)
    if user.face:
        image_path = user.face.path
        # raise Exception(image_path)
        image = face_recognition.load_image_file(image_path)
        # Find all face locations and encodings in the image
        face_locations = face_recognition.face_locations(image)
        face_encodings = face_recognition.face_encodings(image, face_locations)
        # raise Exception(type(face_encodings))
        # Loop through each face found in the image
        for i, face_encoding in enumerate(face_encodings):
            # Convert face encoding to bytes for database storage
            user.encoding = list(face_encoding)
            user.save()
