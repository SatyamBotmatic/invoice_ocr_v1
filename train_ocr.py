import matplotlib.pyplot as plt
import cv2
from pytesseract import Output
import re
import json

try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract


def plot_gray(image):
    plt.figure(figsize=(16, 10))
    return plt.imshow(image, cmap='Greys_r')


def plot_rgb(image):
    plt.figure(figsize=(16, 10))
    return plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))


def find_amounts(text):
        amounts = re.findall(r'\d+\.\d{2}\b', text)
        #amounts = re.findall(r'[0-9]+(,[0-9]+)*,?', text)
        floats = [float(amount) for amount in amounts]
        unique = list(dict.fromkeys(floats))
        return unique


def train_ocr_core(filename,reg1,reg2=None,reg3=None,reg4=None,template=None,reg5=None,reg6=None,reg7=None,reg8=None,reg9=None,reg10=None,):
    """
    This function will handle the core OCR processing of images.
    """
    text = pytesseract.image_to_string(Image.open(filename))  # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image






    amounts = find_amounts(text)

    grandtotal = max(amounts)



    #invoiceno = re.findall(r'((?<=Invoice No: ).{17})', text)
    #invoiceran = re.findall(r'((?<=Invoice No:).{17})', text)
    #invoicenum = re.findall(r'((?<=Invoice No :).{17})', text)
    #invoicenumber = re.findall(r'((?<=Invoice Number ).{17})', text)
    #invoicetry = re.findall(r'((?<=Invoice Number# ).{17})', text)
    #invoicewell = re.findall(r'((?<=Invoice Number#).{17})', text)
    #invoicesome = re.findall(r'((?<=Invoice Number #).{17})', text)



    invoice_number = re.findall(rf'((?<='+reg1+').{4,17}\s)', text)
    invoice_vendor = re.findall(rf'((?<='+reg2+').{4,17}\s)', text)
    invoice_date = re.findall(rf'((?<='+reg3+').{4,17}\s)', text)
    invoice_bill = re.findall(rf'((?<='+reg4+').{4,17}\s)', text)



    with open(template+".json", "w") as f:
        #json.dump([{"Invoice_number": reg1,"Vendor": reg2,"Invoice_date": reg3,"Invoice_bill": reg4,f"{reg5}":reg6}], f)
        f.write("[")
        json.dump({"Invoice_number": reg1},f)
        f.write(", \n")
        json.dump({"Vendor": reg2}, f)
        f.write(", \n")
        json.dump({"Invoice_date": reg3}, f)
        f.write(", \n")
        json.dump({"Invoice_bill": reg4}, f)
        f.write(", \n")
        json.dump({f"{reg5}":reg6}, f)
        f.write("] \n")



    return (invoice_number,invoice_vendor,invoice_date,invoice_bill);


