import execjs
import os, sys, json
import urllib
import urllib.request as urllib2
from workflow import Workflow3, ICON_WARNING

u = 'https://tenhou.net/2/?q='


def main(wf):
    url = u + wf.args[0]
    q = url.split('=')[1]
    with open('tenhou_decrypt.js', 'r', encoding='utf-8') as f:
        tenhou_js = f.read()
    data = execjs.compile(tenhou_js).call('fa', q)
    flag = 0
    for line in data.splitlines():
        if flag == 0:
            flag = 1
            continue
        icon = "image/" + line[1 : 3] + ".gif"
        m, s, p, z = 0, 0, 0, 0
        for i in range(3, len(line)):
            if line[i] == 'm': m += 1
            if line[i] == 's': s += 1
            if line[i] == 'p': p += 1
            if line[i] == 'z': z += 1
        line = line[:3] + line[3:].replace('m','', m - 1)
        line = line[:3] + line[3:].replace('s','', s - 1)
        line = line[:3] + line[3:].replace('p','', p - 1)
        line = line[:3] + line[3:].replace('z','', z - 1)
        wf.add_item(line, icon = icon)
    wf.send_feedback()


if __name__ == '__main__':
    wf = Workflow3()
    sys.exit(wf.run(main))
