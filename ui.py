ui = None

def set(obj):
    global ui
    ui = obj


def get():
    return ui


def sizeof_fmt(num, suffix='B'):
    '''http://stackoverflow.com/a/1094933'''
    for unit in ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)
