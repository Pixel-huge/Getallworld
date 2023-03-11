#!/usr/bin/env python 
# coding:utf-8

from fastapi import FastAPI

#起应用服务

app = FastAPI()

@app.get("/")
async def root():
    return {"message":"Hello World"}


# 起服务 命令  uvicorn demo_fastapi.py:app --reload



