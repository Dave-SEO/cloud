'''
Date: 2021-06-18 11:02:37
LastEditors: 景焱
LastEditTime: 2021-08-10 14:49:09
FilePath: /cloudtest/main.py
'''
import sys
sys.path.append('.')

import uvicorn
from fastapi import FastAPI,Body
from fastapi.middleware.cors import CORSMiddleware

# MYsql 查询时链接 结束时关闭

app = FastAPI()


@app.get('/')
def root():
    return {"message": "hello word"}

# 一级分类
@app.get("/h5/category", tags=["一级分类"])
async def category():
    category = [
        {'key': '裙装','label': '裙装' },
        {'key': '上衣','label': '上衣'},
        {'key': '外套','label': '外套'},
        {'key': '裤装','label': '裤装'},
        {'key': '套装','label': '套装'},

    ]
    data = {
        "code": 200,
        "msg": '一级类目',
        "data": category
    }
    return data



# 二级分类
@app.post("/h5/categorySecond", tags=["二级分类"])
async def categorySecond(categoryName: str = Body(1, title='一级分类ID', embed=True)):
    print(categoryName)
    if categoryName == '裙装':
        
        category = [
            {'key': '连衣裙','label': '连衣裙' ,'category_img': "https://mp-1253698321.cos.ap-shanghai.myqcloud.com/categoryimg/连衣裙.jpg"},
            {'key': '半身裙','label': '半身裙','category_img': "https://mp-1253698321.cos.ap-shanghai.myqcloud.com/categoryimg/半身裙.jpg"},
        ]
        color = [
        {'key': '红色','label': '红色'},
        {'key': '粉色','label': '粉色'},
        {'key': '黑色','label': '黑色'},
        {'key': '紫色', 'label': '紫色'},
        {'key': '白色','label': '白色'},
        {'key': '藏青','label': '藏青'},
        {'key': '橘色','label': '橘色'},
        ]
        size = [
        {'key': 'S','label': 'S'},
        {'key': 'M','label': 'M'},
        {'key': 'L', 'label': 'L'},
        {'key': 'XL', 'label': 'XL'},
        {'key': 'XXL','label': 'XXL'},
        {'key': '均码','label': '均码'}
    ]
    
        resullt = {'cateory':category,'color':color,'size':size}
        
    elif categoryName == '上衣':
        category = [
            {'key': 'T恤','label': 'T恤' ,'category_img': "https://mp-1253698321.cos.ap-shanghai.myqcloud.com/categoryimg/连衣裙.jpg"},
            {'key': '背心','label': '背心','category_img': "https://mp-1253698321.cos.ap-shanghai.myqcloud.com/categoryimg/半身裙.jpg"},
            {'key': '衬衫','label': '衬衫','category_img': "https://mp-1253698321.cos.ap-shanghai.myqcloud.com/categoryimg/半身裙.jpg"},
        ]
        color = [
        {'key': '红色','label': '红色'},
        {'key': '粉色','label': '粉色'},
        {'key': '黑色','label': '黑色'},
        {'key': '紫色', 'label': '紫色'},
        {'key': '白色','label': '白色'},
        {'key': '藏青','label': '藏青'},
        {'key': '橘色','label': '橘色'},
        ]
        resullt = {'cateory':category,'color':color}
        
    elif categoryName == '外套':
        category = [
            {'key': '西装外套','label': 'T恤' ,'category_img': "https://mp-1253698321.cos.ap-shanghai.myqcloud.com/categoryimg/连衣裙.jpg"},
        ]
        
        size = [
        {'key': 'S','label': 'S'},
        {'key': 'M','label': 'M'},
        {'key': 'L', 'label': 'L'},
        {'key': 'XL', 'label': 'XL'},
        {'key': 'XXL','label': 'XXL'},
        {'key': '均码','label': '均码'}
        ]
        
        resullt = {'cateory':category,'size':size}
                
    elif categoryName == '裤装':
        category = [
            {'key': '休闲裤','label': '休闲裤' ,'category_img': "https://mp-1253698321.cos.ap-shanghai.myqcloud.com/categoryimg/连衣裙.jpg"},
            {'key': '阔腿裤','label': '阔腿裤' ,'category_img': "https://mp-1253698321.cos.ap-shanghai.myqcloud.com/categoryimg/连衣裙.jpg"},
            {'key': '西装裤','label': '西装裤' ,'category_img': "https://mp-1253698321.cos.ap-shanghai.myqcloud.com/categoryimg/连衣裙.jpg"},
            {'key': '牛仔裤','label': '牛仔裤' ,'category_img': "https://mp-1253698321.cos.ap-shanghai.myqcloud.com/categoryimg/连衣裙.jpg"},
            {'key': '九分裤','label': '九分裤' ,'category_img': "https://mp-1253698321.cos.ap-shanghai.myqcloud.com/categoryimg/连衣裙.jpg"},
            {'key': '长裤','label': '长裤' ,'category_img': "https://mp-1253698321.cos.ap-shanghai.myqcloud.com/categoryimg/连衣裙.jpg"},
        
        ]
        color = [
        {'key': '红色','label': '红色'},
        {'key': '粉色','label': '粉色'},
        {'key': '黑色','label': '黑色'},
        {'key': '紫色', 'label': '紫色'},
        {'key': '白色','label': '白色'},
        {'key': '藏青','label': '藏青'},
        {'key': '橘色','label': '橘色'},
        ]
        
        resullt = {'cateory':category,'color':color}
        
    elif categoryName == '套装':
        category = [
            {'key': '两件套','label': '两件套' ,'category_img': "https://mp-1253698321.cos.ap-shanghai.myqcloud.com/categoryimg/连衣裙.jpg"},
            {'key': '套装','label': '套装' ,'category_img': "https://mp-1253698321.cos.ap-shanghai.myqcloud.com/categoryimg/连衣裙.jpg"},
        ]
        resullt = {'cateory':category}
        
    data = {
        "code": 200,
        "msg": f'{categoryName}二级类目',
        "data": resullt
    }
    return data


# 后台api允许跨域
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



if __name__ == '__main__':
    
    uvicorn.run(app='main:app', host='0.0.0.0',port=9166, debug=False, reload=True)
    
