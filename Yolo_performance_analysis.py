
import re
import os
import sys
import csv


console_file_name = open("/pallawi/out.txt","r")
number_of_iteration = 693

analysia_output_csv_path = '/Users/pallawi/'
# 1729

def get_output_line(number_of_iteration,console_file_name,analysia_output_csv_path):
    print "function called"
    analysis_dictonary = {}
    for check in range(1,number_of_iteration):
        make_pattern = str(check) + ":"
        print make_pattern
        for line in console_file_name:
            matchObj = re.match(make_pattern, line, re.M|re.I)
            if matchObj :
                # print line
                iteration_temp = line.split(',')

                iteration = iteration_temp[0].split(':')[0]
                total_loss = iteration_temp[0].split(':')[1]
                average_loss_error = iteration_temp[1].split('avg')[0]
                rate = iteration_temp[2].split('rate')[0]
                batch_process_time = iteration_temp[3].split('seconds')[0]
                num_img_training = iteration_temp[4].split('images\n')[0]

                analysis_dictonary["iteration"] = iteration
                analysis_dictonary["total_loss"] = total_loss
                analysis_dictonary["average_loss_error"] = average_loss_error
                analysis_dictonary["rate"] = rate
                analysis_dictonary["batch_process_time"] = batch_process_time
                analysis_dictonary["num_img_training"] = num_img_training

                print "analysis_dictonary",analysis_dictonary
                print "iteration",iteration
                print "total_loss",total_loss
                print "average_loss_error",average_loss_error
                print "rate",rate
                print "batch_process_time",batch_process_time
                print "num_img_training",num_img_training

                PATH = analysia_output_csv_path + "training_analysis.csv"
                csvfile = open( PATH, 'aw')
                filename = PATH
                fileEmpty = os.stat(filename).st_size == 0
                fieldnames = ['iteration','total_loss','average_loss_error','rate','batch_process_time','num_img_training']
                with csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    if fileEmpty:
                        writer.writeheader()
                    writer.writerow(analysis_dictonary)

                break;


if __name__ == '__main__':
    get_output_line(number_of_iteration,console_file_name,analysia_output_csv_path)
