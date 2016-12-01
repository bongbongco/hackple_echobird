# -*- coding: utf-8 -*-
#!/usr/bin/python

import sys
from datetime import datetime
from flask import Flask, request, session, redirect, url_for, abort, render_template, flash
#from Config import GetTheConfig, WriteTheConfig
#from app.storage.Database import now, executeNcommit, executeNfetchall
#from app.search.GatheringInformation import GatheringInformation
app = Flask(__name__)

reload(sys)  
sys.setdefaultencoding('utf8')

app.config.update(dict(
	DEBUG=True,
	SECRET_KEY='development key',
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)


@app.route('/')
@app.route('/talk/<talk>')
def show_talk(talk="핵플에서 운영하는 카카오톡 테마의 익명 페이스북 포스팅 봇입니다."):
    now = datetime.now()
    nowTime = "%02d:%02d" % (now.hour, now.minute)
    passerTalks = ['...', '누가 들은 건 아니겠지? 어서 자리를 피해야겠다.']
    birdTalks = ['echo', '"', talk,'"']
    name = "행인"
    return render_template('hackple_ktalk.html', passerTalks=passerTalks, birdTalks=birdTalks, time=nowTime, name=name)

if __name__ == '__main__':
    app.run()