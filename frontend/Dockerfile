FROM node:10 as build

WORKDIR /opt/project

ADD package.json package-lock.json ./
RUN npm install

ADD . /opt/project
RUN npm run build


FROM nginx:1.15 as dist

COPY --from=build /opt/project/dist /usr/share/nginx/html
COPY nginx-server.conf /etc/nginx/conf.d/default.conf
