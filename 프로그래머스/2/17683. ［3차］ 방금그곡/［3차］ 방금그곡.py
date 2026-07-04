from collections import defaultdict
def time_diff(start, end):
    start = list(map(int, start.split(':')))
    end = list(map(int, end.split(':')))
    return end[0]*60+end[1] - (start[0]*60+start[1])

def singingtime(time, song):
    ret = []
    for i in range(time):
        ret.append(song[i % len(song)])
    return ''.join(ret)
    
def solution(m, musicinfos):
    answer = ''
    info = defaultdict(int)
    titleinfo = {}
    for i in range(len(musicinfos)):
        start, end, title, song = musicinfos[i].split(',')  
        song_arr = []
        for j in range(len(song)):
            if song[j] != '#': song_arr.append(song[j])
            else: song_arr[-1] += '#'
        playtime = time_diff(start, end)
        sing = singingtime(playtime, song_arr)
        for j in range(len(sing) - len(m)+1):
            st = sing[j:j+len(m)]
            if j+len(m) < len(sing) and sing[j+len(m)] == '#': st += '#'
            if st == m: 
                info[title] += playtime
                break
        if title not in titleinfo:
            titleinfo[title] = i
            
    temp = [i for i in info if info[i] == max(info.values())]
    idx = len(musicinfos)
    for i in temp:
        if titleinfo[i] < idx: 
            answer = i
            idx = titleinfo[i]
        
    
    
    
    
    return '(None)' if len(temp) == 0 else answer