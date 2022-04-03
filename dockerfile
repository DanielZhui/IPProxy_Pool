FROM python:3.9

ADD . /code
WORKDIR /code

RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
# 保证 /etc/localtime 和 /etc/timezone 时区一致
RUN echo "Asia/Shanghai" > /etc/timezone

RUN pip install -r /code/requirements.txt