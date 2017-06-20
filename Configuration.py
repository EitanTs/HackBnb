# coding=utf-8
__author__ = 'Ido Bichler'

REVIEW_PARAMS = ['Clean', 'Noise', 'bathrooms', 'Silence', 'Snoring']
BED_ID_FORMAT = "{building}_{room_number}_{bed_number}"
ROOM_ID_FORMAT = "{building}_{room_number}"
BED_PLACES = {
    1: 'צד ימין ליד הדלת למטה',
    2: 'צד ימין ליד הדלת למעלה',
    3: 'צד שמאל ליד הדלת למטה',
    4: 'צד שמאל ליד הדלת למעלה',
    5: 'צד ימין ליד החלון למעלה',
    6: 'צד ימין ליד החלון למטה',
    7: 'צד שמאל ליד החלון למטה',
    8: 'צד שמאל ליד החלון למעלה'
}