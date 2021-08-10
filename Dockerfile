# FROM tiangolo/uvicorn-gunicorn:python3.8
FROM ccr.ccs.tencentyun.com/tcb-100000621900-otmp/uvicorn-gunicorn-fastapi:fastapi


# 将本地代码拷贝到容器内
COPY ./ /app


# 安装依赖
RUN pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple 

