#!/usr/bin/python3
import argparse
import xlsxwriter
def get_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("-f", "--filename", required = True,
                        help="This is the argument for input file")
    parser.add_argument("-x", "--xlsxfile", required = True,
                        help="This is the argument for output file")
    parser.add_argument("-c", "--count", type=int, help="how many lines of information to add to one sheet")
    parser.add_argument("-w", "--web", action='store_true', help="for generate file index.html")
    args = parser.parse_args()
    return args
def get_data(fname):
    with open(fname) as f:
        content=f.readlines()
    mycont=[]
    for el in content:
        mycont.append(el.replace("\n","").split(":"))
    return mycont
def create_header(f_out,mycont,count):
    if (len(mycont)-1)%int(count) == 0:
        s = int((len(mycont)-1)/count)
    else:
        s =int((len(mycont)-1)/int(count)+1)
    workbook=xlsxwriter.Workbook(f_out)
    format1=workbook.add_format({'bold': True, 'bg_color': 'yellow'})
    color=workbook.add_format({'bg_color': 'green', 'border': 1})
    for k in range(s):
        sheet=workbook.add_worksheet("sheet"+str(k))
        header=mycont[0]
        p="Programmer"
        for i in range(len(header)):
            sheet.write(0,i, header[i], format1)
            sheet.set_column(i,0, 20,) 
        for i in range(1+k*count, count+k*count+1):
            line=mycont[i]
            for j in range(len(line)):
                if p in line:
                    sheet.write(i-k*count,j, line[j],color)
                else:
                    sheet.write(i-k*count,j, line[j])
            sheet.set_column(j,k, 20)
    workbook.close()
def create_html(fname,mycont):
    with open(fname, "w") as f:
        f.write("<!DOCTYPE html>\n<html>\n<head>\n<body>\n<title>My_table</title>\n</head>\n<body>\n<table border='2'align='center'>\n")
        for i in range(len(mycont)):
            f.write("<tr>\n")
            for j in range(len(mycont[i])):
                f.write("<td>"+mycont[i][j]+"</td>")
            f.write("</tr>")
        f.write("</table>\n</body>\n</html>")


def main():
    arguments=get_args()
    fname=arguments.filename
    f_out=arguments.xlsxfile
    count=arguments.count
    web=arguments.web
    gd=get_data(fname)
    create_header(f_out, gd, count)
    if web:
        create_html("index.html", gd)
    
if __name__ == "__main__":
    main()

