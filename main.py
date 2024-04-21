import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import END, ttk
from tkinter import messagebox
import os

root=tk.Tk()

headers= {'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
lyrics_up_part = '<!-- Usage of azlyrics.com content by any third-party lyrics provider is prohibited by our licensing agreement. Sorry about that. -->'
lyrics_down_part = '<!-- MxM banner -->'
y= [9,74,139,204,269]; destroy=[]; pn='Pyrics_v1.0'

os.system('if not exist c:\\Python\\Pyrics (mkdir c:\\Python\\Pyrics)')


def start():
    global aa; aa=[]
    aa.append(ae1.get())
    aa.append(ae2.get())
    aa.append(ae3.get())
    aa.append(ae4.get())
    aa.append(ae5.get())

    global ss; ss=[]
    ss.append(se1.get())
    ss.append(se2.get())
    ss.append(se3.get())
    ss.append(se4.get())
    ss.append(se5.get())

    if (aa[0],aa[1],aa[2],aa[3],aa[4],ss[0],ss[1],ss[2],ss[3],ss[4])!=('','','','','','','','','',''):
        root.title('Pyrics_v1.0 - Processing . . .')

        global hlb; hlb=[] #存放 Button (取 Button 的 y 座標 = 取 hl 的 key 值)
        global hl; hl={} #存放網址 (取 value 值)
        global hll; hll=[] #供 def 使用

        global tlb; tlb=[] #存放 Button (取 Button 的 y 座標 = 取 tl 的 key 值
        global tl; tl={} #存放 txt 標題 (取 value 值)
        global tll; tll=[] #供 def 使用

        for i in range(5):

            if aa[i]!='' and ss[i]!='':
            
                try:
                    artistname= aa[i].replace(' ','').replace('-','').lower()
                    songtitle= ss[i].replace(' ','').replace('-','').lower()
                    
                    url=ht= f'https://www.azlyrics.com/lyrics/{artistname}/{songtitle}.html' #暫存網址
                    html= requests.get(url, headers=headers)
                    soup = BeautifulSoup(html.text, 'html.parser')
                    
                    ly = str(soup)
                    ly = ly.split(lyrics_up_part)[1]
                    ly = ly.split(lyrics_down_part)[0]
                    ly = ly.replace('<br>','').replace('</br>','').replace('<br/>','').replace('</div>','').replace('</i>','').replace('<i>','').strip()

                    lyrics= list(ly.split('\n'))

                    ac= soup.find_all('b')[0].string[:-7] #確認過的 artist name
                    sc= soup.find_all('b')[1].string[1:-1] #確認過的 song titl

                    try:
                        feat= soup.find('span', class_='feat').get_text()
                        save= open(f'C:\\Python\\Pyrics\\{ac} - {sc} {feat}.txt','w+')
                        save.write(f'{ac} - {sc}\n{feat}\n\n')
                        tt= f'{ac} - {sc} {feat}' #暫存 txt 標題 (當 tl 的 value 值)
                    except:
                        save= open(f'C:\\Python\\Pyrics\\{ac} - {sc}.txt','w+')
                        save.write(f'{ac} - {sc}\n\n')
                        tt= f'{ac} - {sc}' #暫存 txt 標題 (當 tl 的 value 值)

                    for wl in lyrics: save.write(wl+'\n')
                    save.close()
                    st[i]['background']='green'

                    tlt= ttk.Button(root,text='txt'); tlt.place(x=355,y=y[i]) #暫存 Button (當 tl 的 key 值)
                    tlb.append(tlt)
                    destroy.append(tlt)
                    tl[tlt.place_info()['y']]=tt # {y 座標: 歌曲名稱}
                    hlt= ttk.Button(root,text='web page'); hlt.place(x=355,y=y[i]+25) #暫存 Button (當 hl 的 key 值)
                    hlb.append(hlt)
                    destroy.append(hlt)
                    hl[hlt.place_info()['y']]=ht # {y 座標: 網址}

                except:
                    st[i]['background']='red'
                    h4t= ttk.Button(root,text='?',command=error); h4t.place(x=355, y=y[i]) #暫存 HTTP 404 說明
                    destroy.append(h4t)

            elif aa[i]=='' and ss[i]=='': pass

            else:
                st[i]['background']='orange'
                ebt= ttk.Button(root,text='?',command=error); ebt.place(x=355, y=y[i]) #暫存 error blank 說明
                destroy.append(ebt)

        for i in range(len(tlb)):
            tll.append(tl[tlb[i].place_info()['y']]) #歌曲名稱
            tlb[i]['command']=file[i]
        for i in range(len(hlb)):
            hll.append(hl[hlb[i].place_info()['y']]) #網址
            hlb[i]['command']=browse[i]

        root.title(pn)
        messagebox.showinfo(pn,'DONE')

def clear():
    ae1.delete(0,END)
    ae2.delete(0,END)
    ae3.delete(0,END)
    ae4.delete(0,END)
    ae5.delete(0,END)
    se1.delete(0,END)
    se2.delete(0,END)
    se3.delete(0,END)
    se4.delete(0,END)
    se5.delete(0,END)
    root.title(pn); destro()

def destro():
    for st_ in st: st_['background']='white'
    for de in destroy: de.destroy()

def dir(): os.system('start c:\\Python\\Pyrics')

def browse0(): os.system(f'start {hll[0]}')
def browse1(): os.system(f'start {hll[1]}')
def browse2(): os.system(f'start {hll[2]}')
def browse3(): os.system(f'start {hll[3]}')
def browse4(): os.system(f'start {hll[4]}')
browse= [browse0, browse1, browse2, browse3, browse4]

def file0():
    if not '&' in tll[0]: os.system(f'"c:\\Python\\Pyrics\\{tll[0]}.txt"')
    else: dir()
def file1():
    if not '&' in tll[1]: os.system(f'"c:\\Python\\Pyrics\\{tll[1]}.txt"')
    else: dir()
def file2():
    if not '&' in tll[2]: os.system(f'"c:\\Python\\Pyrics\\{tll[2]}.txt"')
    else: dir()
def file3():
    if not '&' in tll[3]: os.system(f'"c:\\Python\\Pyrics\\{tll[3]}.txt"')
    else: dir()
def file4():
    if not '&' in tll[4]: os.system(f'"c:\\Python\\Pyrics\\{tll[4]}.txt"')
    else: dir()
file= [file0, file1, file2, file3, file4]

def error():
    messagebox.showinfo(pn,'Web page not found.\nPlease check whether both of ARTIST NAME and SONG TITLE are correct or unblank.\n')


ttk.Label(root,text='ARTIST NAME').place(x=10,y=10); ae1= ttk.Entry(root); ae1.place(x=105,y=9)
ttk.Label(root,text='ARTIST NAME').place(x=10,y=75); ae2= ttk.Entry(root); ae2.place(x=105,y=74)
ttk.Label(root,text='ARTIST NAME').place(x=10,y=140); ae3= ttk.Entry(root); ae3.place(x=105,y=139)
ttk.Label(root,text='ARTIST NAME').place(x=10,y=205); ae4= ttk.Entry(root); ae4.place(x=105,y=204)
ttk.Label(root,text='ARTIST NAME').place(x=10,y=270); ae5= ttk.Entry(root); ae5.place(x=105,y=269)
ttk.Label(root,text='SONG TITLE').place(x=15,y=35); se1= ttk.Entry(root); se1.place(x=105,y=34)
ttk.Label(root,text='SONG TITLE').place(x=15,y=100); se2= ttk.Entry(root); se2.place(x=105,y=99)
ttk.Label(root,text='SONG TITLE').place(x=15,y=165); se3= ttk.Entry(root); se3.place(x=105,y=164)
ttk.Label(root,text='SONG TITLE').place(x=15,y=230); se4= ttk.Entry(root); se4.place(x=105,y=229)
ttk.Label(root,text='SONG TITLE').place(x=15,y=295); se5= ttk.Entry(root); se5.place(x=105,y=294)

ttk.Label(root,text='------------------------------------------------').place(x=10,y=55)
ttk.Label(root,text='------------------------------------------------').place(x=10,y=120)
ttk.Label(root,text='------------------------------------------------').place(x=10,y=185)
ttk.Label(root,text='------------------------------------------------').place(x=10,y=250)


st=[]
st1= tk.Label(root,text='',background='white',width=7,height=3); st1.place(x=275,y=9); st.append(st1)
st2= tk.Label(root,text='',background='white',width=7,height=3); st2.place(x=275,y=74); st.append(st2)
st3= tk.Label(root,text='',background='white',width=7,height=3); st3.place(x=275,y=139); st.append(st3)
st4= tk.Label(root,text='',background='white',width=7,height=3); st4.place(x=275,y=204); st.append(st4)
st5= tk.Label(root,text='',background='white',width=7,height=3); st5.place(x=275,y=269); st.append(st5)
ttk.Button(root, text='START',width=33,command=start).place(x=10,y=334)
ttk.Button(root, text='CLEAR',width=33,command=clear).place(x=10,y=364)
ttk.Button(root,text='C:\\Python\\Pyrics',width=33,command=dir).place(x=10,y=394)
root.title(pn); root.geometry('468x430+500+150'); root.mainloop()
'''
歌詞爬蟲部分參考: https://artificialintelligencepro.com.tw/python-web-scraping/
'''