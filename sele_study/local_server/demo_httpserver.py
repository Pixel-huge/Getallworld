#!/usr/bin/env python 
# coding:utf-8

from http.server import HTTPServer, BaseHTTPRequestHandler

# 第一个模板—创建一个自创表格信息的网页，并本地启动服务访问

# 定义一个 HTML 页面
PAGE_HTML = '''
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>人员信息</title>
    <style>
        table, th, td {
            border: 1px solid black;
            border-collapse: collapse;
            padding: 5px;
        }
    </style>
</head>
<body>
    <h1>人员信息</h1>
    <table>
        <thead>
            <tr>
                <th>姓名</th>
                <th>年龄</th>
                <th>性别</th>
                <th>爱好</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>张三</td>
                <td>25</td>
                <td>男</td>
                <td>足球</td>
            </tr>
            <tr>
                <td>李四</td>
                <td>32</td>
                <td>男</td>
                <td>篮球</td>
            </tr>
            <tr>
                <td>王五</td>
                <td>27</td>
                <td>男</td>
                <td>羽毛球</td>
            </tr>
        </tbody>
    </table>
</body>
</html>
'''

# 定义一个简单的 HTTP 请求处理类，用于响应 GET 请求
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # 设置响应头
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # 将 HTML 页面作为响应体返回
        self.wfile.write(bytes(PAGE_HTML, 'utf-8'))


# 创建一个 HTTP 服务器并启动它
server_address = ('', 8000)
httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
print('正在监听 http://localhost:8000')
httpd.serve_forever()
