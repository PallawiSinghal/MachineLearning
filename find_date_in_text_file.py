# coding: utf-8
import cv2
import re
import os
from difflib import get_close_matches

folder_path = "/home/Curl/Data/save_ocr/"

date_patterns = ["date"]
def date_search(fileName):
    print"num_lines",num_lines
    textfile = open(fileName, 'r')
    # content = textfile.readlines()
    for lines in textfile:
        line = lines.rstrip()
        line = re.sub(r"[“?|$|!:]", "", line)
        date_pattern = "date"
        found_match = re.findall(date_pattern,line)
        if found_match:
            print "----------------------------start-------------------"
            # print "Each line------>",line
            line_list = line.split()
            # print "line_list----->>",line_list
            line_list_length = len(line_list)
            # print "line_list_length",line_list_length
            if date_pattern not in line_list:
                found_match = re.search("(date.*)", lines)
                if found_match:
                    # print lines
                    data_of_date = found_match.group(1)
                    print "found_match_for_date---------------------------------------------------------->>>>>>>",found_match.group(1)
            else:
                matched_index_location = line_list.index(date_pattern)
                # print "matched_index_location",matched_index_location
                take_length = line_list_length - matched_index_location
                # print "take_length--->>",take_length
                data_of_date = ''.join(line_list[matched_index_location:line_list_length])
                print "data_of_date------------------------------------------------------------------------>>>>>>>",data_of_date

                print "----------------------------stop-------------------------"

if __name__ == '__main__':
    text_files = os.listdir(folder_path)
    for singletext in text_files:
        print "singletext",singletext
        full_path = folder_path + singletext
        num_lines = 0

        date_search(full_path)
