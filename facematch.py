import face_recognition

img_of_bill = face_recognition.load_image_file('img/known/Bill Gates.jpg')
bill_face_enc = face_recognition.face_encodings(img_of_bill)[0]

unk_img = face_recognition.load_image_file('img/unknown/bill-gates-4.jpg')
unk_face_enc = face_recognition.face_encodings(unk_img)[0]



#compare faces


results = face_recognition.compare_faces([bill_face_enc],unk_face_enc)

if results[0]:
  print('this is bill')
else:
  print('not bill')  


# print(results[0])