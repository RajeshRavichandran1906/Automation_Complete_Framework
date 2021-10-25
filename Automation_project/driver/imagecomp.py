import glob, os, re, sys, subprocess
from PIL import Image
from PIL import ImageChops

def compare_images(test, path_one, path_two, diff_save_location, log_file):
    """
    Compares to images and saves a diff image, if there
    is a difference
 
    @param: path_one: The path to the first image
    @param: path_two: The path to the second image
    """
    fileObj = open(log_file, "a")
    try:
        image_one = Image.open(path_one)
    except FileNotFoundError:
        fileObj.write(test + " file is not available in Base location.")
        fileObj.write("\n")
        return
    image_two = Image.open(path_two)
    one=image_one.convert('RGBA')
    two=image_two.convert('RGBA')
    
    diff = ImageChops.difference(one, two)
    
    if diff.getbbox():
        diff.save(diff_save_location)
        fileObj.write(test + " - Failed.")
        fileObj.write("\n")
    else:
        fileObj.write(test + " - Passed.")
        fileObj.write("\n")
    fileObj.close()
    
def send_email(suite, mail_list, diff_report_location):
    classpath="\\\\bigrepos01\\bigscm\\admin\\bin";
    mailto=mail_list
    mailfrom="\"qaauto@ibi.com\""
    sub="\"Image comparison Report for " + suite + ".\""
    message="\"Please Open the attachment to find the image comparison Report.\""
    diff_report=diff_report_location
    cmd="java  -cp " + classpath + ' emailtogp \"' + mailto + '\" ' + mailfrom + " " + sub + " " + message + ' \"' + diff_report + '\"'
    subprocess.Popen(cmd)
    
"""
Here is the main program.
Syntax: python imagecomp.py "D:\wf3_S9164_pdf_chart_1_cr\qa\selenium\S9164_pdf_chart_1" "se.automation@amtexsystems.com"
"""
suite=sys.argv[1]
mail_list=sys.argv[2]
root=os.getcwd()
basepath=root + "\\qa\\selenium\\" + suite
actual_image_path=basepath + "\\actual_images\\"
base_image_path=basepath + "\\images\\"
diff_image_path=basepath + "\\diff\\"
log_file=basepath + "\\diff\\image_compare.txt"

if not os.path.exists(diff_image_path):
    os.makedirs(diff_image_path)
if len(glob.glob(actual_image_path + "\\*.*")) > 1:
    for name in glob.glob(actual_image_path + "\\*.*"):
        if bool('actual.png' not in name):
            try:
                test=re.match('.*([C|c]\d+.*\.png)', name).group(1)
            except AttributeError:
                print(name+" file not found.")
            base=re.sub('Actual', 'Base', test)
            diff=re.sub('Actual', 'Diff', test)
            diff=re.sub('png', 'jpg', diff)
            base=base_image_path + base
            act=actual_image_path + test
            diff=diff_image_path + diff
            compare_images(test, base, act, diff, log_file)
    send_email(suite, mail_list, log_file)
else:
    print("There is no file to compare.")
