import io
import os


def text_files_to_csv(files,cell_num):

    plus = [f+'\\'+c for f,c in zip(files,cell_num)]
    rows = []
    text =''
    html = ''
    for p in plus:
        row, column = map(int, p.split("\\")[1].split("-"))
        chr = p.split("\\")[0]

        if row == len(rows):
            rows.append([])

        rows[row].append(chr)


        text = to_text(rows)
        html = to_html(rows)
        html_test = to_html_test(rows)
        html_last_test = file_html2(rows)
        # 지우기
        # html_file = file_html(rows)

        # 지우기
    # 지우기
    # bn = r'C:\Users\user\Desktop\normal\final-test\aaa\bbb'
    # basename = basename + '.html'
    # basename = os.path.join(bn, basename)
    # with open(basename, 'w') as html_files:
    #     html_files.write(html_file)
    # 지우기

    return text, html_last_test


def to_text(rows):
    text_string_return = ''
    for row_index in rows:
        for column_index in row_index:
            if column_index == '':
                text_string_return = text_string_return + (' NaN') + ('\t')
            else :
                text_string_return = text_string_return + (' ') + column_index  + ('\t')
        text_string_return = text_string_return +('\n')

    text_string_return = text_string_return[:-1]

    return text_string_return


    # for f in files:
    #
    #     directory, filename = os.path.split(f)
    #     with open(f) as of:
    #         txt = of.read().strip()
    #
    #     row, column = map(int, cell_num.split(".")[0].split("-"))   #000-000.gt.txt -> .으로 나눈뒤 0번째를 - 로 나눈뒤 row와 column에 저장
    #     if row == len(rows):
    #         rows.append([])
    #
    #     rows[row].append(f)



def to_html(rows):
    html_string_return ='<table></table>'

    for row_index in rows:
        html_string_return = html_string_return[:-8]+'<tr>'+html_string_return[-8:]
        for column_index in row_index:
            if column_index == '':
                html_string_return = html_string_return[:-8]+'<td>' + 'NaN' + '</td>'+html_string_return[-8:]
            else:
                html_string_return = html_string_return[:-8]+ '<td>' + column_index + '</td>'+html_string_return[-8:]
        html_string_return = html_string_return[:-8] + '</tr>'+html_string_return[-8:]

    return html_string_return

def to_html_test(rows):
    html_string_return = '<table><tbody></tbody></table>'

    for row_index in rows:
        html_string_return = html_string_return[:-16] + '<tr>' + html_string_return[-16:]
        for column_index in row_index:
            if column_index == '':
                html_string_return = html_string_return[:-16] + '<td>'+ html_string_return[-16:]
            else:
                html_string_return = html_string_return[:-16] + '<td>'+ html_string_return[-16:]
        html_string_return = html_string_return[:-16] + '</tr>' + html_string_return[-16:]

    return html_string_return


def file_html(rows):
    html_string_return = '<table border = "1"></table>'

    for row_index in rows:
        html_string_return = html_string_return[:-8]+'<tr>'+html_string_return[-8:]
        for column_index in row_index:
            if column_index == '':
                html_string_return = html_string_return[:-8]+'<td>' + 'NaN' + '</td>'+html_string_return[-8:]
            else:
                html_string_return = html_string_return[:-8]+ '<td>' + column_index + '</td>'+html_string_return[-8:]
        html_string_return = html_string_return[:-8] + '</tr>'+html_string_return[-8:]


    return html_string_return

def file_html2(rows):
    html_string_return ='<table></table>'

    for row_index in rows:
        html_string_return = html_string_return[:-8]+'<tr>'+html_string_return[-8:]
        for column_index in row_index:
            if column_index == '':
                html_string_return = html_string_return[:-8]+'<td>'+'</td>'+html_string_return[-8:]
            else:
                html_string_return = html_string_return[:-8]+ '<td>'+'</td>'+html_string_return[-8:]
        html_string_return = html_string_return[:-8] + '</tr>'+html_string_return[-8:]

    return html_string_return

    # 지우기



    """
    dir = os.path.dirname(save_filepath)   #디렉토리 이름 검출



    csv_file_name = 'table_csv.csv'                 #csv파일 이름
    csv_name = os.path.join(dir, csv_file_name)
    csv_file = io.StringIO()
    writer = csv.writer(csv_file)
    writer.writerows(rows)
    with open(csv_name, 'w', newline='') as cf:
        writer2 = csv.writer(cf)
        writer2.writerows(rows)

    html_file_name = 'table_html.html'
    html_name = os.path.join(dir, html_file_name)
    html_file = open(html_name,'w')
    html_file.write(html_string)
    html_file.close()
    """
