import logging
import re
import sys


def main_fun():
    print("-" *70 +"Read Config"+"-" *70)
    content_of_config = readsConfiguration()
    print(content_of_config[0])
    print(content_of_config[1])
    print("-" * 125)

    read_lines_array = content_of_log_file(content_of_config[0])
    single_line = single_line_log(read_lines_array)



def readsConfiguration():
    try:
        file = open("lab.config")
        content_of_file = file.read()

        log_file = re.compile("(\\[Logfile]\\nname=)(.*)")
        log_name = (log_file.findall(content_of_file))[0][1]

        config_file = re.compile(r'(\[Config]\\nebug=)(.*)')
        config_name = (config_file.findall(content_of_file))[0][1]
        logging_level(config_name)

        display_file = re.compile(r'(\[Display]\n)(lines=)(.*)(\nseparator=)(.*)(\nfilter=)(.*)')
        display_name = (b.findall(read_lines))[0]
        print(display_name)
        lines = display[2]
        separator = display[4]
        filter = display[6]
        if (lines == ''):
            lines = '15'
        if (separator == ''):
            separator = '|'
        if (filter == ''):
            filter = 'GET'

        display_settings = {
            "lines": lines,
            "separator": separator,
            "filter": filter
        }

    except FileNotFoundError:
        print("config file is not present")
        logging.error("File Not Found")
        sys.exit()

    return (log_name, display_settings)

def logging_level(level):
    if level == "debug":
        logging.basicConfig(level=logging.DEBUG)
    elif level == "info":
        logging.basicConfig(level=logging.INFO)
    elif level == "error":
        logging.basicConfig(level=logging.ERROR)
    elif level == "warning":
        logging.basicConfig(level=logging.WARNING)

def content_of_log_file(file_name):
    All_log_lines = []
    try:
        f = open(file_name + ".txt")
        for line in f:
            All_log_lines.append(line)
    except FileNotFoundError:
        logging.error("File does not exist!")
        logging.error("File Not Found")
        sys.exit()
    return All_log_lines

def single_line_log(line_array):
    single_object = []
    print("-" *70 +"Extract using regular expression"+"-" *70)
    for line in line_array:
        i = re.compile(r'(d{1,3}.){3}d{1,3}')
        ip_add = i.search(line).group()

        t = re.compile(r'[(.*?)]')
        tstamp = t.search(line).group()

        h = r'"(.*?)"'
        http_header = (re.findall(h, line))[0]

        c = r'("s)(d{3})'

        http_status_code = (re.findall(c, line))[0][1]

        s = r'(d+)(s")'
        size = (re.findall(s, line))
        if len(size) == 1:
            size = size[0][0]
        else:
            size = 0

        single_object.append((ip_add, tstamp, http_header, http_status_code, size))
    return single_object


if __name__ == "__main__":
    main_fun()