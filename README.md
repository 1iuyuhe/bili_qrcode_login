# bili_qrcode_login
## 这是什么？

B站二维码扫描登录，登录后生成`cookies.txt`

## 什么是SESSDATA？

SESSDATA 是 B站 的登陆凭证，每个账户登录后都会在服务器生成一个单独的 SESSDATA，如果不刷新有效期为半个月。可以用 SESSDATA 来请求某些必须要登录状态才能访问的 API，具体可以参考[易姐文档](https://socialsisteryi.github.io/bilibili-API-collect/)

## 使用方法

克隆仓库

```bash
git clone https://github.com/1iuyuhe/bili_qrcode_login.git
```



安装依赖

```bash
pip install -r requirements.txt
```

运行

```bash
python login.py
```



## 支持与贡献

如果这个项目对你有帮助不妨点个 Star 吧，如果有什么改进建议也欢迎提交 Issue 和 Pull requests。

## 免责声明

本项目仅供学习交流使用，请勿用于任何违法、商业用途。
