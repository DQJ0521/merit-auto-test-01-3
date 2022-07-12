FROM registry-vpc.cn-hangzhou.aliyuncs.com/meritfit_test/merit-auto:V1
ENV LANG en_US.UTF-8 LC_ALL=en_US.UTF-8
COPY . /home/
ENV PYTHONIOENCODING=utf-8
WORKDIR /home/
CMD ["python3","/home/run.py"]
