npm init
npm install json-server --save
json-server --watch src/db.json
curl http://localhost:3000/employees
curl http://localhost:3000/employees/4