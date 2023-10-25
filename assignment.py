import PyPDF2
import fitz 
import io
from PIL import Image


a = PyPDF2.PdfReader('dharamsotu2019.pdf')#write your pdf's name in this 
#print(a.metadata)#for printing details of pdf files
#print(len(a.pages))for getting length of pages of file 
str=""
for i in range (1,10):
    str +=a.pages[i].extract_text()
with open("data.txt","w",encoding='utf-8') as f:
    f.write(str)

#code for extracting images from code

def extract_images_from_pdf(pdf_path, output_folder):
    doc = fitz.open(pdf_path)
    
    for page_num in range(doc.page_count):
        page = doc.load_page(page_num)
        image_list = page.get_images(full=True)
        
        for img_index, img in enumerate(image_list):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_data = base_image["image"]
            
            image = Image.open(io.BytesIO(image_data))
            image.save(f'{output_folder}/image_{page_num + 1}_{img_index}.png')

    doc.close()

# Specify the PDF file and output folder
pdf_path = 'dharamsotu2019.pdf'#set your pdf origins path
output_folder = 'images_of_pdf'#set the path where you want put the images 


# Create the output folder if it doesn't exist
import os
os.makedirs(output_folder, exist_ok=True)

# Extract images from the PDF
extract_images_from_pdf(pdf_path, output_folder)
