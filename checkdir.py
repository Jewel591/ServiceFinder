import subprocess
import time
import os
import sys

# f_url = open("./input/ips.txt","r")
# f_name = f_url.readlines()

pwd = os.path.abspath(".") #获取当前路径
try:
    os.chdir(pwd+"/dirsearch") #切换到 subDomainsBrute 目录并调用执行 subDomainsBrute.py
except:
    print('调用 subDomainsBrute.py 失败...')
    sys.exit(0)
print('\033[1;31;8m[+] 目录猜测调用 dirsearch.py ...\033[0m')
print("python dirsearch.py -u targetip -e php -w dics/testpass.txt -x 301,302,400,403,500 -t 100 --plain-text-report=ttttt")
# subprocess.call("pwd", shell=True)

for targetip in open("../input/ips.txt","r").readlines():
    targetip = targetip.replace("\n","")
    if "ftp" in targetip:
        command = "hydra -L ./dic/ftp-user.txt -P ./dic/ftp-pass.txt -o ./output/out_sys.txt "+targetip
        subprocess.call(command, shell=True)
    if "ssh" in targetip:
        command = "hydra -L ./dic/ftp-user.txt -P ./dic/ftp-pass.txt -o ./output/out_sys.txt "+targetip
        subprocess.call(command, shell=True)
    if "http" in targetip:
        command = "python dirsearch.py -u "+ targetip +"  --timeout=3 -e php --ua='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36' -w ../dic/web-dir.txt -x 301,302,307,400,403,500 -t 100 --plain-text-report=../tmp/tmp.txt"
        subprocess.call(command, shell=True)
        ### 整个结果
        f_tmp = open("../tmp/tmp.txt" , 'r')
        for tmplist in f_tmp.readlines():
            signal = 1
            for out_weblist in open("../output/out_web.txt", 'r').readlines():  #
                if tmplist.replace("\n", "") in out_weblist.replace("\n", ""):
                    signal = 0
                    break
            if signal == 1:
                print("新增 ", tmplist.replace("\n", ""))
                open("../output/out_web.txt", 'a+').write(tmplist.replace("\n", "")+"\n")
            # if signal == 0:
            #     print s1sublist3r_out.replace("\n", ""), "存在"
    else:
        continue
