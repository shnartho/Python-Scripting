import logging
import re
import sys
import ipaddress

def main_fun():
    print("-" *70 +"Read Config"+"-" *70)
    content_of_config = readsConfiguration()
    print(content_of_config[0])
    print(content_of_config[1])
    print("-" * 125)
    read_lines_array = content_of_log_file(content_of_config[0])
    single_line = single_line_log(read_lines_array)
    request_given_ip_subnet(single_line, int(content_of_config[1].get("lines")))
    browser_of_your_choice(read_lines_array)
    print("-" * 150)
    total_number_of_bytes(content_of_config[1])
    print("-" * 150)

def readsConfiguration():
    try:
        file_nam = "lab.config"
        log_file = open(file_nam)
        content_of_file = log_file.read()

        log_file = re.compile("(\\[LogFile]\\nname=)(.*)")
        log_name = (log_file.findall(content_of_file))[0][1]
        print(log_name)

        config_file = re.compile(r'(\[Config]\ndebug=)(.*)')
        config_name = (config_file.findall(content_of_file))[0][1]
        logging_level(config_name)

        display_file = re.compile(r'(\[Display]\n)(lines=)(.*)(\nseparator=)(.*)(\nfilter=)(.*)')
        display_name = (display_file.findall(content_of_file))[0]
        print(display_name)
        lines = display_name[2]
        separator = display_name[4]
        filter = display_name[6]
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
        i = re.compile(r'(\d{1,3}\.){3}\d{1,3}')
        ip_add = i.search(line).group()

        t = re.compile(r'[(.*?)]')
        tstamp = t.search(line).group()

        h = r'\"(.*?)\"'
        http_header = (re.findall(h, line))[0]

        c = r'("\s)(\d{3})'

        http_status_code = (re.findall(c, line))[0][1]
        s = r'(\d+)(\s")'
        size = (re.findall(s, line))
        if len(size) == 1:
            size = size[0][0]
        else:
            size = 0

        single_object.append((ip_add, tstamp, http_header, http_status_code, size))
    return single_object

def request_given_ip_subnet(loglinearray, interval):
    ip_input = input("Enter your ip address:")
    ip = ip_input.strip()
    print("Student index number 268921 netmask 17 @MD Shahadat Hossen Nayem")
    netmask = "255.255.128.0"
    net = ipaddress.ip_network(ip+'/'+netmask, strict=False)
    subnet = net.network_address
    print("Net:"+ str(net))
    print("Subnet:"+ str(subnet))
    counter = 1
    for line in loglinearray:
        if belongs_to_given_subnet(line[0], netmask, subnet):
            if counter > interval and interval > 0:
                input("Press enter to continue")
                counter = 1
            print(line)
            counter += 1

def belongs_to_given_subnet(ip, mask, subnet):
    net = ipaddress.ip_network(ip+'/'+mask, strict=False)
    if net.network_address == subnet:
        return True
    else:
        return False


def browser_of_your_choice(requests):
    choice = str(input("What is your favourite browser[Chrome,Mozilla,Firefox]? "))
    for request in requests:
        pattern = re.compile(choice)
        matches = pattern.finditer(request)
        for match in matches:
            print(request)

def total_number_of_bytes(fileconfig):
    total = 0
    filter = fileconfig.get("filter")
    sep = fileconfig.get("separater")

    with open('accesslog.txt', 'r') as f:
        logs = f.readlines()
        for log in logs:
            Type = re.findall(r"\"[A-Z]{3,4}", log.split("\"-\"")[0])
            if len(Type) > 0:
                Type2 = Type[0][1:]

            stat_size = re.findall(r"\d\d\d", log.split("\"-\"")[0])
            size = stat_size[1]

            if Type2 == filter:
                total += int(size)

    print(f"Filter: {filter} \nSeperator: {sep} \nTotal: {total}")

if __name__ == "__main__":
    main_fun()