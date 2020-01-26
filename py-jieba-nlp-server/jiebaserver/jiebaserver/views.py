from django.http import HttpRequest, HttpResponse
import jieba
import json

def handle_split(request:HttpRequest):
    if request.method == 'GET':
        sentence = request.GET.dict()['sentence']
        seg_list = jieba.cut(sentence)
        str_seg_list = [str(x) for x in seg_list]
        content = json.dumps({"result": str_seg_list}, ensure_ascii=False, indent=2)
        resp = HttpResponse(content, status=200, 
            content_type='application/json; charset=utf-8')
        resp['Access-Control-Allow-Origin'] = '*'
        resp['Access-Control-Allow-Methods'] = 'POST,GET'
        resp['Access-Control-Allow-Headers'] = 'Content-Type'
        return resp