# Dockerfile
FROM node:14.17.0-alpine

# create destination directory
RUN mkdir -p /usr/src/nuxt
WORKDIR /usr/src/nuxt

# update and install dependency
RUN apk update && apk upgrade
RUN apk add git

# copy the app, note .dockerignore
COPY ./todo_front /usr/src/nuxt/
RUN npm install
RUN npm run build

EXPOSE 3000

ENV NUXT_HOST=0.0.0.0
ENV NUXT_PORT=3000

# CMD [ "yarn", "dev" ]
CMD [ "npm", "run", "start" ]
