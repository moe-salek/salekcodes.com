# front build stage:
FROM node:21-alpine3.17 as front_build

WORKDIR /app
COPY . .

RUN npm install
RUN npm run build

# production stage:
FROM node:21-slim

WORKDIR /app
COPY --from=front_build /app/dist /app/dist

RUN npm install -g http-server

EXPOSE 8000

CMD ["http-server", "dist", "-p", "8000"]
