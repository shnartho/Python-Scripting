import json


def run():
    print("-" * 150)
    print("Start")
    print("-" * 150)
    ask_configuration()

def ask_configuration():
    nameWebServer = str(input('Name of the web server log: '))
    ipAddress = str(input('IP Address(to be used as a filter for displaying) : '))
    loggingLevel = str(input('Logging level used by the application: '))
    numOfLines = input('Number of lines to be displayed at once: ')
    nameUser = str(input('Which Search Engine are you using (eg. www.bing.com ): '))

    configuration = {
        "Name_Web_Server": nameWebServer,
        "Ip_Address": ipAddress,
        "Logging_Level": loggingLevel,
        "Number_of_Lines": numOfLines,
        "Name": nameUser
    }
    with open('configuration.json', 'w') as file:
        json.dump(configuration, file)
        # file.write('\n')

if __name__ == "__main__":
    run()
