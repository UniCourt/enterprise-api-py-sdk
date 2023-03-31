FROM python:3.9.12-alpine3.15 
RUN apk add --update git 

ARG CLIENT_ID
ENV CLIENT_ID $CLIENT_ID

ARG CLIENT_SECRET
ENV CLIENT_SECRET $CLIENT_SECRET


ARG PACER_CLIENT_CODE
ENV PACER_CLIENT_CODE $PACER_CLIENT_CODE


ARG PACER_USER_ID
ENV PACER_USER_ID $PACER_USER_ID

WORKDIR /app
RUN git clone https://github.com/UniCourt/enterprise-api-py-sdk.git
RUN python enterprise-api-py-sdk/setup.py install
RUN python enterprise-api-py-sdk/test/base.py --exclude TestPacer

# docker build -t test_sdh --build-arg CLIENT_ID=G3cfixgetVzfaoszGOBp5LPGtih1nMJ9 --build-arg CLIENT_SECRET=u6PTti57IjPlrwU5MzOwLBD2MCwx-IEbo8sTStTivh1I-EqQ8Jcm27Gfo2GhpHCw --build-arg PACER_CLIENT_CODE=xyz_client --build-arg PACER_USER_ID=pcrid .