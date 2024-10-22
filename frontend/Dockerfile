FROM node:12.18.2 as build

ARG REACT_APP_SERVICES_HOST=/services/m

WORKDIR /app/frontend

COPY ./package.json /app/frontend//package.json
COPY ./package-lock.json /app/frontend/package-lock.json

RUN npm install
COPY . .
RUN npm run build


FROM nginx
COPY ./nginx/nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=build /app/frontend/build /usr/share/nginx/html