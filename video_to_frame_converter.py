import cv2
cap=cv2.VideoCapture('source_videos/video1.mp4')
total_number_of_frames=int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print('How many frames do you need?')
number_of_frames_needed=int(input())
print('Nearly', number_of_frames_needed, ' number of frames will be saved in the target location.')
modulus=total_number_of_frames//number_of_frames_needed
i=0
while(cap.isOpened()):
    ret, frame=cap.read()
    if(ret==False):
        break
    if i%modulus==0:
        location='source_to_frames_converted/clean_frames/clean '+str(i)+'.jpg'
        cv2.imwrite(location, frame)
    i+=1
cap.release()
cv2.destroyAllWindows()


cap=cv2.VideoCapture('source_videos/video2.mp4')
total_number_of_frames=int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print('How many frames do you need?')
number_of_frames_needed=int(input())
print('Nearly', number_of_frames_needed, ' number of frames will be saved in the target location.')
modulus=total_number_of_frames//number_of_frames_needed
i=0
while(cap.isOpened()):
    ret, frame=cap.read()
    if(ret==False):
        break
    if i%modulus==0:
        location='source_to_frames_converted/cracked_frames/cracked '+str(i)+'.jpg'
        cv2.imwrite(location, frame)
    i+=1
cap.release()
cv2.destroyAllWindows()