FROM registry-vpc.cn-hangzhou.aliyuncs.com/meritfit_test/merit-auto:v2
RUN rm -rf /home/*
COPY . /home/
WORKDIR /home/
CMD ["python3","run.py"]
