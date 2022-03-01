import re
import operator


def messagesCount():
    main = {}
    with open(r'C:\\Users\\piyush\\Desktop\\final_project\\syslog.log', 'r') as f:
        pattern = r"[\w]+ \d{2} \d{2}:\d{2}:\d{2} [\w\.]+ ticky: ERROR ([\w' ]*)  ?"
        content = f.read()
        result_error = re.findall(pattern, content.strip('\n'))
        for i in result_error:
            main[i] = result_error.count(i)
    returndata = dict(
        sorted(main.items(), key=operator.itemgetter(1), reverse=True))

    with open('error_message.csv', 'w') as csvfile:
        csvfile.write("Error, Count\n")
        for key in returndata.keys():
            csvfile.write("%s, %s\n" % (key, returndata[key]))


def infoErrorCount():
    from operator import itemgetter
    pattern = r"ticky: ([\w]+) [\w' ]* (?:\[#?0?\d{4}\])? ? ?\(([\w\.]+)\)"
    field_headers = ['Username', 'INFO', 'ERROR']
    dic_holder = []

    with open(r'C:\\Users\\piyush\\Desktop\\final_project\\syslog.log', 'r') as f:
        contents = f.read().splitlines()
        users = []
        users_count = 0
        for line in contents:
            users_match = re.search(pattern, line)
            users.append(users_match.group(2))
            users = list(set(users))
        users_count += len(users)

# TODO: COMPLETE THE CODE

if __name__ == '__main__':
    messagesCount()
    print(infoErrorCount())
