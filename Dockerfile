FROM python:3.6
ADD . /root
RUN pip3 install -r /root/requirements.txt
EXPOSE 5000
CMD ["python3","/root/app.py"]