import matplotlib.pyplot as plt
from datetime import date, timedelta, datetime
import numpy as np

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
def func(pct, allvals):
    absolute = int(np.round(pct/100.*np.sum(allvals)))
    return "{:.1f}%\n({:d} TestCases)".format(pct, absolute)

def generate_pie_chart(not_yet_no, automated_no, chart_title):

    labels = 'Not-Yet', 'Automated'
    sizes = [not_yet_no, automated_no]
    explode = (0, 0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')

    fig1, ax = plt.subplots(figsize=(10, 5), subplot_kw=dict(aspect="equal"))
    wedges, texts, autotexts = ax.pie(sizes, explode=explode, labels=labels, autopct=lambda pct: func(pct, sizes), shadow=True, startangle=90,
            textprops=dict(color="w"))
    ax.legend(wedges, labels,
              title="Note",
              loc="center left")

    plt.setp(autotexts, size=8, weight="bold")
    reportDate = date.today()
    chartTitle = chart_title + str(reportDate.strftime('%d-%m-%Y'))
    plt.title(chartTitle, fontsize=15, color='#FFCC00')

    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    file_name = "Testcase-report-{}.png".format(chartTitle)
    plt.savefig(file_name)
