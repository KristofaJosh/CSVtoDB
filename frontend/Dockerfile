FROM node

MAINTAINER Chris Josh "christopherjoshua25@hotmail.com"

WORKDIR /zenoContainer/frontend

COPY package.json /zenoContainer/frontend
COPY yarn.lock /zenoContainer/frontend

RUN yarn install
COPY . /zenoContainer/frontend

EXPOSE 3000

CMD ["yarn", "start"]

