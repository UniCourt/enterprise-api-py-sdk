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

ARG SDK_VERSION
ENV SDK_VERSION $SDK_VERSION

WORKDIR /app
RUN git clone https://github.com/UniCourt/enterprise-api-py-sdk.git
RUN python enterprise-api-py-sdk/setup.py install
RUN cd enterprise-api-py-sdk/test/ && python base.py --exclude TestPacer