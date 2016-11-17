FROM python:3.5

ENV APP_ROOT /app
WORKDIR $APP_ROOT

ADD requirements.txt setup.py $APP_ROOT/
RUN pip install -r requirements.txt

ADD image image
ENV PATH $APP_ROOT/image:$PATH

ADD bonus bonus
ADD myapp myapp
ADD myapp_ripozo myapp_ripozo
ADD myapp_tests myapp_tests

RUN python setup.py install

CMD ["run-ripozo"]
