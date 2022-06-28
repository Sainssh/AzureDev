def genrate_dataset():
    face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_alt.xml");
    def face_cropper(img):
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces=face_classifier.detectMultiScale(gray,1.3,5)

        if faces is ():
            return None
        for (x,y,w,h) in faces:
            cropped_Face=img[y:y+h,x:x+w]
        return cropped_Face
    cap=cv2.VideoCapture(0)
    img_id=1

    while True:
        ret,Fram=cap.read()
        if face_cropper(Fram) is not None:
            img_id+=1
            face=cv2.resize(face_cropper(Fram),(200,200))
            face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
            file_name_path="data/"+"second."+str(img_id)+".jpg"
            #file_name_path="Visulaization/"+str(img_id)+'.jpg'
            cv2.imwrite(file_name_path,face)
            cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)

            cv2.imshow("CroppedFace",face)
            if cv2.waitKey(1)==13 or int(img_id)==1000:
                break
    
    cap.release()
    cv2.destroyAllWindows()
    print("Collection samples is completed")

genrate_dataset()

def capturePhoto():
    face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_alt.xml");
    def face_cropper(img):
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces=face_classifier.detectMultiScale(gray,1.3,5)

        if faces is ():
            return None
        for (x,y,w,h) in faces:
            cropped_Face=img[y:y+h,x:x+w]
        return cropped_Face
    cap=cv2.VideoCapture(0)
    img_id=1

    while True:
        ret,Fram=cap.read()
        if face_cropper(Fram) is not None:
            img_id+=1
            face=cv2.resize(face_cropper(Fram),(200,200))
            face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
            #file_name_path="data/"+"first."+str(img_id)+".jpg"
            file_name_path="Visulaization/"+str(img_id)+'.jpg'
            cv2.imwrite(file_name_path,face)
            cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)

            cv2.imshow("CroppedFace",face)
            if cv2.waitKey(1)==13 or int(img_id)==2:
                break
    
    cap.release()
    cv2.destroyAllWindows()
    print("Collection samples is completed")
capturePhoto()