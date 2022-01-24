from fpdf import FPDF
import csv




def load_report(name):
  return list(csv.reader(open(name)))



def fill_report(data,path="report.pdf",font='Arial',font_size=10):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font(font, size = font_size)
    pdf.set_left_margin(margin= 15.1)
    # create a cell
    pdf.cell(190, 10, txt = "Synthesis report",
        ln = 1, align = 'C')

    # add another cell
    pdf.cell(190, 10, txt ="Results of cards",
        ln = 2, align = 'C')
    
    line_height = pdf.font_size * 2.5
    col_width =  180/6  # distributpdfe content evenly

    for row in data:
        for datum in row:
          pdf.cell(col_width, line_height, str(datum), border=1, align="C"  )
        pdf.ln(line_height)

    
    # save the pdf with name .pdf
    pdf.output(path)

if __name__ == '__main__':
  data = load_report("report.csv")
  fill_report(data)
