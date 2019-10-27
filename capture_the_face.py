import cv2
from time import sleep

def take_a_picture(self):
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        cv2.imshow('Face capture', frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('s'):
            sleep(1)# wait a little bit to notice that picture has been taken
            image_name = 'face.jpg'
            path_to_save = 'Test/{}'.format(image_name)
            cv2.imwrite(path_to_save, frame)
        elif key == 27:
            cv2.destroyAllWindows()
            break
    cap.release()

if __name__ == '__main__':
    take_a_picture()