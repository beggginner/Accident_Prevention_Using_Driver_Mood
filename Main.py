from scipy.spatial import distance as dist
import playsound
def eye_aspect_ratio(eye):
    # compute the euclidean distances between the two sets of
    # vertical eye landmarks (x, y)-coordinates
    A = dist.euclidean(eye[1], eye[5])
    B = dist.euclidean(eye[2], eye[4])

    # compute the euclidean distance between the horizontal
    # eye landmark (x, y)-coordinates
    C = dist.euclidean(eye[0], eye[3])

    # compute the eye aspect ratio
    ear = (A + B) / (2.0 * C)

    # return the eye aspect ratio
    return ear


# define two constants, one for the eye aspect ratio to indicate
# blink and then a second constant for the number of consecutive
# frames the eye must be below the threshold for to set off the
# alarm
EYE_AR_THRESH = 0.3
EYE_AR_CONSEC_FRAMES = 48

# Next we'll calculate EAR for both left and right eye and then take average
## leftEAR = eye_aspect_ratio(leftEye)
## rightEAR = eye_aspect_ratio(rightEye)
ear=0.0
COUNTER=0
## ear = (leftEAR + rightEAR) / 2.0
# check to see if the eye aspect ratio is below the blink
# threshold, and if so, increment the blink frame counter
if ear < EYE_AR_THRESH:
    COUNTER += 1
    #we'll check this condition for many frames of the live face stream
    # if the eyes were closed for a sufficient number of
    if COUNTER >= EYE_AR_CONSEC_FRAMES:
        # then sound the alarm
        playsound.playsound('alarm.wav')
