from fpdf import FPDF
from PIL import Image

pdf = FPDF()

def main():
    name = input("Name: ")
    get_pdf(name)


def get_pdf(s):
    img = Image.open("shirtificate.png")
    text = f"{s} took CS50"
    pdf.add_page()
    pdf.set_font("helvetica", "B", size=36)
    pdf.cell(80)
    pdf.cell(30, 10, txt="CS50 Shirtificate", align='C')
    pdf.ln(20)
    pdf.image(img, x=15, y=40, w=180, h=200)
    pdf.cell(80)
    pdf.set_font("helvetica", "B", size=24)
    pdf.set_text_color(r=255, g=255, b=255)
    pdf.cell(30, 180, txt=text, align='C')
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()