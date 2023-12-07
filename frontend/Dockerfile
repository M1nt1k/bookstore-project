FROM node:19.5.0-alpine

RUN npm install -g http-server

WORKDIR /app/frontend

COPY package*.json ./

RUN npm install --force

COPY . .