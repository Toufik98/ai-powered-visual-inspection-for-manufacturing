"""
This program allows to generate pdf synthesis report. Make sure the fpdf package is well installed.
"""

#pip install fpdf

from fpdf import FPDF
import csv
import seaborn as sns
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt


class PDF(FPDF):
    def header(self):
        # Logo
        self.image('valeo_logo.png', 10, 8, 33)
        # Arial bold 15
        self.set_font('Arial', 'B', 15)
        # Move to the right
        self.cell(80)
        # Title
        self.cell(40, 10, 'Synthesis report', 'C')
        # Line break
        self.ln(20)

    # Page footer
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()) , 0, 0, 'C')

  
    def chapter_title(self, label):
        # Arial 12
        self.set_font('Arial', '', 12)
        # Background color
        self.set_fill_color(200, 220, 255)
        # Title
        self.cell(0, 6, ' %s' % (label), 0, 1, 'L', 1)
        # Line break
        self.ln(4)

    def chapter_body(self, name):
        # Read text file
        if name != " ": 
          with open(name, 'rb') as fh:
              txt = fh.read().decode('latin-1')
          # Times 12
          self.set_font('Times', '', 10)
          # Output justified text
          self.multi_cell(0, 5, txt)
          # Line break
          self.ln()
          # Mention in italics
          self.set_font('', 'I')
          #self.cell(0, 5, '(end of excerpt)')

    def print_chapter(self, title, name):
        self.chapter_title( title)
        self.chapter_body(name)



    def fill_report(self,data,path="report",font='Arial',font_size=10):
        self.add_page()
        # create a cell
        

        # add another cell
        self.print_chapter( 'Results of inspection'," ")
        

        self.set_font(font, size = font_size)
        self.set_left_margin(margin= 10.1)

        
        col_width =  190/6  # distributpdfe content evenly
        #pdf.set_font(size = 0)
        self.set_font('Times', '', 6)
        line_height = pdf.font_size * 2.5
        for row in data:
            for datum in row:
              self.cell(col_width, line_height, str(datum), border=1, align="C"  )
            self.ln(line_height)
        self.cell(190, 10, txt =" ",
            ln = 2, align = 'C')
        self.set_font('Arial', '', 10)
        # Add counting of defected/ Not defected according to dies
        df = pd.DataFrame(data[1:],columns = data[0])
        sns_plot1 = sns.histplot(df, x="Decision", hue= "DIE",multiple="dodge",binwidth=3,shrink=.8)
        sns_plot1.figure.savefig("output1.png")
        self.image("output1.png",x=50,w=100,h=70)
        plt.close(sns_plot1.figure)
        
        # Add count according to decision
        sns_plot2 = sns.histplot(df, x="Decision",binwidth=3)
        sns_plot2.figure.savefig("output2.png")
        self.image("output2.png",x=50,w=100,h=70)
        plt.close(sns_plot2.figure)

        # Add time series informations 
        df['Date'] = pd.to_datetime(df['Date']).dt.date
        dx =df.groupby(['Date','Decision'])["Card_Name"].count()
        dx= dx.reset_index()
        palette = sns.color_palette("mako_r", 2)
        sns_plot3 = sns.lineplot(x="Date", y='Card_Name',
                    hue="Decision",
                    data=dx,palette=palette).set_title("Time-Series representation- Monthly aggregation")
        plt.xticks(rotation=30)
        plt.ylabel("Numbers of cards")
        sns_plot3.figure.savefig("output3.png")
        self.image("output3.png",x=50,w=110,h=70)
        plt.close(sns_plot3.figure)
        # save the pdf with name .pdf

        pdf.cell(190, 10, txt =" ",
            ln = 2, align = 'C')
        
        # generate conclusion according to numbers of defected and non defecte cards
        dy = df["Decision"].value_counts()
        
        if dy['Defected']>= dy['NOT Defected']:
          result = "negatif.txt"
        elif  2*dy['Defected']> dy['NOT Defected']:
          result = "medium.txt"
        else: 
            result = "positif.txt"
      
        self.print_chapter( 'Conclusion', result)

        # save pdf
        self.output(path+".pdf")


    
def load_report(name):
  return list(csv.reader(open(name)))




if __name__ == '__main__':
  name = "report"+"_"+datetime.today().strftime('%Y-%m-%d')+".csv"
  data = load_report(name)
  pdf = PDF()
  pdf.fill_report(data,path = name [:-4])
